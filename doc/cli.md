# 💻 在命令行中使用

如果你想从命令行使用，请阅读此区域，了解可用的参数

如果你想把这个程序作为库在你的代码中调用，请阅读[此文档](import.md)

> [!TIP]
> 重要更新！自 1.2.0 后，你可以在部分参数中输入用空格分开的多个ID，最大化的节省时间。支持这一特性的参数值已经提前标明
>
> 例如：`python3 main.py follow-user -uid 114514 1919810`

## 可用指令

```
欢迎使用 CodemaoEDUTools! 当前版本: v1.2.3

positional arguments:
  {check-token,get-token,signature,follow-user,get-work,like-work,collect-work,report-work,review-work,review-top,view-work,fork-work,create-class,create-student,merge-xls,login-edu,version}
                        可用命令
    check-token         查看一个Token文件内，有多少个Token（读取行数）
    get-token           登录以获取一个用户的Token
    signature           签订友好协议，推荐在使用其他功能前统一签订一次友好协议，防止出现无法请求的情况
    follow-user         批量关注一个用户，高情商就是刷粉丝
    get-work            获取用户所有作品ID
    like-work           批量点赞一个作品
    collect-work        批量收藏一个作品
    report-work         批量举报一个作品，请勿大量Token举报
    review-work         在一个作品下，批量发送同样的评论
    review-top          越权置顶某个评论
    view-work           给作品加一个浏览，如果要一直刷，只需要循环这个函数就可以，一个Token就够
    fork-work           再创作一个作品
    create-class        在Edu里添加一个新的班级
    create-student      批量把创建新的学生并添加到班级内
    merge-xls           如果要合成为一个xlsx文件用于登录，请使用此函数
    login-edu           批量登录所有在xlsx内保存的账号密码，并打印Token到指定的文件内
    version             获取CET版本

options:
  -h, --help            show this help message and exit

全局参数:
  -tf TOKEN_FILE, --token-file TOKEN_FILE
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

## 用户 (3)

[功能描述](import.md#用户-2)

### 签订友好协议

`-tf <Token文件路径> signature`

### 关注用户

`-tf <Token文件路径> follow-user -uid <训练师编号>`

支持输入多个训练师编号，使用空格分隔每个ID

### 获取用户所有的作品

`-uid <训练师编号>`

支持输入多个训练师编号，使用空格分隔每个ID

返回格式：{作品ID}<空格>{作品ID}

## 作品 (7)

[功能描述](import.md#作品-6)

### 点赞作品

`-tf <Token文件路径> like-work -wid <作品ID>`

支持输入多个作品ID，使用空格分隔每个ID

### 收藏作品

`-tf <Token文件路径> collect-work -wid <作品ID>`

支持输入多个作品ID，使用空格分隔每个ID

### 举报作品

`-tf <Token文件路径> report-work -wid <作品ID> -r <举报原因> -d <举报描述>`

支持输入多个作品ID，使用空格分隔每个ID

> [!IMPORTANT]
> 默认只取Token文件内前二十个进行请求，可在程序中修改变量 `report_readtoken_line`

> [!TIP]
> 可用于举报的原因（Reason），与官网一致，直接填入即可，推荐使用**违法违规**举报理由
> 
> 1. 违法违规
> 2. 色情低俗
> 3. 脏话暴力
> 4. 造谣、引战
> 5. 抄袭
> 6. 广告
> 7. 其他

### 评论作品

`-tf <Token文件路径> review-work -wid <作品ID> -r <回复内容>`

支持输入多个作品ID，使用空格分隔每个ID

支持输入多个回复内容，使用空格分隔每个回复内容。输入多个回复内容后，每个账号将会同时评论这些内容

### 置顶评论（越权）

`review-top -wid <作品ID> -cid <评论ID> -t <一个可用Token>`

### 浏览作品

`view-work -wid <作品ID> -t <一个可用Token>`

### 再创作作品

`-tf <Token文件路径> fork-work -wid <作品ID>`

支持输入多个作品ID，使用空格分隔每个ID

## EDU (4)

[功能描述](import.md#edu-4)

### 添加新的班级

`create-class -t <Edu Token> -cn <班级名称>`

### 添加新的学生到班级

`create-student -t <Edu Token> -cid <班级ID> -sl <学生名字的列表> -o <*.xls>`

> [!WARNING]
> 注意！学生列表请使用单引号包裹，否则会导致终端误解析！

> [!TIP]
> 当不填入 "-sl" 参数值时，程序会使用自带的学生列表

### 合并生成的表格

`merge-xls -if <含有多个xls文件的文件夹> -o <*.xlsx>`

> [!TIP]
> 当不填入 "-o" 参数值时，程序会使用 "output.xlsx" 作为文件名

### 登录Edu账号

`login-edu -i <含有账号密码的xlsx表格文件的路径> -o <*.txt> -s <是否同时签署友好协议{True/False}>`

> [!TIP]
> 当不填入 "-o" 参数值时，程序会使用 "tokens.txt" 作为文件名
> 
> 当不填入 "-s" 参数值时，登录时不会同时签署友好协议