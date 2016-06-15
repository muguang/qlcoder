import requests


"""


http://www.qlcoder.com/task/4/solve?answer=restful&_token=9IDQrlei6wgW0VN8CrrLs2edkX7LIepoK0bWE5FJ
"""

url = "http://www.qlcoder.com/task/4/solve"
#url = "http://www.qlcoder.com/task/7527"


Header = {
    "_token": "9IDQrlei6wgW0VN8CrrLs2edkX7LIepoK0bWE5FJ"
}

data = {
    "answer": "restful"

}




s = requests.post(url=url, headers=Header,data=data)