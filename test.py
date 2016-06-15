import requests

raw_url = "http://www.qlcoder.com/train/handsomerank?_token=9IDQrlei6wgW0VN8CrrLs2edkX7LIepoK0bWE5FJ&user=a%7C%7C%7CupOI&checkcode="

captcha = 1




with open("a.txt", "r") as f:
    tt = f.readlines()


# print(tt)

for i in tt:
#     print(tt)
    temp = i.split(" ")[1].strip()

#     print(type(tt))
    full_url = raw_url+temp
    print(full_url)
#
#
    s = requests.get(full_url)
    print(s.text)
#
#
