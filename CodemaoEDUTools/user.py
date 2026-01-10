"""
用户
"""

import json
import logging
import os
from concurrent.futures import ThreadPoolExecutor
from typing import Any

from .api import PostAPI, PostWithoutTokenAPI

from CodemaoEDUTools import max_workers, report_readtoken_line

logger = logging.getLogger(__name__)


def GetUserToken(Username: str, Password: str) -> str | bool:
    """登录并获取用户Token"""
    response = PostWithoutTokenAPI(
        Path="/tiger/v3/web/accounts/login",
        PostData={"pid": "65edCTyg", "identity": Username, "password": Password},
    )
    if response.status_code == 200:
        return str(json.loads(response.text).get("auth", {}).get("token"))
    else:
        logger.error(
            f"请求失败，用户名：{Username}, 状态码: {response.status_code}, 响应: {response.text[:100]}"
        )
        return False


def CheckToken(Path: str) -> int:
    """确定Token数量"""
    if not os.path.exists(Path):
        logger.error(f"找不到Token文件: {Path}")
        return 0
    else:
        with open(Path, "r", encoding="utf-8") as f:
            FileLine = len(f.readlines())
            f.close()
            return FileLine


def SignatureUser(Path: str) -> bool:
    """签订友好协议"""
    if not os.path.exists(Path):
        logger.error(f"找不到Token文件: {Path}")
        return False
    elif CheckToken(Path) == 0:
        logger.warning("可用的Token数为0")
        return False
    else:
        with open(Path, "r") as f:
            TokenList = [line.strip() for line in f if line.strip()]
            f.close()

        def CallToAPI_Sign(Token: str) -> bool:
            try:
                response = PostAPI(
                    Path="/nemo/v3/user/level/signature", PostData={}, Token=Token
                )
                return response.status_code == 200
            except Exception as e:
                logger.error(f"请求异常: {str(e)}")
                return False

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(CallToAPI_Sign, TokenList))

        return all(results)


def FollowUser(Path: str, UserID: str) -> bool:
    """关注用户"""
    if not os.path.exists(Path):
        logger.error(f"找不到Token文件: {Path}")
        return False
    elif CheckToken(Path) == 0:
        logger.warning("可用的Token数为0")
        return False
    else:
        with open(Path, "r") as f:
            TokenList = [line.strip() for line in f if line.strip()]
            f.close()

        def CallToAPI_Follow(Token: str) -> bool:
            try:
                response = PostAPI(
                    Path=f"/nemo/v2/user/{UserID}/follow", PostData={}, Token=Token
                )
                return response.status_code == 204
            except Exception as e:
                logger.error(f"请求异常: {str(e)}")
                return False

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(CallToAPI_Follow, TokenList))

        return all(results)
