"""
作品
"""

import json
import logging
import os
from concurrent.futures import ThreadPoolExecutor

from .api import PostAPI, GetWithoutTokenAPI, PutAPI, GetAPI, DeleteAPI
from .user import CheckToken


from CodemaoEDUTools import max_workers, report_readtoken_line

logger = logging.getLogger(__name__)


def GetUserWork(UserID: str) -> str | bool:
    """获取用户所有的作品"""
    response = GetWithoutTokenAPI(
        f"/creation-tools/v2/user/center/work-list?type=newest&user_id={UserID}&offset=0&limit=1000"
    )
    if response.status_code == 200:
        ids = [str(item["id"]) for item in json.loads(response.text)["items"]]
        return " ".join(ids)
    else:
        logger.error(
            f"请求失败，状态码: {response.status_code}, 响应: {response.text[:100]}"
        )
        return False


def LikeWork(Path: str, WorkID: str) -> bool:
    """点赞作品"""
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

        def CallToAPI_Like(Token: str) -> bool:
            try:
                response = PostAPI(
                    Path=f"/nemo/v2/works/{WorkID}/like", PostData={}, Token=Token
                )
                return response.status_code == 200
            except Exception as e:
                logger.error(f"请求异常: {str(e)}")
                return False

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(CallToAPI_Like, TokenList))

        return all(results)


def CollectionWork(Path: str, WorkID: str) -> bool:
    """收藏作品"""
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

        def CallToAPI_Collection(Token: str) -> bool:
            try:
                response = PostAPI(
                    Path=f"/nemo/v2/works/{WorkID}/collection", PostData={}, Token=Token
                )
                return response.status_code == 200
            except Exception as e:
                logger.error(f"请求异常: {str(e)}")
                return False

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(CallToAPI_Collection, TokenList))

        return all(results)


def ReportWork(Path: str, WorkID: str, Reason: str, Describe: str) -> bool:
    """举报作品"""
    if not os.path.exists(Path):
        logger.error(f"找不到Token文件: {Path}")
        return False
    elif CheckToken(Path) == 0:
        logger.warning("可用的Token数为0")
        return False
    else:
        with open(Path, "r") as f:
            TokenList = []
            for i in range(report_readtoken_line):
                line = f.readline()
                if not line:
                    break
                line = line.strip()
                if line:
                    TokenList.append(line)
            f.close()

        def CallToAPI_ReportWork(Token: str) -> bool:
            try:
                response = PostAPI(
                    Path="/nemo/v2/report/work",
                    PostData={
                        "work_id": WorkID,
                        "report_reason": Reason,
                        "report_describe": Describe,
                    },
                    Token=Token,
                )
                return response.status_code == 200
            except Exception as e:
                logger.error(f"请求异常: {str(e)}")
                return False

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(CallToAPI_ReportWork, TokenList))

        return all(results)


def SendReviewToWork(Path: str, WorkID: str, ReviewText: str) -> bool:
    """回复作品"""
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

        def CallToAPI_Review(Token: str) -> bool:
            try:
                response = PostAPI(
                    Path=f"/creation-tools/v1/works/{WorkID}/comment",
                    PostData={"emoji_content": "", "content": ReviewText},
                    Token=Token,
                )
                return response.status_code == 201
            except Exception as e:
                logger.error(f"请求异常: {str(e)}")
                return False

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(CallToAPI_Review, TokenList))

        return all(results)


def TopReview(Token: str, WorkID: str, CommentID: str) -> bool:
    """置顶评论（越权）"""
    try:
        response = PutAPI(
            f"/creation-tools/v1/works/{WorkID}/comment/{CommentID}/top", Token=Token
        )
        return response.status_code == 204
    except Exception as e:
        logger.error(f"请求异常：{str(e)}")
        return False

def UnTopReview(Token: str, WorkID: str, CommentID: str) -> bool:
    """取消置顶评论（越权）"""
    try:
        response = DeleteAPI(
            f"/creation-tools/v1/works/{WorkID}/comment/{CommentID}/top", Token=Token
        )
        return response.status_code == 204
    except Exception as e:
        logger.error(f"请求异常：{str(e)}")
        return False


def ViewWork(Token: str, WorkID: str) -> bool:
    """浏览作品"""
    try:
        response = GetAPI(f"/creation-tools/v1/works/{WorkID}", Token=Token)
        return response.status_code == 200
    except Exception as e:
        logger.error(f"请求异常: {str(e)}")
        return False


def ForkWork(Path: str, WorkID: str) -> bool:
    """再创作作品"""
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

        def CallToAPI_Fork(Token: str) -> bool:
            try:
                response = PostAPI(
                    Path=f"/nemo/v2/works/{WorkID}/fork",
                    PostData={},
                    Token=Token,
                )
                return response.status_code == 200
            except Exception as e:
                logger.error(f"请求异常: {str(e)}")
                return False

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(CallToAPI_Fork, TokenList))

        return all(results)
