# Stock Monitoring

## Description

It is a stock monitoring script. This repository is still under developing.

### Monitoring Websites (for now)

- BestBuy
- Adorama (Can not bypass the CAPTCHA now. Working on that)
- MicroCenter (Location: MA; changeable)

## Getting Started

### Prerequisites & Installing

```
pip install -r requirements.txt
git clone https://github.com/Sission/StockMonitoring.git
```
Add the url of your desired item in to *url.txt*

Add telegram bot configuration to get real time notification. Check [this](https://core.telegram.org/bots) to see how
to add a telegram bot.

Create file *telegram_info.txt* under folder *restock* to store your _api_key_ and
_user_id_ of telegram. 

```
api_key = '<your api key>'
user_id = '<your user id>>'
```


### Executing Program

```
python run main.py --print_format <format> --os <OS> --refresh_rate <to refresh the page> 
```


### Example
#### Table mode

```
python run main.py --print_format "Tabel" --os MacOS
```
<img src="Examples/TableOutput.png">

#### Flow mode

```
python run main.py --print_format "Flow" --os Windows
```

<img src="Examples/FlowOutput.png">

### Future Functions
 - Docker package in Windows
 - Monitor other websites such as Newegg.com
 - Automatically check out