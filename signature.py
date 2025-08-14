# @author:Wangs_official
# 先过签订友好协议再进行批量评论什么的
import os
import queue
import threading
import time

import control as c


def worker(q):
    while not q.empty():
        mission = q.get()
        req = c.call_api("nemo/v3/user/level/signature", "{}", mission)
        if not req.status_code == 200:
            print(f"请求失败 : {req.text}\n----------")


if not os.path.exists("tokens.txt"):
    exit("未找到Tokens文件")

tokens = open("tokens.txt", "r").read().split("\n")
print("已加载Token数量：" + str(len(tokens)))

q = queue.Queue()
print(f"\r正在请求，你先别急", end="")
for token in tokens:
    q.put(token)
worker_num = 8
for _ in range(worker_num):
    threading.Thread(target=worker, args=(q,)).start()
