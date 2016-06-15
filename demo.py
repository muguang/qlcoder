


import string
import datetime
import hashlib
import threading
import requests
import time
raw_url = "http://www.qlcoder.com/train/handsomerank?_token=9IDQrlei6wgW0VN8CrrLs2edkX7LIepoK0bWE5FJ&user=a%7C%7C%7CupOI&checkcode="



list = []
with open("result.txt", "r") as f:
    while True:
        text = f.readline()
        if not text:
            break
        # print(text)
        s = requests.session()
        order = text.split(" ")[0]
        captcha = text.split(" ")[1]
        print(order)
        print(captcha)
        full_url = raw_url + str(captcha)
        print(full_url)

        s = requests.get(full_url)


        time.sleep(1)
        print(s.text)

        # print(s.text)
        # time.sleep(0.1)
