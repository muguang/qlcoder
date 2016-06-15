"""


1	509
2	838
3	924
4	650
5	604
6	793
7	564
8	651
9	697
10	649
11	747
12	787
13	701
14	605
15	644

载重 5t


背包问题?


"""

ss = """

1	509
2	838
3	924
4	650
5	604
6	793
7	564
8	651
9	697
10	649
11	747
12	787
13	701
14	605
15	644
"""

dict_weight = {}

ss = ss.strip()
ss = ss.replace("\t", ' ')
ss = ss.replace("\n", " ")
ss = ss.split(" ")

print(ss)
for i in range(0,30,2):
    dict_weight[int(ss[i])] = int(ss[i+1])

print(dict_weight)


def
