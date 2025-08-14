# @author Wangs_official
import time
import requests
import json
import random


def get_class(token):
    header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Authorization": f"Bearer {token}"
    }
    url = f"https://eduzone.codemao.cn/edu/zone/classes?page=1&TIME={int(time.time())}"
    req = requests.get(url=url, headers=header)
    if req.status_code == 200:
        return str(json.loads(req.text).get("total"))
    else:
        print(f"请求失败：{req.text}")
        return False


def create_class(token):
    header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Authorization": f"Bearer {token}"
    }
    # 生成12个随机大写字母作为班级名称
    li = []
    for i in range(12):
        temp = random.randrange(65, 91)
        c = chr(temp)
        li.append(c)
    result = "".join(li)
    wc_name = f"{result}"

    # 创建班级
    req = requests.post("https://eduzone.codemao.cn/edu/zone/class",
                        data=json.dumps({"name": wc_name}),
                        headers=header)

    if req.status_code == 200:
        id = json.loads(req.text).get("id")
        # 准备学生名单
        stud_names = json.dumps({"student_names": ["vlokud", "mgstop", "waidtk", "ruabon", "ncxjsb", "apgtxw", "sqnpfx",
                                                   "qvxpgr", "yihsdm", "vzgsub", "fxywlt", "smqwvt", "qdrjoe", "rohgzt",
                                                   "fpzuvd", "zfcuhy", "kfmlsd", "uxdwsc", "qyvkle", "vstunq", "pqbcjx",
                                                   "hcxfyd", "caewzx", "obaxfu", "qfobkc", "inrdqg", "ftizlb", "jahdoz",
                                                   "himayz", "fdrjnv", "lzjxpd", "lzqguo", "zvywpa", "batmqp", "vdtgzf",
                                                   "qihpke", "lgdtxn", "mevsfn", "gkpzth", "naxtby", "oejtmv", "vpwbga",
                                                   "twfpav", "mabxio", "zbhyoc", "xgfshv", "zumfnp", "tmajfv", "qtwzma",
                                                   "fozhjb", "sgaouk", "odkxzy", "hkexpl", "byuzpc", "vjlxsh", "gdczwr",
                                                   "urhtav", "txyjrc", "oalhkz", "yfkxbg", "mliqdx", "osqxck", "adbtro",
                                                   "qdzfeb", "ldjvuw", "glhkns", "flevyk", "lrkxta", "lamjey", "fphkcr",
                                                   "hxolyc", "euvdmh", "vpdkue", "bqonci", "fmibrj", "zfvjcm", "efhyvj",
                                                   "ljguwc", "ckamsg", "hwlned", "utzxer", "mtdnwy", "xitflg", "xgdofl",
                                                   "gvirnt", "zvbkos", "gvcjhi", "wqceok", "lvhnto", "caurnj", "xhwnfl",
                                                   "qeykzn", "tkefna", "hbamgv", "sinrpq", "xponme", "zpwquc", "hebomj",
                                                   "bzsxlp", "mjcotf"]})
        # 添加学生
        req2 = requests.post(f"https://eduzone.codemao.cn/edu/zone/class/{id}/students",
                             data=stud_names,
                             headers=header)

        if req2.status_code == 200:
            # 确保xls目录存在
            if not os.path.exists("xls"):
                os.makedirs("xls")
            # 保存学生名单
            with open(f"xls/{id}.xls", "wb") as f:
                f.write(req2.content)
            return True
        else:
            print(f"添加学生失败：{req2.text}")
            return False
    else:
        print(f"创建班级失败：{req.text}")
        return False


if __name__ == "__main__":
    itoken = input("请输入账户Token: ")
    print("将以12个字母作为班级名称，且将学生信息保存到当前目录下的xls文件夹")

    try:
        current_class_count = int(get_class(itoken))
    except TypeError:
        exit("获取班级数量失败，请检查Token是否正确")

    max_class_count = 10  # 设置最大班级数为10
    remaining = max_class_count - current_class_count

    if remaining <= 0:
        exit(f"您的账户已有{current_class_count}个班级，已达到或超过{max_class_count}个班级的上限")

    print(f"将创建{remaining}个班级")

    created = 0
    for _ in range(remaining):
        if create_class(itoken):
            created += 1
            print(f"已成功创建{created}/{remaining}个班级")
        else:
            print("创建过程中出现错误，已停止")
            break

    print(f"操作完成，共创建了{created}个班级")