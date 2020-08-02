import requests
import datetime
from datetime import datetime, timedelta, timezone
import os
import argparse
import time
import threading


# make dataset from coincheck api
def save_btc_price(save_dir):
    path = os.path.join(save_dir, 'btc_jpy_{}.csv'.format(datetime.now().strftime("%Y%m%d")))
    if not os.path.exists(path):
        with open(path, "w") as fp:
            fp.write("date,time,last,bid,ask,high,low,volume,timestamp\n")
        print("make csv file: " + path)
    with open(path, "a") as fp:
        r = requests.get("https://coincheck.com/api/ticker")
        date_str = datetime.now().strftime("%Y-%m-%d")
        time_str = datetime.now().strftime("%H:%M:%S")
        if r.status_code == 200:
            item = r.json()
            item["date"] = date_str
            item["time"] = time_str
            line = "%(date)s,%(time)s,%(last)s,%(bid)s,%(ask)s,%(high)s,%(low)s,%(volume)s,%(timestamp)s" % item
            fp.write(line + "\n")
            print(line)
        else:
            error_message = 'status code {}'.format(r.status_code)
            line = '{0},{1},{2},{2},{2},{2},{2},{2},{2}'.format(date_str, time_str, error_message)
            fp.write(line + "\n")
            print('{},{} API error : status code {}'.format(date_str, time_str, r.status_code))


# run at regular intervals
def periodic_execution(interval, function, argument):
    base_time = time.time()
    while True:
        thread = threading.Thread(target=function, args=([argument]))
        thread.start()
        time.sleep((base_time - time.time()) % interval)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_dir', type=str, default="./")
    args = parser.parse_args()
    save_dir = args.save_dir
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    JST = timezone(timedelta(hours=+9), 'JST')
    time_now = datetime.now(JST)
    time.sleep(60-time_now.second)

    periodic_execution(60, save_btc_price, save_dir)
