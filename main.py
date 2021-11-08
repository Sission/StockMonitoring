import os
import time
from restock.merchant_classify import classify
from datetime import datetime
from restock.basic import Colors, Setting
from restock.dynamic_monitor import status, table_format, flow_format
import argparse
from restock.basic import telegram_communicator, telegram_info
import schedule


def parse_args():
    desc = "Stock Monitoring"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--print_format', type=str, default='Flow')
    parser.add_argument('--testing', type=bool, default=False)
    parser.add_argument('--refresh_rate', type=int, default=5)
    parser.add_argument('--os', type=str, default='MacOS')

    return check_args(parser.parse_args())


"""checking arguments"""


def check_args(args):
    # --printing format
    try:
        assert args.print_format == 'Table' or args.print_format == 'Flow'
    except (Exception,):
        print('Unsupported printing format')
        return None

    # Running mode
    try:
        assert args.testing or not args.testing
    except (Exception,):
        print('Unsupported running mode')
        return None

    # Refresh_rate
    try:
        assert type(args.refresh_rate) is int
    except (Exception,):
        print('Unsupported refresh_rate')
        return None

    try:
        assert type(args.os) is str
    except (Exception,):
        print('Unsupported Operating System')
        return None
    return args


def main(args):
    TESTING = args.testing
    PRINT_FORMAT = args.print_format
    refresh_rate = args.refresh_rate
    OS = args.os
    start_time = time.time()
    seconds = 15
    url_root = os.path.abspath(os.path.dirname(__file__))
    url_path = os.path.join(url_root, "restock/url.txt")
    tele_path = os.path.join(url_root, "restock/telegram_info.txt")
    try:
        print('Loading the bots ...')
        st = Setting(OS)
        bots, num = classify(url_path=url_path, st=st)
        print("Bots loaded!")
        api_key, user_id = telegram_info(tele_path)
    except (Exception,):
        print('Bots load failed')
        raise

    try:
        print('Loading the pages ...')
        for bot in bots:
            bot.load_page()
        print("Pages loaded!")
        telegram_communicator(api_key, user_id, 'Stock Monitor is loaded')

        if PRINT_FORMAT == 'Table':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(u'\u2500' * 180, '\n', end='\r')
            table_format('Time', 'Item', 'Merchant', 'Price', 'Availability', title=True)
            print(u'\u2500' * 180, '\n', end='\r')

        while True:
            for idx, bot in enumerate(bots):
                bot.refresh()
                now = datetime.now()
                current_time = now.strftime("%Y-%m-%d %H:%M:%S")
                bot.run(current_time)
                if PRINT_FORMAT == 'Table':
                    avail_status = status(bot, num, idx)
                elif PRINT_FORMAT == 'Flow':
                    avail_status = flow_format(bot)
                if avail_status:
                    telegram_communicator(api_key, user_id, f'{bot.st.item} in Stock Now!')
                    telegram_communicator(api_key, user_id, f'{bot.url}')
                if datetime.now().hour > 8 and (datetime.now().hour % 2)-1:
                    if datetime.now().minute == 0:
                        telegram_communicator(api_key, user_id, 'Stock Monitor is working!!')

            time.sleep(refresh_rate)
            if TESTING:
                current_time = time.time()
                elapsed_time = current_time - start_time

                if elapsed_time > seconds:
                    print("Finished iterating in: " + str(int(elapsed_time)) + " seconds")
                    break

    except Exception:
        raise


if __name__ == '__main__':

    # parse arguments
    arg = parse_args()
    if arg is None:
        exit()

    # main
    main(arg)
