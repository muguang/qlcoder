import requests
import re
# from bs4 import BeautifulSoup
raw_url = "https://movie.douban.com/top250?start={}"

number =0


# s = requests.session()
list_all = []


def get_onepage():
    global number
    url = raw_url.format(number)
    number += 25
    r = requests.get(url=url)
    list = re.findall(r'v:average\">([1-9]\d*.\d*|0.\d*[1-9]\d*)<', r.text)
    print(list)
    with open("result_of_score", "a") as f:

        f.writelines(str(list)+'\n')
    list_all.append(list)

def analysis():
    sum = 0
    count = 0
    for i in range(166//25+1):
        get_onepage()

sum=0
def analysis2():
    global sum
    with open("result_of_score", "r") as f:
        t = f.read().replace("'", "").replace(",", "").replace("[", "").replace(']', "").strip().split()

        # t = str(list)
    print(len(t))
    for i in range(166):
        sum += float(t[i])



if __name__ == '__main__':

    analysis()

    analysis2()

    print("sum :", sum)
