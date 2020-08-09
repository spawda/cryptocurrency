# Cryptocurrency
This repository holds the codes for cryptocurrency.     
Some codes use [coincheck api](https://coincheck.com/ja/documents/exchange/api). Coincheck official Python-api-tool is [here](https://github.com/coincheckjp/coincheck-python).     
I'm planning to add a price prediction program and an automated trading program.

## development environment
- Python 3.7.3    
- requests 2.22.0

## How to use
### make_dataset.py
Gathering and saving BTC/JPY price data per minute from coinckeck API (Public). You don't have to sign up for coincheck account to use this script.   
`> python make_dataset.py --save_dir [save directory path]`   
--save_dir is optional and if not specified, current directory is used.

example : `python make_dataset.py --save_dir ./btc_jpy`    

Price data is written in csv file, each line stores the following:
```
date : date (JST, GMT +09:00)
time : time (JST, GMT +09:00)
last : Latest quote (最後の取引の価格)
bid : Current highest buying order (現在の買い板の最高価格)
ask : Current lowest selling order (現在の売り板の最低価格)
high : The highest price within 24 hours (過去24時間での最高取引価格)
low : The lowest price within 24 hours (過去24時間での最低取引価格)
volume : 24 hours trading volume (過去24時間での取引量)
timestamp : timestamp (価格取得時のtimestamp)
```
If API HTTP status code is not `200`, status code is written instead of the price data.