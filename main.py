"""
Author: WangZixu
欢迎使用 CodemaoEDUTools!
https://github.com/Wangs-official/CodemaoEDUTools/
====================
请阅读 README.md 中的命令行参数，或在你的程序中添加此库
import CodemaoEDUTools
====================
开发者不对您使用本项目造成的风险负责，请自行考虑是否使用，谢谢！
====================
请在开始使用前运行
pip3 install -r requirements.txt
"""
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent
from typing import Optional
import coloredlogs
import argparse
import requests
import logging
import certifi
import random
import time
import json
import os

coloredlogs.install(level='INFO', fmt='%(asctime)s - %(funcName)s: %(message)s')

"""POST方式调用API"""


def API_Post(Path: str, PostData: dict, Token: str) -> requests.Response:
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        'User-Agent': UserAgent().random,
        "authorization": Token
    }
    return requests.post(url=f"https://api.codemao.cn{Path}",
                         headers=headers,
                         json=PostData)


"""POST方式匿名调用API"""


def API_Post_WithoutToken(Path: str, PostData: dict) -> requests.Response:
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        'User-Agent': UserAgent().random,
    }
    logging.error(f"https://api.codemao.cn{Path}", )
    return requests.post(url=f"https://api.codemao.cn{Path}",
                         headers=headers,
                         json=PostData)


"""GET方式调用API"""


def API_Get(Path: str, Token: str) -> requests.Response:
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        'User-Agent': UserAgent().random,
        "authorization": Token
    }
    return requests.get(url=f"https://api.codemao.cn{Path}",
                        headers=headers)


"""确定Token数量"""


def Check_TokenFile(Path: str) -> Optional[int]:
    if not os.path.exists(Path):
        logging.error(f"找不到Token文件: {Path}")
        return 0
    else:
        with open(Path, "r", encoding="utf-8") as file:
            FileLine = len(file.readlines())
            file.close()
            return FileLine


"""登录并获取用户Token"""


def GetMyToken(Username: str, Password: str) -> str:
    response = API_Post_WithoutToken(Path="/tiger/v3/web/accounts/login",
                                     PostData={'pid': '65edCTyg',
                                               'identity': Username,
                                               'password': Password})
    if response.status_code == 200:
        return str(json.loads(response.text).get("auth", {}).get("token"))
    else:
        logging.error(f"请求失败，状态码: {response.status_code}, 响应: {response.text[:50]}")
        return ""


"""签订友好协议"""


def Signature(Path: str) -> bool:
    if not os.path.exists(Path):
        logging.error(f"找不到Token文件: {Path}")
        return False
    elif Check_TokenFile(Path, False) == 0:
        logging.warning(f"可用的Token数为0")
        return False
    else:
        with open(Path, 'r') as file:
            TokenList = [line.strip() for line in file if line.strip()]
            f.close()

        def CallToAPI_Sign(Token: str) -> bool:
            try:
                response = API_Post(
                    Path="/nemo/v3/user/level/signature",
                    PostData={},
                    Token=Token
                )

                if response.status_code == 200:
                    return True
                else:
                    logging.error(
                        f"请求失败，状态码: {response.status_code}, 响应: {response.text[:50]}")
                    return False
            except Exception as e:
                logging.error(f"请求异常: {str(e)}")
                return False

        success_count = 0
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(CallToAPI_Sign, TokenList))
            success_count = sum(results)

        return True


"""关注用户"""


def FollowUser(Path: str, UserID: str) -> bool:
    if not os.path.exists(Path):
        logging.error(f"找不到Token文件: {Path}")
        return False
    elif Check_TokenFile(Path, False) == 0:
        logging.warning(f"可用的Token数为0")
        return False
    else:
        with open(Path, 'r') as file:
            TokenList = [line.strip() for line in file if line.strip()]
            f.close()

        def CallToAPI_Follow(Token: str) -> bool:
            try:
                response = API_Post(
                    Path=f"/nemo/v2/user/{UserID}/follow",
                    PostData={},
                    Token=Token
                )

                if response.status_code == 204:
                    return True
                else:
                    logging.error(
                        f"请求失败，状态码: {response.status_code}, 响应: {response.text[:50]}")
                    return False
            except Exception as e:
                logging.error(f"请求异常: {str(e)}")
                return False

        success_count = 0
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(CallToAPI_Follow, TokenList))
            success_count = sum(results)

        return True


"""点赞作品"""


def LikeWork(Path: str, WorkID: str) -> bool:
    if not os.path.exists(Path):
        logging.error(f"找不到Token文件: {Path}")
        return False
    elif Check_TokenFile(Path) == 0:
        logging.warning(f"可用的Token数为0")
        return False
    else:
        with open(Path, 'r') as file:
            TokenList = [line.strip() for line in file if line.strip()]
            f.close()

        def CallToAPI_Like(Token: str) -> bool:
            try:
                response = API_Post(
                    Path=f"/nemo/v2/works/{WorkID}/like",
                    PostData={},
                    Token=Token
                )

                if response.status_code == 200:
                    return True
                else:
                    logging.error(
                        f"请求失败，状态码: {response.status_code}, 响应: {response.text[:50]}")
                    return False
            except Exception as e:
                logging.error(f"请求异常: {str(e)}")
                return False

        success_count = 0
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(CallToAPI_Like, TokenList))
            success_count = sum(results)

        return True


"""收藏作品"""


def CollectionWork(Path: str, WorkID: str) -> bool:
    if not os.path.exists(Path):
        logging.error(f"找不到Token文件: {Path}")
        return False
    elif Check_TokenFile(Path) == 0:
        logging.warning(f"可用的Token数为0")
        return False
    else:
        with open(Path, 'r') as file:
            TokenList = [line.strip() for line in file if line.strip()]
            f.close()

        def CallToAPI_Collection(Token: str) -> bool:
            try:
                response = API_Post(
                    Path=f"/nemo/v2/works/{WorkID}/collection",
                    PostData={},
                    Token=Token
                )

                if response.status_code == 200:
                    return True
                else:
                    logging.error(
                        f"请求失败，状态码: {response.status_code}, 响应: {response.text[:50]}")
                    return False
            except Exception as e:
                logging.error(f"请求异常: {str(e)}")
                return False

        success_count = 0
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(CallToAPI_Collection, TokenList))
            success_count = sum(results)

        return True


"""批量举报作品"""


def ReportWork(Path: str, WorkID: str) -> bool:
    if not os.path.exists(Path):
        logging.error(f"找不到Token文件: {Path}")
        return False
    elif Check_TokenFile(Path) == 0:
        logging.warning(f"可用的Token数为0")
        return False
    else:
        with open(Path, 'r') as file:
            TokenList = [line.strip() for line in file if line.strip()]
            f.close()

        def CallToAPI_ReportWork(Token: str) -> bool:
            try:
                response = API_Post(
                    Path=f"/nemo/v2/report/work",
                    PostData={"work_id": WorkID,
                              "report_reason": "违法违规",
                              "report_describe": "作品有问题"},
                    Token=Token
                )

                if response.status_code == 200:
                    return True
                else:
                    logging.error(
                        f"请求失败，状态码: {response.status_code}, 响应: {response.text[:50]}")
                    return False
            except Exception as e:
                logging.error(f"请求异常: {str(e)}")
                return False

        success_count = 0
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(CallToAPI_ReportWork, TokenList))
            success_count = sum(results)

        return True


"""批量在作品下发送回复"""


def SendReview(Path: str, ReviewText: str, WorkID: str) -> bool:
    if not os.path.exists(Path):
        logging.error(f"找不到Token文件: {Path}")
        return False
    elif Check_TokenFile(Path) == 0:
        logging.warning(f"可用的Token数为0")
        return False
    else:
        with open(Path, 'r') as file:
            TokenList = [line.strip() for line in file if line.strip()]
            f.close()

        def CallToAPI_Review(Token: str) -> bool:
            try:
                response = API_Post(
                    Path=f"/creation-tools/v1/works/{WorkID}/comment",
                    PostData={"emoji_content": "",
                              "content": ReviewText},
                    Token=Token
                )

                if response.status_code == 201:
                    return True
                else:
                    logging.error(
                        f"请求失败，状态码: {response.status_code}, 响应: {response.text[:50]}")
                    return False
            except Exception as e:
                logging.error(f"请求异常: {str(e)}")
                return False

        success_count = 0
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(CallToAPI_Review, TokenList))
            success_count = sum(results)

        return True


"""浏览作品"""


def ViewWork(Token: str, WorkID: str) -> bool:
    try:
        response = API_Get(f"/creation-tools/v1/works/{WorkID}",
                           Token=Token)

        if response.status_code == 200:
            return True
        else:
            logging.error(
                f"请求失败，状态码: {response.status_code}, 响应: {response.text[:50]}")
            return False
    except Exception as e:
        logging.error(f"请求异常: {str(e)}")
        return False


if __name__ == '__main__':
    pass
