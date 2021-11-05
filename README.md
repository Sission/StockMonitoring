# Stock Monitoring

## Description

It is a stock monitoring script. This repository is still under developing.

### Monitoring Websites (for now)

- BestBuy
- Adorama (Can not bypass the CAPTCHA now. Working on that)
- MicroCenter (Location: MA; changeable)

## Getting Started

### Prerequisites & Installing

This script is being tested on macOS. For Windows and Ubuntu user, replacing selenium driver should be necessary.
```
pip install selenium
git clone https://github.com/Sission/StockMonitoring.git
```
Add the url of your desired item in to *url.txt*

### Executing Program

```
python run main.py --print_format <format>
```


### Example
#### Table mode

```
python run main.py --print_format "Tabel"
```
<img src="Examples/TableOutput.png">

#### Flow mode

```
python run main.py --print_format "Flow"
```

<img src="Examples/FlowOutput.png">

### Future Functions
 - Monitor other websites such as Newegg.com
 - Send notification via text or Webhook
 - Automatically check out
 - Docker package
 