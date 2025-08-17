"""
====================
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
====================
Version: 1.1.3
====================
"""
import json
import logging
import os
from concurrent.futures import ThreadPoolExecutor

import coloredlogs
import pandas as pd
import requests
from fake_useragent import UserAgent
from openpyxl import Workbook
from openpyxl import load_workbook

coloredlogs.install(level='INFO', fmt='%(asctime)s - %(funcName)s: %(message)s')

"""POST方式调用API"""


def PostAPI(Path: str, PostData: dict, Token: str) -> requests.Response:
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


def PostWithoutTokenAPI(Path: str, PostData: dict) -> requests.Response:
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


"""使用POST方式调用EDUAPI"""


def PostEduAPI(Path: str, PostData: dict, Token: str) -> requests.Response:
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        'User-Agent': UserAgent().random,
        "authorization": f"Bearer {Token}"
    }
    return requests.post(url=f"https://eduzone.codemao.cn{Path}",
                         headers=headers,
                         json=PostData)


"""GET方式调用API"""


def GetAPI(Path: str, Token: str) -> requests.Response:
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


def CheckToken(Path: str) -> int:
    if not os.path.exists(Path):
        logging.error(f"找不到Token文件: {Path}")
        return 0
    else:
        with open(Path, "r", encoding="utf-8") as file:
            FileLine = len(file.readlines())
            file.close()
            return FileLine


"""登录并获取用户Token"""


def GetUserToken(Username: str, Password: str) -> str:
    response = PostWithoutTokenAPI(Path="/tiger/v3/web/accounts/login", PostData={'pid': '65edCTyg',
                                                                                  'identity': Username,
                                                                                  'password': Password})
    if response.status_code == 200:
        return str(json.loads(response.text).get("auth", {}).get("token"))
    else:
        logging.error(f"请求失败，状态码: {response.status_code}, 响应: {response.text[:50]}")
        return ""


"""签订友好协议"""


def SignatureUser(Path: str) -> bool:
    if not os.path.exists(Path):
        logging.error(f"找不到Token文件: {Path}")
        return False
    elif CheckToken(Path) == 0:
        logging.warning(f"可用的Token数为0")
        return False
    else:
        with open(Path, 'r') as file:
            TokenList = [line.strip() for line in file if line.strip()]
            f.close()

        def CallToAPI_Sign(Token: str) -> bool:
            try:
                response = PostAPI(Path="/nemo/v3/user/level/signature", PostData={}, Token=Token)

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
    elif CheckToken(Path) == 0:
        logging.warning(f"可用的Token数为0")
        return False
    else:
        with open(Path, 'r') as file:
            TokenList = [line.strip() for line in file if line.strip()]
            f.close()

        def CallToAPI_Follow(Token: str) -> bool:
            try:
                response = PostAPI(Path=f"/nemo/v2/user/{UserID}/follow", PostData={}, Token=Token)

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
    elif CheckToken(Path) == 0:
        logging.warning(f"可用的Token数为0")
        return False
    else:
        with open(Path, 'r') as file:
            TokenList = [line.strip() for line in file if line.strip()]
            f.close()

        def CallToAPI_Like(Token: str) -> bool:
            try:
                response = PostAPI(Path=f"/nemo/v2/works/{WorkID}/like", PostData={}, Token=Token)

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
    elif CheckToken(Path) == 0:
        logging.warning(f"可用的Token数为0")
        return False
    else:
        with open(Path, 'r') as file:
            TokenList = [line.strip() for line in file if line.strip()]
            f.close()

        def CallToAPI_Collection(Token: str) -> bool:
            try:
                response = PostAPI(Path=f"/nemo/v2/works/{WorkID}/collection", PostData={}, Token=Token)

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


"""举报作品"""


def ReportWork(Path: str, WorkID: str, Reason: str, Describe: str) -> bool:
    if not os.path.exists(Path):
        logging.error(f"找不到Token文件: {Path}")
        return False
    elif CheckToken(Path) == 0:
        logging.warning(f"可用的Token数为0")
        return False
    else:
        with open(Path, 'r') as file:
            TokenList = [line.strip() for line in file if line.strip()]
            f.close()

        def CallToAPI_ReportWork(Token: str) -> bool:
            try:
                response = PostAPI(Path=f"/nemo/v2/report/work", PostData={"work_id": WorkID,
                                                                           "report_reason": Reason,
                                                                           "report_describe": Describe},
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

        success_count = 0
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(CallToAPI_ReportWork, TokenList))
            success_count = sum(results)

        return True


"""回复作品"""


def SendReviewToWork(Path: str, WorkID: str, ReviewText: str) -> bool:
    if not os.path.exists(Path):
        logging.error(f"找不到Token文件: {Path}")
        return False
    elif CheckToken(Path) == 0:
        logging.warning(f"可用的Token数为0")
        return False
    else:
        with open(Path, 'r') as file:
            TokenList = [line.strip() for line in file if line.strip()]
            f.close()

        def CallToAPI_Review(Token: str) -> bool:
            try:
                response = PostAPI(Path=f"/creation-tools/v1/works/{WorkID}/comment", PostData={"emoji_content": "",
                                                                                                "content": ReviewText},
                                   Token=Token)

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
        response = GetAPI(f"/creation-tools/v1/works/{WorkID}", Token=Token)

        if response.status_code == 200:
            return True
        else:
            logging.error(
                f"请求失败，状态码: {response.status_code}, 响应: {response.text[:50]}")
            return False
    except Exception as e:
        logging.error(f"请求异常: {str(e)}")
        return False


"""添加新的班级"""


def CreateClassOnEdu(Token: str, ClassName: str) -> str:
    try:
        response = PostEduAPI(Path="/edu/zone/class",
                              PostData={"name": ClassName},
                              Token=Token)
        if response.status_code == 200:
            return str(json.loads(response.text).get("id"))
        else:
            logging.error(
                f"请求失败，状态码: {response.status_code}, 响应: {response.text[:50]}")
            return "0"
    except Exception as e:
        logging.error(f"请求异常: {str(e)}")
        return "0"


"""添加新的学生到班级"""


def CreateStudentOnEdu(Token: str, ClassID: str, StudentNameList: list[str]) -> bytes:
    try:
        response = PostEduAPI(Path=f"/edu/zone/class/{ClassID}/students",
                              PostData={"student_names": StudentNameList},
                              Token=Token)
        if response.status_code == 200:
            return response.content
        else:
            logging.error(
                f"请求失败，状态码: {response.status_code}, 响应: {response.text[:50]}")
            return None
    except Exception as e:
        logging.error(f"请求异常: {str(e)}")
        return None


"""合并生成的表格"""


def MergeStudentXls(InputFolder: str, OutputFile: str) -> bool:
    try:
        if os.path.exists(InputFolder):
            main = Workbook().active
            RowCount = 1
            for FileName in os.listdir(InputFolder):
                if FileName.endswith(".xlsx"):
                    FilePath = os.path.join(InputFolder, FileName)
                    Df = pd.read_excel(FilePath, skiprows=3)
                    for index, row in Df.iterrows():
                        main.append(row.tolist())
                        RowCount += 1
            OutPutFile = OutputFlile
            return True
        else:
            logging.error(f"找不到输入的文件夹: {InputFolder}")
            return False
    except Exception as e:
        logging.error(f"出现异常: {str(e)}")
        return False


"""登录Edu账号"""


def LoginUseEdu(InputXlsx: str, OutputFile: str) -> bool:
    CannotLogin = 0
    if os.path.exists(InputXlsx):
        Sheet = load_workbook(InputXlsx).active
        AllAccount = Sheet.max_row
        logging.info(f"登录账号共{AllAccount}个")
        for _ in range(AllAccount):
            try:
                UserList = []
                PasswordList = []
                for Row in Sheet.iter_rows(min_row=1, min_col=2, max_col=3, values_only=True):
                    User, Password = Row
                    UserList.append(user)
                    PasswordList.append(password)
                LoginReponse = GetUserToken(UserList[_], PasswordList[_])
                with open(OutputFile, 'a') as file:
                    file.write(token + "\n")
            except TypeError:
                CannotLogin += 1
                logging.error(
                    f"请求失败，状态码: {response.status_code}, 响应: {response.text[:50]}")
        logging.warning(f"未成功登录数量: {CannotLogin}，占比{CannotLogin / AllAccount}")
        return True
    else:
        logging.error(f"找不到输入的Xlsx文件: {InputXlsx}")
        return False


if __name__ == '__main__':
    pass
