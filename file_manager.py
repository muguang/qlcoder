



"""
这里需要将这些垃圾归类，并计算其大小，之后根据用户需求删除或继续保留。
这里有一个文件夹，答案就在里面最大的text文档里面。


import os
dir="e:\\"
for root,dirs,files in os.walk(dir):
    for file in files:
        print os.path.join(root,file)


import os.path
def processDirectory ( args, dirname, filenames ):
    print 'Directory',dirname
    for filename in filenames:
        print ' File',filename
"""

import os
# import

dict_file = {}



for root, dirs, files in os.walk("root"):
    for file in files:
        # print(os.path.join(root, file))
        filename = os.path.join(root, file)
        filesize = os.path.getsize(filename)
        dict_file[filename] = filesize


# print(dict_file)


for key, values in dict_file.items():
    if values>21:
        print(key, values)


#
# sorted(dict_file.items(), key = lambda x:x[1])
#
# print(dict_file)
#
print(dict_file)







