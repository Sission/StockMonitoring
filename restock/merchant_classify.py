from restock.bestbuy_stock import BestBuyStock
from restock.adorama_stock import AdoramaStock
from restock.microcenter_stock import MicroCenterStock


def classify(url_path):
    bots = []
    bestbuy = ['bestbuy']
    adorama = ['adorama']
    microcenter = ['microcenter']
    with open(url_path) as f:
        url = f.readlines()
        url = [line.rstrip() for line in url]

    num = len(url)

    for i in range(num):
        merchant = (url[i].split("www.", 1)[1].split(".com", 1)[0])
        if bool([ele for ele in bestbuy if (ele in merchant.lower())]):
            bots.append(BestBuyStock(url=url[i], merchant='BestBuy'))

        elif bool([ele for ele in adorama if (ele in merchant.lower())]):
            bots.append(AdoramaStock(url=url[i], merchant='Adorama'))

        elif bool([ele for ele in microcenter if (ele in merchant.lower())]):
            bots.append(MicroCenterStock(url=url[i], merchant='MicroCenter'))

        else:
            print('Assign bots failed!')

    return bots, num
