"""
CodemaoEDUTools
==================================
作者: WangZixu
GitHub: https://github.com/Wangs-official/CodemaoEDUTools/

欢迎使用 CodemaoEDUTools!
这是一个Python包，你可以使用 import CodemaoEDUTools 来导入它

开发者不对您使用本项目造成的风险负责，请自行考虑是否使用，谢谢！
"""

__version__ = "2.1.0"
__author__ = "WangZixu"
__description__ = "为编程猫社区的“老师”们提供更便捷的API调用方案，且用且珍惜"

# 线程配置
max_workers = 8

# 举报配置
report_readtoken_line = 20

# 学生名字列表
student_names = [
    "xvbnmklq",
    "asdfghjk",
    "qwertyui",
    "zxcvbnml",
    "poiuytre",
    "lkjhgfds",
    "mnbvcxza",
    "plokmijn",
    "uhbygvtd",
    "crfvtgby",
    "edcrfvtg",
    "qazwsxed",
    "rfvtgbyh",
    "nujmikol",
    "zxasqwde",
    "plmnkoij",
    "bvcdxsza",
    "qwermnbp",
    "asxcvgfr",
    "lpoikmju",
    "yhnujmik",
    "tgbzdxew",
    "rfvgyhuj",
    "edcwsxqa",
    "zaqxswcd",
    "vfrcdews",
    "bgtnhyuj",
    "mkiopluj",
    "nhybtgvr",
    "cdexswza",
    "qwerfdsa",
    "zxcvfdsa",
    "poiuytrw",
    "lkjhgfda",
    "mnbvcxzs",
    "asdfqwer",
    "zxcvqwer",
    "poiulkjh",
    "mnbvcxas",
    "qwertzui",
    "yxcvbnmq",
    "plokmnji",
    "uhbgyvft",
    "crfvtgyn",
    "edcrfvbg",
    "qazwsxrf",
    "rfvtgbyu",
    "nujmiklp",
    "zxasqwed",
    "plmnkoji",
    "bvcdxsaz",
    "qwermnbo",
    "asxcvfgd",
    "lpoikmjn",
    "yhnujmki",
    "tgbzdxec",
    "rfvgyhuk",
    "edcwsxqz",
    "zaqxswce",
    "vfrcdewa",
    "bgtnhyum",
    "mkioplun",
    "nhybtgvf",
    "cdexswzb",
    "qwerfdsz",
    "zxcvfdsz",
    "poiuytrq",
    "lkjhgfdz",
    "mnbvcxzc",
    "asdfqwez",
    "zxcvqwez",
    "poiulkjm",
    "mnbvcxaq",
    "qwertzuy",
    "yxcvbnmr",
    "plokmnjh",
    "uhbgyvfr",
    "crfvtgyb",
    "edcrfvbn",
    "qazwsxre",
    "rfvtgbyi",
    "nujmiklj",
    "zxasqweg",
    "plmnkojh",
    "bvcdxsay",
    "qwermnbu",
    "asxcvfgh",
    "lpoikmjh",
    "yhnujmko",
    "tgbzdxer",
    "rfvgyhun",
    "edcwsxqv",
    "zaqxswec",
    "vfrcdewq",
    "bgtnhyup",
    "mkiopluh",
    "nhybtgvc",
    "cdexswzg",
    "qwerfdsx",
    "zxcvfdsx",
]

# 请在创建新功能后更新此处！

# API函数
from .api import (  # noqa: E402
    PostAPI,
    PostWithoutTokenAPI,
    PostEduAPI,
    GetAPI,
    GetWithoutTokenAPI,
    PutAPI,
    DeleteAPI,
)

# 用户功能
from .user import (  # noqa: E402
    GetUserToken,
    CheckToken,
    SignatureUser,
    FollowUser,
)

# 作品功能
from .work import (  # noqa: E402
    GetUserWork,
    LikeWork,
    CollectionWork,
    ReportWork,
    SendReviewToWork,
    TopReview,
    UnTopReview,
    ViewWork,
    ForkWork,
)

# EDU功能
from .edu import (  # noqa: E402
    CreateClassOnEdu,
    CreateStudentOnEdu,
    MergeStudentXls,
    LoginUseEdu,
)

# 导入命令行
from .cli import CreateParser  # noqa: E402

# 请在创建新功能后更新此处！导入控制
__all__ = [
    # 配置
    "__version__",
    "__author__",
    "__description__",
    "max_workers",
    "student_names",
    "report_readtoken_line",
    # API
    "PostAPI",
    "PostWithoutTokenAPI",
    "PostEduAPI",
    "GetAPI",
    "GetWithoutTokenAPI",
    "PutAPI",
    "DeleteAPI",
    # 用户
    "GetUserToken",
    "CheckToken",
    "SignatureUser",
    "FollowUser",
    # 作品
    "GetUserWork",
    "LikeWork",
    "CollectionWork",
    "ReportWork",
    "SendReviewToWork",
    "TopReview",
    "UnTopReview",
    "ViewWork",
    "ForkWork",
    # 教育版
    "CreateClassOnEdu",
    "CreateStudentOnEdu",
    "MergeStudentXls",
    "LoginUseEdu",
    # 命令行
    "CreateParser",
]


# 包函数
def get_version() -> str:
    """获取版本号"""
    return __version__


def info() -> str:
    """显示包信息"""
    return f"""
CodemaoEDUTools v{__version__}
作者: {__author__}
GitHub: https://github.com/Wangs-official/CodemaoEDUTools/

导入方式:
    import CodemaoEDUTools
    from CodemaoEDUTools import *

命令行使用:
    python main.py check-token

注意事项:
    请合理使用本工具，遵守编程猫平台的使用规则。
    开发者不对滥用本工具造成的后果负责。
"""


def about() -> str:
    """显示关于信息"""
    return f"""
CodemaoEDUTools v{__version__}
作者: {__author__}
GitHub: https://github.com/Wangs-official/CodemaoEDUTools/
"""
