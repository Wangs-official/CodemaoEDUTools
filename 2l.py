# @author:Wangs_official
import os
import queue
import threading
import time
import requests

import control as c

if not os.path.exists("tokens.txt"):
    exit("未找到Tokens文件")

tokens = open("tokens.txt", "r").read().split("\n")
print("已加载Token数量：" + str(len(tokens)))

al = 0
zid = input("请输入作品ID : ")
if len(zid) == 0:
    exit("?")


def worker(q, zid):
    while not q.empty():
        mission = q.get()
        while 1:
            for _ in range(10):
                view = requests.get(f"https://api.codemao.cn/creation-tools/v1/works/{zid}", headers={"Authorization": mission})
            break
        req = c.call_api(f"nemo/v2/works/{zid}/collection", "{}", mission)
        req2 = c.call_api(f"nemo/v2/works/{zid}/like", "{}", mission)
        if not req.status_code == 200:
            print(f"   (点赞)请求失败 : {req.text}\n----------")
        if not req2.status_code == 200:
            print(f"   (收藏)请求失败 : {req2.text}\n----------")


q = queue.Queue()
print(f"\r正在请求，你先别急", end="")
for token in tokens:
    q.put(token)
worker_num = 8
for _ in range(worker_num):
    threading.Thread(target=worker, args=(q, zid)).start()
