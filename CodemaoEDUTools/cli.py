"""
命令行解析器
"""

import argparse
import json

from . import __version__, student_names


def CreateParser():
    parser = argparse.ArgumentParser(
        description=f"欢迎使用 CodemaoEDUTools! 当前版本: v{__version__}",
        epilog="示例: python -m CodemaoEDUTools check-token",
    )

    global_group = parser.add_argument_group("全局参数")
    global_group.add_argument(
        "-tf", "--token-file", help="Token文件路径", default="tokens.txt"
    )

    subparsers = parser.add_subparsers(dest="command", help="可用命令")

    # Check_TokenFile(Path: str)
    subparsers.add_parser(
        "check-token", help="查看一个Token文件内，有多少个Token（读取行数）"
    )

    # GetUserToken(Username: str, Password: str)
    getusertoken_parser = subparsers.add_parser(
        "get-token", help="登录以获取一个用户的Token"
    )
    getusertoken_parser.add_argument(
        "-u", "--username", required=True, help="用户名（手机号）"
    )
    getusertoken_parser.add_argument("-p", "--password", required=True, help="密码")

    # SignatureUser(Path: str)
    subparsers.add_parser("signature", help="签订友好协议")

    # FollowUser(Path: str, UserID: str)
    followuser_parser = subparsers.add_parser("follow-user", help="批量关注一个用户")
    followuser_parser.add_argument(
        "-uid", "--user-id", required=True, nargs="+", help="训练师编号"
    )

    # GetUserWork(UserID: str)
    getuserwork_parser = subparsers.add_parser("get-work", help="获取用户所有作品ID")
    getuserwork_parser.add_argument(
        "-uid", "--user-id", required=True, nargs="+", help="训练师编号"
    )

    # LikeWork(Path: str, WorkID: str)
    likework_parser = subparsers.add_parser("like-work", help="批量点赞一个作品")
    likework_parser.add_argument(
        "-wid", "--work-id", nargs="+", required=True, help="作品ID"
    )

    # CollectionWork(Path: str, WorkID: str)
    collectwork_parser = subparsers.add_parser("collect-work", help="批量收藏一个作品")
    collectwork_parser.add_argument(
        "-wid", "--work-id", nargs="+", required=True, help="作品ID"
    )

    # ReportWork(Path: str, WorkID: str, Reason: str, Describe: str)
    reportwork_parser = subparsers.add_parser("report-work", help="批量举报一个作品")
    reportwork_parser.add_argument(
        "-wid", "--work-id", nargs="+", required=True, help="作品ID"
    )
    reportwork_parser.add_argument("-r", "--report-reason", required=True, help="原因")
    reportwork_parser.add_argument(
        "-d", "--report-describe", required=True, help="举报理由"
    )

    # SendReviewToWork(Path: str, WorkID: str, ReviewText: str)
    sendreview_parser = subparsers.add_parser(
        "review-work", help="在一个作品下，批量发送同样的评论"
    )
    sendreview_parser.add_argument(
        "-wid", "--work-id", required=True, nargs="+", help="作品ID"
    )
    sendreview_parser.add_argument(
        "-r", "--review-text", required=True, nargs="+", help="评论内容"
    )

    # TopReview(Token: str, WorkID: str, CommentID: str)
    topreview_parser = subparsers.add_parser("review-top", help="越权置顶某个评论")
    topreview_parser.add_argument(
        "-t", "--one-token", required=True, help="一个可用Token"
    )
    topreview_parser.add_argument("-wid", "--work-id", required=True, help="作品ID")
    topreview_parser.add_argument("-cid", "--comment-id", required=True, help="评论ID")

    # UnTopReview(Token: str, WorkID: str, CommentID: str)
    untopreview_parser = subparsers.add_parser("review-untop", help="越权取消置顶某个评论")
    untopreview_parser.add_argument(
        "-t", "--one-token", required=True, help="一个可用Token"
    )
    untopreview_parser.add_argument("-wid", "--work-id", required=True, help="作品ID")
    untopreview_parser.add_argument("-cid", "--comment-id", required=True, help="评论ID")

    # ViewWork(Token: str, WorkID: str)
    viewwork_parser = subparsers.add_parser("view-work", help="给作品加一个浏览")
    viewwork_parser.add_argument(
        "-t", "--one-token", required=True, help="一个可用Token"
    )
    viewwork_parser.add_argument("-wid", "--work-id", required=True, help="作品ID")

    # ForkWork(Path: str, WorkID: str)
    forkwork_parser = subparsers.add_parser("fork-work", help="再创作一个作品")
    forkwork_parser.add_argument(
        "-wid", "--work-id", required=True, nargs="+", help="作品ID"
    )

    # CreateClassOnEdu(Token: str, ClassName: str)
    createclass_parser = subparsers.add_parser(
        "create-class", help="在Edu里添加一个新的班级"
    )
    createclass_parser.add_argument("-t", "--token", required=True, help="Edu Token")
    createclass_parser.add_argument(
        "-cn", "--class-name", required=True, help="班级名称"
    )

    # CreateStudentOnEdu(Token: str, ClassID: str, StudentNameList: list[str])
    createstudent_parser = subparsers.add_parser(
        "create-student", help="批量创建新的学生并添加到班级"
    )
    createstudent_parser.add_argument("-t", "--token", required=True, help="Edu Token")
    createstudent_parser.add_argument(
        "-cid", "--class-id", required=True, help="班级ID"
    )
    createstudent_parser.add_argument(
        "-sl",
        "--student-name-list",
        required=False,
        default=json.dumps(student_names),
        help="学生名字列表，JSON格式",
    )

    # MergeStudentXls(InputFolder: str, OutputFile:str)
    merge_parser = subparsers.add_parser(
        "merge-xls", help="合并多个xls文件为一个xlsx文件"
    )
    merge_parser.add_argument(
        "-if", "--input-xls-folder", required=True, help="含有多个.xls文件的文件夹"
    )
    merge_parser.add_argument(
        "-o", "--output-xlsx", default="output.xlsx", help="输出文件名"
    )

    # LoginUseEdu(InputXlsx:str, OutputFile:str)
    login_parser = subparsers.add_parser("login-edu", help="批量登录xlsx内的账号")
    login_parser.add_argument(
        "-i", "--input-xlsx", required=True, help="含有账号密码的xlsx文件路径"
    )
    login_parser.add_argument(
        "-s", "--signature-user", action="store_true", help="是否同时签署友好协议"
    )
    login_parser.add_argument(
        "-o", "--output-txt", default="tokens.txt", help="输出Token文件"
    )

    # Version
    subparsers.add_parser("version", help="获取CET版本")

    return parser
