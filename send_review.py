# @author:Wangs_official
import os
import queue
import threading
import time
import requests
import json

import control as c

if not os.path.exists("tokens.txt"):
    exit("未找到Tokens文件")

tokens = open("tokens.txt", "r").read().split("\n")
print("已加载Token数量：" + str(len(tokens)))

al = 0
zid = input("请输入作品ID : ")
if len(zid) == 0:
    exit("?")

review = input("请输入评论内容 : ")
if len(review) == 0:
    exit("review")

# review_json = json.dumps({"emoji_content": "", "content": review})
review_json = json.dumps({"emoji_content": "", "content": review})

def worker(q, zid):
    try:
        while not q.empty():
            mission = q.get()
            req = c.call_api(f"creation-tools/v1/works/{zid}/comment", review_json, mission)
            if not req.status_code == 201:
                print(f"请求失败 : {req.text}\n----------")
    except urllib3.exceptions.SSLError:
        exit()

q = queue.Queue()
print(f"\r正在请求，你先别急", end="")
for token in tokens:
    q.put(token)
worker_num = 1024
for _ in range(worker_num):
    threading.Thread(target=worker, args=(q, zid)).start()
