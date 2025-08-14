# @author:Wangs_official
import os
import queue
import threading
import time
import requests

al = 0
zid = input("请输入作品ID : ")
if len(zid) == 0:
    exit("?")
Token = input("请输入一个Token : ")
if len(Token) == 0:
    exit("?")
print("刷够了就关上吧")

while 1:
    view = requests.get(f"https://api.codemao.cn/creation-tools/v1/works/{zid}",
                        headers={"Authorization": f"{Token}"})
    view2 = requests.get(f"https://api.codemao.cn/creation-tools/v1/works/{zid}",
                        headers={"Authorization": f"{Token}"})
    view3 = requests.get(f"https://api.codemao.cn/creation-tools/v1/works/{zid}",
                        headers={"Authorization": f"{Token}"})
    view4 = requests.get(f"https://api.codemao.cn/creation-tools/v1/works/{zid}",
                            headers={"Authorization": f"{Token}"})
    view5 = requests.get(f"https://api.codemao.cn/creation-tools/v1/works/{zid}",
                         headers={"Authorization": f"{Token}"})
    view6 = requests.get(f"https://api.codemao.cn/creation-tools/v1/works/{zid}",
                         headers={"Authorization": f"{Token}"})
    view7 = requests.get(f"https://api.codemao.cn/creation-tools/v1/works/{zid}",
                         headers={"Authorization": f"{Token}"})
    view8 = requests.get(f"https://api.codemao.cn/creation-tools/v1/works/{zid}",
                         headers={"Authorization": f"{Token}"})
    view8 = requests.get(f"https://api.codemao.cn/creation-tools/v1/works/{zid}",
                         headers={"Authorization": f"{Token}"})
    view9 = requests.get(f"https://api.codemao.cn/creation-tools/v1/works/{zid}",
                         headers={"Authorization": f"{Token}"})
    view10 = requests.get(f"https://api.codemao.cn/creation-tools/v1/works/{zid}",
                         headers={"Authorization": f"{Token}"})