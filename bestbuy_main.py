import os
from gpu_restock.bestbuy_stock import StockChecking
import time

TESTING = False

url_root = os.path.abspath(os.path.dirname(__file__))
url_path = os.path.join(url_root, "gpu_restock/bestbuy_url.txt")

with open(url_path) as f:
    url = f.readlines()
    url = [line.rstrip() for line in url]

bots = []
for i in range(len(url)):
    bots.append(StockChecking(url=url[i]))

if TESTING:
    start_time = time.time()
    seconds = 15

try:
    for bot in bots:
        bot.load_page()

    while True:

        for bot in bots:
            time.sleep(5)
            bot.refresh()
            bot.run()
            # bot.check()

        if TESTING:
            current_time = time.time()
            elapsed_time = current_time - start_time

            if elapsed_time > seconds:
                print("Finished iterating in: " + str(int(elapsed_time)) + " seconds")
                break

except Exception as e:
    raise
