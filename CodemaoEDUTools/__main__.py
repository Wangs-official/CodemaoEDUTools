import json
import logging
import coloredlogs

from CodemaoEDUTools import CreateParser, __version__

coloredlogs.install(level="INFO", fmt="%(asctime)s - %(funcName)s: %(message)s")


def main():
    parser = CreateParser()
    args = parser.parse_args()

    if args.command is None:
        logging.info(f'''
 ██████╗ ██████╗ ██████╗ ███████╗███╗   ███╗ █████╗  ██████╗ ███████╗██████╗ ██╗   ██╗████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝████╗ ████║██╔══██╗██╔═══██╗██╔════╝██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
██║     ██║   ██║██║  ██║█████╗  ██╔████╔██║███████║██║   ██║█████╗  ██║  ██║██║   ██║   ██║   ██║   ██║██║   ██║██║     ███████╗
██║     ██║   ██║██║  ██║██╔══╝  ██║╚██╔╝██║██╔══██║██║   ██║██╔══╝  ██║  ██║██║   ██║   ██║   ██║   ██║██║   ██║██║     ╚════██║
╚██████╗╚██████╔╝██████╔╝███████╗██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗██████╔╝╚██████╔╝   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═════╝  ╚═════╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
-==============================================================================-
欢迎使用CodemaoEDUTools CLI Version {__version__}
您正在使用的是 CodemaoEDUTools 的命令行版本
输入 "-h" 获得使用帮助
-==============================================================================-
''')

    if args.command == "check-token":
        from CodemaoEDUTools import CheckToken

        logging.info(f"可用Token数量: {CheckToken(args.token_file)}")

    if args.command == "get-token":
        from CodemaoEDUTools import GetUserToken

        logging.info(GetUserToken(args.username, args.password))

    if args.command == "signature":
        from CodemaoEDUTools import SignatureUser

        logging.info("请稍后...")
        if SignatureUser(args.token_file):
            logging.info("执行成功")

    if args.command == "follow-user":
        from CodemaoEDUTools import FollowUser

        for i in args.user_id:
            logging.info(f"请稍后，正在执行：{i}")
            if FollowUser(args.token_file, i):
                logging.info("执行成功")

    if args.command == "get-work":
        from CodemaoEDUTools import GetUserWork

        for i in args.user_id:
            logging.info(f"请稍后，正在执行：{i}")
            if not GetUserWork(i):
                pass
            else:
                logging.info(f"用户：{i} 的作品列表：")
                logging.info(GetUserWork(i))

    if args.command == "like-work":
        from CodemaoEDUTools import LikeWork

        for i in args.work_id:
            logging.info(f"请稍后，正在执行：{i}")
            if LikeWork(args.token_file, i):
                logging.info("执行成功")

    if args.command == "collect-work":
        from CodemaoEDUTools import CollectionWork

        for i in args.work_id:
            logging.info(f"请稍后，正在执行：{i}")
            if CollectionWork(args.token_file, i):
                logging.info("执行成功")

    if args.command == "report-work":
        from CodemaoEDUTools import ReportWork

        for i in args.work_id:
            logging.info(f"请稍后，正在执行：{i}")
            if ReportWork(args.token_file, i, args.report_reason, args.report_describe):
                logging.info("执行成功")

    if args.command == "review-work":
        from CodemaoEDUTools import SendReviewToWork

        for i in args.work_id:
            for r in args.review_text:
                logging.info(f"请稍后，正在执行：{i} | 发送内容：{r}")
                if SendReviewToWork(args.token_file, i, r):
                    logging.info("执行成功")

    if args.command == "review-top":
        from CodemaoEDUTools import TopReview

        logging.info("请稍后...")
        if TopReview(args.one_token, args.work_id, args.comment_id):
            logging.info("执行成功")
    
    if args.command == "unreview-top":
        from CodemaoEDUTools import UnTopReview

        logging.info("请稍后...")
        if UnTopReview(args.one_token, args.work_id, args.comment_id):
            logging.info("执行成功")

    if args.command == "view-work":
        from CodemaoEDUTools import ViewWork

        logging.info("请稍后...")
        if ViewWork(args.one_token, args.work_id):
            logging.info("执行成功")

    if args.command == "fork-work":
        from CodemaoEDUTools import ForkWork

        for i in args.work_id:
            logging.info(f"请稍后，正在执行：{i}")
            if ForkWork(args.token_file, i):
                logging.info("执行成功")

    if args.command == "create-class":
        from CodemaoEDUTools import CreateClassOnEdu

        logging.info("请稍后...")
        logging.info(f"Class ID: {CreateClassOnEdu(args.token, args.class_name)}")

    if args.command == "create-student":
        from CodemaoEDUTools import CreateStudentOnEdu

        logging.info("请稍后...")
        try:
            with open(args.output_xls, "wb") as f:
                f.write(
                    CreateStudentOnEdu(
                        args.token, args.class_id, json.loads(args.student_name_list)
                    )
                )
                f.close()
            logging.info(f"执行成功，学生密码表已保存到: {args.output_xls}")
        except Exception as e:
            import os

            if os.path.exists(args.output_xls):
                os.remove(args.output_xls)
            logging.error(f"执行失败: {e}")
            exit()

    if args.command == "merge-xls":
        from CodemaoEDUTools import MergeStudentXls

        logging.info("请稍后...")
        if MergeStudentXls(args.input_xls_folder, args.output_xlsx):
            logging.info(f"执行成功，合并的文件已保存到：{args.output_xlsx}")

    if args.command == "login-edu":
        from CodemaoEDUTools import LoginUseEdu

        logging.info("请稍后...")
        if LoginUseEdu(args.input_xlsx, args.output_txt, args.signature_user):
            logging.info(f"执行成功，已将登录的Token保存到：{args.output_txt}")

    if args.command == "version":
        logging.info(f"CET版本: v{__version__}")
        logging.info("https://github.com/Wangs-official/CodemaoEDUTools/")


if __name__ == "__main__":
    main()
