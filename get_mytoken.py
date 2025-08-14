try:
    import requests
except ImportError:
    exit("请先 pip3 install requests")

import json


def login(username, pwd):
    url = "https://api.codemao.cn/tiger/v3/web/accounts/login"
    header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    post_text = json.dumps({'pid': '65edCTyg', 'identity': username, 'password': pwd})
    return requests.post(url, data=post_text, headers=header)


uname = input("请输入账号:")
password = input("请输入密码")
login_req = login(uname, password)

if login_req.status_code == 200:
    token = json.loads(login_req.text).get("auth", {}).get("token")
    exit(f"你的Token是\n{token}")
else:
    exit(f"出现异常: {login_req.text}")

