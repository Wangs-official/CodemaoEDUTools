# 💻 在命令行中使用

如果你想想从命令行使用，请阅读此区域，了解可用的参数

如果你想把这个程序作为库在你的代码中调用，请阅读[此文档](import.md)

## 可用指令

```
usage: main.py [-h] [-tf TOKEN_FILE] {check-token,get-token,signature,follow-user,like-work,collect-work,report-work,review-work,view-work,create-class,create-student,merge-xls,login-edu,version} ...

欢迎使用 CodemaoEDUTools! 当前版本: v1.1.5

positional arguments:
  {check-token,get-token,signature,follow-user,like-work,collect-work,report-work,review-work,view-work,create-class,create-student,merge-xls,login-edu,version}
                        可用命令
    check-token         查看一个Token文件内，有多少个Token（读取行数）
    get-token           登录以获取一个用户的Token
    signature           签订友好协议，推荐在使用其他功能前统一签订一次友好协议，防止出现无法请求的情况
    follow-user         批量关注一个用户，高情商就是刷粉丝
    like-work           批量点赞一个作品
    collect-work        批量收藏一个作品
    report-work         批量举报一个作品，请勿大量Token举报
    review-work         在一个作品下，批量发送同样的评论
    view-work           给作品加一个浏览，如果要一直刷，只需要循环这个函数就可以，一个Token就够
    create-class        在Edu里添加一个新的班级
    create-student      批量把创建新的学生并添加到班级内
    merge-xls           如果要合成为一个xlsx文件用于登录，请使用此函数
    login-edu           批量登录所有在xlsx内保存的账号密码，并打印Token到指定的文件内
    version             获取CET版本

options:
  -h, --help            show this help message and exit

全局参数:
  -tf, --token-file TOKEN_FILE
                        Token文件路径

示例: python3 main.py check-token

```

## 全局参数

`-tf`: Token文件路径，这个参数的默认值是`tokens.txt`

## 获取版本

`python3 main.py version`

## 获得指令帮助

`python3 main.py -h`

## 文档提示

文档仅列出需求的参数，请在参数前加上 `python3 main.py`，并完成库的安装

下方列出的所有参数均为必填

查看功能描述，请点击链接，然后寻找与其对应的标题查看描述

## 功能 (2)

[功能描述](import.md#功能-2)

### 确定Token数量

`-tf <Token文件路径> check-token`

### 获取用户Token

`get-token -u <用户名/手机号> -p <密码>`

## 用户 (2)

[功能描述](import.md#用户-2)

### 签订友好协议

`-tf <Token文件路径> signature`

### 关注用户

`-tf <Token文件路径> follow-user -uid <训练师id>`

## 作品 (5)

[功能描述](import.md#作品-5)

### 点赞作品

`-tf <Token文件路径> like-work -wid <作品id>`

### 收藏作品

`-tf <Token文件路径> collect-work -wid <作品id>`

### 举报作品

`-tf <Token文件路径> report-work -wid <作品id> -r <举报原因> -d <举报描述>`

**⚠️ 请额外分出来20~25个Token使用此函数，不要几千个Token一起举报，选择"违法违规"的话20个Token就能让作品进到审核状态**

> 可用于举报的原因（Reason），与官网一致，直接填入即可
> 
> 推荐使用**违法违规**举报理由
> 1. 违法违规
> 2. 色情低俗
> 3. 脏话暴力
> 4. 造谣、引战
> 5. 抄袭
> 6. 广告
> 7. 其他

### 评论作品

`-tf <Token文件路径> review-work -wid <作品id> -r <回复内容>`

### 浏览作品

`view-work -wid <作品id> -t <一个可用Token>`

## EDU (4)

[功能描述](import.md#edu-4)

### 添加新的班级

`create-class -t <Edu Token> -cn <班级名称>`

### 添加新的学生到班级

`create-student -t <Edu Token> -cid <班级ID> -sl <学生名字的列表> -o <*.xls>`

> 注意！学生列表请使用单引号包裹，否则会导致终端误解析！

### 合并生成的表格

`merge-xls -if <含有多个xls文件的文件夹> -o <*.xlsx>`

### 登录Edu账号

`login-edu -i <含有账号密码的xlsx表格文件的路径> -o <*.txt(推荐tokens.txt)>`