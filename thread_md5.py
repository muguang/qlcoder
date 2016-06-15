


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
order = 11
dict = {}





def analysis_captcha(captcha, order):
    captcha = 0
    while True:
        captcha = captcha+1
        temp = data+username+str(order)+ str(captcha)
        temp_md5 = hashlib.md5(temp.encode(encoding="utf-8"))
        temp_md5 = temp_md5.hexdigest()
        aa = temp_md5[:6]
        #print(aa)

        if aa == "000000":

            dict[order] = captcha
            print(order, captcha)
            with open("tt.txt", "a") as f:
                f.write(str(order),)
                f.write(' ')
                f.write(str(captcha))
                f.write('\n')
            return captcha


a = 796

for i in range(a, a+100, 2):
    t2 = threading.Thread(target=analysis_captcha(0, i))
    t3 = threading.Thread(target=analysis_captcha(0, i+1))


t2.start()
t3.start()


"""

70119044832
70216785266



950, 12808242

"""

