"""

每一个网站都会根据访客日志统计访客数据，比如UV。UV能够回答一个关键的市场营销问题：“到底有多少人（潜在客户）看到了你发布的信息（即网站）。
下面根据题目给出的某购物网站访问日志，统计当天该网站UV。日志文件的每一行代表一次访问行为，每行分别包含三项，用户访问的时间，用户的id，用户的行为。请问8月24号当天，该网站有多少个用户访问了。

"""

f = open("uv.txt")

list_user = []


s = f.readlines()

print(len(s))
len_l = len(s)


for i in range(len_l):
    ss = s[i]
    user_id = ss.split(" ")[1]
    if user_id not in list_user:
        list_user.append(user_id)
        print(len(list_user))



print(len(list_user))


# while True:
#
#
#     #print(s)

#  Python print(len({i.split(' ')[1] for i in open('./uv.txt')}))


