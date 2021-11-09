from restock.bestbuy_stock import BestBuyStock
from restock.basic import Colors


def table_format(time, item, merchant, price, availability, title=False):
    title_format = time.center(19), item.center(100), merchant.center(12), price.center(10), availability.center(20)
    gap_format = time.center(19), item.center(100), merchant.center(12), price.center(12), availability.center(20)
    if title:
        print(Colors.BOLD + "%s | %s | %s | %s | %s" % title_format + Colors.ENDC)
    elif availability == 0:
        avail = 'Sold Out'
        print("%s | %s | %s |" % gap_format[0:3]
              + Colors.HEADER + "%s" % gap_format[3] + Colors.ENDC
              + '|' + Colors.WARNING + "%s" % avail.center(20) + Colors.ENDC + "\n",
              flush=True, end='\r')
    elif availability == 1:
        avail = 'In Stock'
        print("%s | %s | %s |" % gap_format[0:3]
              + Colors.HEADER + "%s" % gap_format[3] + Colors.ENDC
              + '|' + Colors.OKGREEN + "%s" % avail.center(20) + Colors.ENDC + "\n",
              flush=True, end='\r')
    else:
        print("%s | %s | %s |" % gap_format[0:3]
              + Colors.HEADER + "%s" % gap_format[3] + Colors.ENDC
              + '|' + Colors.WARNING + "%s" % gap_format[4] + Colors.ENDC + "\n",
              flush=True, end='\r')


def status(bot: BestBuyStock, num, idx):
    table_format(bot.st.time, bot.st.item, bot.st.merchant, bot.st.price, bot.st.availability)
    print(u'\u2500' * 180, '\n', end='\r')
    if idx == num - 1:
        print("\033[F" * (2 * num + 1))


def rt_status(availability, current_time):
    if availability == 0:
        print(f'[{current_time}]' + Colors.HEADER + ' Status: ' + Colors.WARNING + 'Out of Stock' + Colors.ENDC)
    elif availability == 1:
        print(f'[{current_time}]' + Colors.HEADER + ' Status: ' + Colors.OKGREEN + 'In Stock !!' + Colors.ENDC)
    else:
        print(f'[{current_time}]' + Colors.WARNING + " Can't get the status" + Colors.ENDC)


def flow_format(bot: BestBuyStock):
    print(bot.st.item)
    print(f'[{bot.st.time}]' + Colors.HEADER + ' Price:' + Colors.ENDC, end=" ")
    print(bot.st.price)
    rt_status(bot.st.availability, bot.st.time)
