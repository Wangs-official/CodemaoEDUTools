# @author:Wangs_official
try:
    import requests
except ImportError:
    exit("请先 pip3 install requests")
import time
import json
import os


def call_api(path, data, token):
    url = f"https://api.codemao.cn/{path}"
    header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "authorization": f"{token}"
    }
    post_text = data
    return requests.post(url, data=post_text, headers=header)


def get_api(path, token):
    url = f"https://api.codemao.cn/{path}"
    header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "authorization": f"{token}"
    }
    post_text = json.dumps(data)
    return requests.get(url, headers=header)
