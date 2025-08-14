# @author:Wangs_official
import os
import queue
import threading
import time

import control as c

if not os.path.exists("tokens.txt"):
    exit("未找到Tokens文件")

tokens = open("tokens.txt", "r").read().split("\n")
print("已加载Token数量：" + str(len(tokens)))

uid = input("请输入要关注的UID : ")
if len(uid) == 0:
    exit("?")


def worker(q, uid):
    while not q.empty():
        mission = q.get()
        req = c.call_api(f"nemo/v2/user/{uid}/follow", "{}", mission)
        if not req.status_code == 204:
            print(f"请求失败 : {req.text}\n----------")


q = queue.Queue()
print(f"\r正在请求，你先别急", end="")
for token in tokens:
    q.put(token)
worker_num = 8
for _ in range(worker_num):
    threading.Thread(target=worker, args=(q, uid)).start()

print("\r请求完毕", end="")
