"""
一般点赞这种行为会设计一个验证码…来区别您是普通人还是机器…

我们网站是coder专享的…验证码当然会难一点啦~


这里的验证码是一个自然数x…他能使 md5(当天日期+你的用户名+当前的票数+x)的前6位都是0…

举例: 假如2015年12月4号食年已经拿到了1014票,当你想投第1015票的时候,你的验证码可以是12011618,
因为 "20151204shinian101412011618"的md5值是"0000003A19CF73CF3E9799219A9FFF4F",这个md5前6位都是0…


http://www.qlcoder.com/train/handsomerank?_token=9IDQrlei6wgW0VN8CrrLs2edkX7LIepoK0bWE5FJ&user=a%7C%7C%7CupOI&checkcode=12


md5(当天日期+你的用户名+当前的票数+x)的前6位都是0
"""


import requests
import string
import datetime
import hashlib
import threading


raw_url = "http://www.qlcoder.com/train/handsomerank?_token=9IDQrlei6wgW0VN8CrrLs2edkX7LIepoK0bWE5FJ&user=a%7C%7C%7CupOI&checkcode="


data = datetime.datetime.now()
data = str(data).split(' ')[0].split("-")
data = "".join(data)
print(data)

username = "a|||upOI"



captcha = 0
order = 244

list = []



def analysis_captcha(captcha, order):
    captcha = 0
    while True:
        captcha = captcha+1
        temp = data+username+str(order)+ str(captcha)
        temp_md5 = hashlib.md5(temp.encode(encoding="utf-8"))
        temp_md5 = temp_md5.hexdigest()
        aa = temp_md5[:6]
        # print(aa)

        if aa == "000000":
            print("aa:", aa)
            print(temp)
            print(temp_md5)
            list.append(captcha)
            print()
            print("succeed ")
            print(captcha)
            return captcha


while order <1001:
    captcha_temp = analysis_captcha(captcha, order)
    full_url = raw_url+str(captcha_temp)
    # print(full_url)
    s = requests.get(full_url)
    # print(s.text)
    order = order +1


# full_url = raw_url+str(captcha)
# s = requests.get(full_url)
# print(s.text)







