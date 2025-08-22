"""
====================
Author: WangZixu
欢迎使用 CodemaoEDUTools!
https://github.com/Wangs-official/CodemaoEDUTools/
====================
请阅读 doc/cli.md 中的命令行参数，或在你的程序中添加此库
import CodemaoEDUTools
====================
开发者不对您使用本项目造成的风险负责，请自行考虑是否使用，谢谢！
====================
请在开始使用前运行
pip3 install -r requirements.txt
====================
"""
import argparse
import json
import logging
import os
from concurrent.futures import ThreadPoolExecutor
from typing import Any

import coloredlogs
import pandas as pd
import requests
from fake_useragent import UserAgent
from openpyxl import Workbook
from openpyxl import load_workbook

coloredlogs.install(level='INFO', fmt='%(asctime)s - %(funcName)s: %(message)s')
version = "1.1.5_NT"
max_workers = 8

"""POST方式调用API"""


def PostAPI(Path: str, PostData: dict, Token: str) -> requests.Response:
    headers = {"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "zh-CN,zh;q=0.9",
               "Connection": "keep-alive", "Content-Type": "application/json", 'User-Agent': UserAgent().random,
               "authorization": Token}
    return requests.post(url=f"https://api.codemao.cn{Path}", headers=headers, json=PostData)


"""POST方式匿名调用API"""


def PostWithoutTokenAPI(Path: str, PostData: dict) -> requests.Response:
    headers = {"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "zh-CN,zh;q=0.9",
               "Connection": "keep-alive", "Content-Type": "application/json", 'User-Agent': UserAgent().random, }
    return requests.post(url=f"https://api.codemao.cn{Path}", headers=headers, json=PostData)


"""使用POST方式调用EDUAPI"""


def PostEduAPI(Path: str, PostData: dict, Token: str) -> requests.Response:
    headers = {"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "zh-CN,zh;q=0.9",
               "Connection": "keep-alive", "Content-Type": "application/json", 'User-Agent': UserAgent().random,
               "authorization": f"Bearer {Token}"}
    return requests.post(url=f"https://eduzone.codemao.cn{Path}", headers=headers, json=PostData)


"""GET方式调用API"""


def GetAPI(Path: str, Token: str) -> requests.Response:
    headers = {"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "zh-CN,zh;q=0.9",
               "Connection": "keep-alive", "Content-Type": "application/json", 'User-Agent': UserAgent().random,
               "authorization": Token}
    return requests.get(url=f"https://api.codemao.cn{Path}", headers=headers)


"""确定Token数量"""


def CheckToken(Path: str) -> int:
    if not os.path.exists(Path):
        logging.error(f"找不到Token文件: {Path}")
        return 0
    else:
        with open(Path, "r", encoding="utf-8") as f:
            FileLine = len(f.readlines())
            f.close()
            return FileLine


"""登录并获取用户Token"""


def GetUserToken(Username: str, Password: str) -> str | bool:
    response = PostWithoutTokenAPI(Path="/tiger/v3/web/accounts/login",
                                   PostData={'pid': '65edCTyg', 'identity': Username, 'password': Password})
    if response.status_code == 200:
        return str(json.loads(response.text).get("auth", {}).get("token"))
    else:
        logging.error(f"请求失败，状态码: {response.status_code}, 响应: {response.text[:100]}")
        return False


"""签订友好协议"""


def SignatureUser(Path: str) -> bool:
    if not os.path.exists(Path):
        logging.error(f"找不到Token文件: {Path}")
        return False
    elif CheckToken(Path) == 0:
        logging.warning(f"可用的Token数为0")
        return False
    else:
        with open(Path, 'r') as f:
            TokenList = [line.strip() for line in f if line.strip()]
            f.close()

        def CallToAPI_Sign(Token: str) -> bool:
            try:
                response = PostAPI(Path="/nemo/v3/user/level/signature", PostData={}, Token=Token)

                if response.status_code == 200:
                    return True
                else:
                    logging.error(f"请求失败，状态码: {response.status_code}, 响应: {response.text[:100]}")
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
        with open(Path, 'r') as f:
            TokenList = [line.strip() for line in f if line.strip()]
            f.close()

        def CallToAPI_Follow(Token: str) -> bool:
            try:
                response = PostAPI(Path=f"/nemo/v2/user/{UserID}/follow", PostData={}, Token=Token)

                if response.status_code == 204:
                    return True
                else:
                    logging.error(f"请求失败，状态码: {response.status_code}, 响应: {response.text[:100]}")
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
        with open(Path, 'r') as f:
            TokenList = [line.strip() for line in f if line.strip()]
            f.close()

        def CallToAPI_Like(Token: str) -> bool:
            try:
                response = PostAPI(Path=f"/nemo/v2/works/{WorkID}/like", PostData={}, Token=Token)

                if response.status_code == 200:
                    return True
                else:
                    logging.error(f"请求失败，状态码: {response.status_code}, 响应: {response.text[:100]}")
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
        with open(Path, 'r') as f:
            TokenList = [line.strip() for line in f if line.strip()]
            f.close()

        def CallToAPI_Collection(Token: str) -> bool:
            try:
                response = PostAPI(Path=f"/nemo/v2/works/{WorkID}/collection", PostData={}, Token=Token)

                if response.status_code == 200:
                    return True
                else:
                    logging.error(f"请求失败，状态码: {response.status_code}, 响应: {response.text[:100]}")
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
        with open(Path, 'r') as f:
            TokenList = [line.strip() for line in f if line.strip()]
            f.close()

        def CallToAPI_ReportWork(Token: str) -> bool:
            try:
                response = PostAPI(Path=f"/nemo/v2/report/work",
                                   PostData={"work_id": WorkID, "report_reason": Reason, "report_describe": Describe},
                                   Token=Token)

                if response.status_code == 200:
                    return True
                else:
                    logging.error(f"请求失败，状态码: {response.status_code}, 响应: {response.text[:100]}")
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
        with open(Path, 'r') as f:
            TokenList = [line.strip() for line in f if line.strip()]
            f.close()

        def CallToAPI_Review(Token: str) -> bool:
            try:
                response = PostAPI(Path=f"/creation-tools/v1/works/{WorkID}/comment",
                                   PostData={"emoji_content": "", "content": ReviewText}, Token=Token)

                if response.status_code == 201:
                    return True
                else:
                    logging.error(f"请求失败，状态码: {response.status_code}, 响应: {response.text[:100]}")
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
            logging.error(f"请求失败，状态码: {response.status_code}, 响应: {response.text[:100]}")
            return False
    except Exception as e:
        logging.error(f"请求异常: {str(e)}")
        return False


"""添加新的班级"""


def CreateClassOnEdu(Token: str, ClassName: str) -> str:
    try:
        response = PostEduAPI(Path="/edu/zone/class", PostData={"name": ClassName}, Token=Token)
        if response.status_code == 200:
            return str(json.loads(response.text).get("id"))
        else:
            logging.error(f"请求失败，状态码: {response.status_code}, 响应: {response.text[:100]}")
            return "0"
    except Exception as e:
        logging.error(f"请求异常: {str(e)}")
        return "0"


"""添加新的学生到班级"""


def CreateStudentOnEdu(Token: str, ClassID: str, StudentNameList: list[str]) -> bytes | None | Any:
    try:
        response = PostEduAPI(Path=f"/edu/zone/class/{ClassID}/students", PostData={"student_names": StudentNameList},
                              Token=Token)
        if response.status_code == 200:
            return response.content
        else:
            logging.error(f"请求失败，状态码: {response.status_code}, 响应: {response.text[:100]}")
            return None
    except Exception as e:
        logging.error(f"请求异常: {str(e)}")
        return None


"""合并生成的表格"""


def MergeStudentXls(InputFolder: str, OutputFile: str) -> bool:
    try:
        if os.path.exists(InputFolder):
            with open(OutputFile, "w") as f:
                f.close()
            main_wb = Workbook()
            main_ws = main_wb.active
            row_count = 1
            for filename in os.listdir(InputFolder):
                if filename.endswith('.xls'):
                    file_path = os.path.join(InputFolder, filename)
                    df = pd.read_excel(file_path, skiprows=3)
                    for index, row in df.iterrows():
                        main_ws.append(row.tolist())
                        row_count += 1
            output_file = OutputFile
            main_wb.save(output_file)
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
            UserList = []
            PasswordList = []
            for Row in Sheet.iter_rows(min_row=1, min_col=2, max_col=3, values_only=True):
                User, Password = Row
                UserList.append(User)
                PasswordList.append(Password)
            LoginReponse = GetUserToken(UserList[_], PasswordList[_])
            if not LoginReponse:
                CannotLogin += 1
            else:
                with open(OutputFile, 'a') as f:
                    file.write(LoginReponse + "\n")
        logging.warning(f"未成功登录数量: {CannotLogin}，占比{(CannotLogin / AllAccount) * 100}%")
        return True
    else:
        logging.error(f"找不到输入的Xlsx文件: {InputXlsx}")
        return False


"""参数处理器"""


def CreateParser():
    parser = argparse.ArgumentParser(description=f'欢迎使用 CodemaoEDUTools! 当前版本: v{version}',
                                     epilog='示例: python3 main.py check-token')

    global_group = parser.add_argument_group('全局参数')
    global_group.add_argument('-tf', '--token-file', help='Token文件路径', default='tokens.txt')

    subparsers = parser.add_subparsers(dest='command', help='可用命令')

    # Check_TokenFile(Path: str)
    check_tokenfile_parser = subparsers.add_parser('check-token', help='查看一个Token文件内，有多少个Token（读取行数）')

    # GetUserToken(Username: str, Password: str)
    getusertoken_parser = subparsers.add_parser('get-token', help='登录以获取一个用户的Token')

    getusertoken_parser.add_argument('-u', '--username', required=True, help='用户名（手机号）')

    getusertoken_parser.add_argument('-p', '--password', required=True, help='密码')

    # SignatureUser(Path: str)
    signature_parser = subparsers.add_parser('signature',
                                             help='签订友好协议，推荐在使用其他功能前统一签订一次友好协议，防止出现无法请求的情况')

    # FollowUser(Path: str, UserID: str)
    followuser_parser = subparsers.add_parser('follow-user', help='批量关注一个用户，高情商就是刷粉丝')

    followuser_parser.add_argument('-uid', '--user-id', required=True, help='训练师编号')

    # LikeWork(Path: str, WorkID: str)
    likework_parser = subparsers.add_parser('like-work', help='批量点赞一个作品')

    likework_parser.add_argument('-wid', '--work-id', required=True, help='作品ID')

    # CollectionWork(Path: str, WorkID: str)
    collectwork_parser = subparsers.add_parser('collect-work', help='批量收藏一个作品')

    collectwork_parser.add_argument('-wid', '--work-id', required=True, help='作品ID')

    # ReportWork(Path: str, WorkID: str, Reason: str, Describe: str)
    reportwork_parser = subparsers.add_parser('report-work', help='批量举报一个作品，请勿大量Token举报')

    reportwork_parser.add_argument('-wid', '--work-id', required=True, help='作品ID')

    reportwork_parser.add_argument('-r', '--report-reason', required=True, help='原因，请参考文档给出的可用方式')

    reportwork_parser.add_argument('-d', '--report-describe', required=True, help='举报理由')

    # SendReviewToWork(Path: str, WorkID: str, ReviewText: str)
    sendrevietowork_parser = subparsers.add_parser('review-work', help='在一个作品下，批量发送同样的评论')

    sendrevietowork_parser.add_argument('-wid', '--work-id', required=True, help='作品ID')

    sendrevietowork_parser.add_argument('-r', '--review-text', required=True, help='评论内容')

    # ViewWork(Token: str, WorkID: str)
    viewwork_parser = subparsers.add_parser('view-work',
                                            help='给作品加一个浏览，如果要一直刷，只需要循环这个函数就可以，一个Token就够')

    viewwork_parser.add_argument('-t', '--one-token', required=True, help='一个可用Token')

    viewwork_parser.add_argument('-wid', '--work-id', required=True, help='作品ID')

    # CreateClassOnEdu(Token: str, ClassName: str)
    createclassedu_parser = subparsers.add_parser('create-class', help='在Edu里添加一个新的班级')

    createclassedu_parser.add_argument('-t', '--token', required=True, help='Edu Token')

    createclassedu_parser.add_argument('-cn', '--class-name', required=True, help='班级名称，遵循官方命名规则')

    # CreateStudentOnEdu(Token: str, ClassID: str, StudentNameList: list[str])
    createstudentedu_parser = subparsers.add_parser('create-student', help='批量把创建新的学生并添加到班级内')

    createstudentedu_parser.add_argument('-t', '--token', required=True, help='Edu Token')

    createstudentedu_parser.add_argument('-cid', '--class-id', required=True, help='班级ID')

    createstudentedu_parser.add_argument('-sl', '--student-name-list', required=True,
                                         type=json.loads, help='学生名字的列表，最多100个学生，学生命名遵循官方命名规则')

    createstudentedu_parser.add_argument('-o', '--output-xls', required=True, help='输出文件名，需要填写.xls后缀')

    # MergeStudentXls(InputFolder: str, OutputFile:str)
    mergestudentxls_parser = subparsers.add_parser('merge-xls', help='如果要合成为一个xlsx文件用于登录，请使用此函数')

    mergestudentxls_parser.add_argument('-if', '--input-xls-folder', required=True, help='含有多个.xls文件的文件夹')

    mergestudentxls_parser.add_argument('-o', '--output-xlsx', required=True, help='输出文件名，需要填写.xlsx后缀')

    # LoginUseEdu(InputXlsx:str, OutputFile:str)
    loginedu_parser = subparsers.add_parser('login-edu',
                                            help='批量登录所有在xlsx内保存的账号密码，并打印Token到指定的文件内')

    loginedu_parser.add_argument('-i', '--input-xlsx', required=True, help='含有账号密码的xlsx表格文件的路径')

    loginedu_parser.add_argument('-o', '--output-txt', required=True, help='输出文件名，需要填写.txt后缀')

    # Version
    getversion_parser = subparsers.add_parser('version', help='获取CET版本')

    # End

    return parser


if __name__ == '__main__':
    print('Welcome to CET')

    parser = CreateParser()
    args = parser.parse_args()

    # 处理
    if args.command == 'check-token':
        logging.info(f'可用Token数量: {CheckToken(args.token_file)}')

    if args.command == 'get-token':
        logging.info(GetUserToken(args.username, args.password))

    if args.command == 'signature':
        logging.info('请稍后...')
        if SignatureUser(args.token_file):
            logging.info('执行成功')

    if args.command == 'follow-user':
        logging.info('请稍后...')
        if FollowUser(args.token_file, args.user_id):
            logging.info('执行成功')

    if args.command == 'like-work':
        logging.info('请稍后...')
        if LikeWork(args.token_file, args.work_id):
            logging.info('执行成功')

    if args.command == 'collect-work':
        logging.info('请稍后...')
        if CollectionWork(args.token_file, args.work_id):
            logging.info('执行成功')

    if args.command == 'report-work':
        logging.info('请稍后...')
        if ReportWork(args.token_file, args.work_id, args.report_reason, args.report_describe):
            logging.info('执行成功')

    if args.command == 'review-work':
        logging.info('请稍后...')
        if SendReviewToWork(args.token_file, args.work_id, args.review_text):
            logging.info('执行成功')

    if args.command == 'view-work':
        logging.info('请稍后...')
        if ViewWork(args.one_token, args.work_id):
            logging.info('执行成功')

    if args.command == 'create-class':
        logging.info('请稍后...')
        logging.info(f'Class ID: {CreateClassOnEdu(args.token, args.class_name)}')

    if args.command == 'create-student':
        logging.info('请稍后...')
        try:
            with open(args.output_xls, "wb") as f:
                f.write(CreateStudentOnEdu(args.token, args.class_id, args.student_name_list))
                f.close()
            logging.info(f'执行成功，学生密码表已保存到: {args.output_xls}')
        except TypeError:
            os.remove(args.output_xls)
            exit()

    if args.command == 'merge-xls':
        logging.info('请稍后...')
        if MergeStudentXls(args.input_xls_folder, args.output_xlsx):
            logging.info(f'执行成功，合并的文件已保存到：{args.output_xlsx}')

    if args.command == 'login-edu':
        logging.info('请稍后...')
        if LoginUseEdu(args.input_xlsx, args.output_txt):
            logging.info(f'执行成功，已将登录的Token保存到：{args.output_txt}')

    if args.command == 'version':
        logging.info(f'CET版本: v{version}\nhttps://github.com/Wangs-official/CodemaoEDUTools/')
