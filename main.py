import os
import time
from restock.merchant_classify import classify
from datetime import datetime
from restock.dynamic_monitor import status, table_format, flow_format
import argparse


def parse_args():
    desc = "Stock Monitoring"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--print_format', type=str, default='Flow')
    parser.add_argument('--testing', type=bool, default=False)
    return check_args(parser.parse_args())


"""checking arguments"""


def check_args(args):
    # --printing format
    try:
        assert args.print_format == 'Table' or args.print_format == 'Flow'
    except (Exception,):
        print('Unsupported printing format')
        return None
    return args


def main(args):
    TESTING = args.testing
    PRINT_FORMAT = args.print_format
    start_time = time.time()
    seconds = 15
    url_root = os.path.abspath(os.path.dirname(__file__))
    url_path = os.path.join(url_root, "restock/url.txt")
    try:
        print('Loading the bots ...')
        bots, num = classify(url_path=url_path)
        print("Bots loaded!")

    except Exception:
        print('Bots load failed')
        raise

    try:
        print('Loading the pages ...')
        for bot in bots:
            bot.load_page()
        print("Pages loaded!")

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
                    status(bot, num, idx)
                elif PRINT_FORMAT == 'Flow':
                    flow_format(bot)

            time.sleep(5)
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
