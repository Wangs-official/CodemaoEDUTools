"""
API调用
"""

import logging

import requests
from fake_useragent import UserAgent

logger = logging.getLogger(__name__)


def PostAPI(Path: str, PostData: dict, Token: str) -> requests.Response:
    """POST方式调用API"""
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "User-Agent": UserAgent().random,
        "authorization": Token,
    }
    return requests.post(
        url=f"https://api.codemao.cn{Path}", headers=headers, json=PostData
    )


def PostWithoutTokenAPI(Path: str, PostData: dict) -> requests.Response:
    """POST方式匿名调用API"""
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "User-Agent": UserAgent().random,
    }
    return requests.post(
        url=f"https://api.codemao.cn{Path}", headers=headers, json=PostData
    )


def PostEduAPI(Path: str, PostData: dict, Token: str) -> requests.Response:
    """使用POST方式调用EDUAPI"""
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "User-Agent": UserAgent().random,
        "authorization": f"Bearer {Token}",
    }
    return requests.post(
        url=f"https://eduzone.codemao.cn{Path}", headers=headers, json=PostData
    )


def GetAPI(Path: str, Token: str) -> requests.Response:
    """GET方式调用API"""
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "User-Agent": UserAgent().random,
        "authorization": Token,
    }
    return requests.get(url=f"https://api.codemao.cn{Path}", headers=headers)


def GetWithoutTokenAPI(Path: str) -> requests.Response:
    """GET方式匿名调用API"""
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "User-Agent": UserAgent().random,
    }
    return requests.get(url=f"https://api.codemao.cn{Path}", headers=headers)


def PutAPI(Path: str, Token: str) -> requests.Response:
    """PUT方式调用API"""
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "User-Agent": UserAgent().random,
        "authorization": Token,
    }
    return requests.put(url=f"https://api.codemao.cn{Path}", headers=headers)

def DeleteAPI(Path: str, Token: str) -> requests.Response:
    """DELETE方式调用API"""
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "User-Agent": UserAgent().random,
        "authorization": Token,
    }
    return requests.delete(url=f"https://api.codemao.cn{Path}", headers=headers)