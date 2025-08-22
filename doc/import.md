# 🌏 作为库使用

`import CodemaoEDUTools`

如果你想把这个程序作为库在你的代码中调用，请阅读此区域，了解可用的函数

如果你只是想从命令行使用，请阅读[此文档](cli.md)

1. API
2. 功能
3. 用户
4. 作品
5. EDU

## API (4)

`*API`

Header 已准备好，使用`UserAgent().random`随机生成UA

### 使用POST方式调用API

`PostAPI(Path: str, PostData: dict, Token: str)`

- Path: API路径，不包括 **https://api.codemao.cn** 部分
- PostData: 字典格式的请求体
- Token: 单个Token放入

携带Token，以POST方式调用一个编程猫API

- 返回: `requests.Response`

### 使用POST方式匿名调用API

`PostWithoutTokenAPI(Path: str, PostData: dict)`

- Path: API路径，不包括 **https://api.codemao.cn** 部分
- PostData: 字典格式的请求体

不携带Token，以POST方式调用一个编程猫API

- 返回类型: `requests.Response`

### 使用POST方式调用EduAPI

`PostEduAPI(Path: str, PostData: dict, Token: str)`

- Path: API路径，不包括 **https://eduzone.codemao.cn** 部分
- Token: 单个Token放入

携带Token，以POST方式调用一个编程猫EduAPI（https://eduzone.codemao.cn）

- 返回类型: `requests.Response`

### 使用GET方式调用API

`GetAPI(Path: str, Token: str)`

- Path: API路径，不包括 **https://api.codemao.cn** 部分
- Token: 单个Token放入

携带Token，以GET方式调用一个编程猫API

- 返回类型: `requests.Response`

## 功能 (2)

### 确定Token数量

`Check_TokenFile(Path: str)`

- Path: Token文件路径，Token文件格式请参考README中的 **📃 文件格式**

查看一个Token文件内，有多少个Token（读取行数）

- 返回类型: `int`
- 返回值: Token数量

### 登录并获取用户Token

`GetUserToken(Username: str, Password: str)`

- Username: 用户名（手机号）
- Password: 密码

登录以获取一个用户的Token

- 返回类型: `str | bool`
- 返回值: 可用于请求的Token，请求失败时，返回False

## 用户 (2)

`*User`

### 签订友好协议

`SignatureUser(Path: str)`

- Path: Token文件路径，Token文件格式请参考README中的 **📃 文件格式**

签订友好协议，推荐在使用其他功能前统一签订一次友好协议，防止出现无法请求的情况

- 返回类型: `bool`
- 返回值: 请求完成后，返回**True**

### 关注用户

`FollowUser(Path: str, UserID: str)`

- Path: Token文件路径，Token文件格式请参考README中的 **📃 文件格式**
- UserID: 训练师编号

批量关注一个用户，高情商就是刷粉丝

- 返回类型: `bool`
- 返回值: 请求完成后，返回**True**

## 作品 (5)

`*Work`

### 点赞作品

`LikeWork(Path: str, WorkID: str)`

- Path: Token文件路径，Token文件格式请参考README中的 **📃 文件格式**
- WorkID: 作品ID

批量点赞一个作品

- 返回类型: `bool`
- 返回值: 请求完成后，返回**True**

### 收藏作品

`CollectionWork(Path: str, WorkID: str)`

- Path: Token文件路径，Token文件格式请参考README中的 **📃 文件格式**
- WorkID: 作品ID

批量收藏一个作品

- 返回类型: `bool`
- 返回值: 请求完成后，返回**True**

### 举报作品

`ReportWork(Path: str, WorkID: str, Reason: str, Describe: str)`

- Path: Token文件路径，Token文件格式请参考README中的 **📃 文件格式**
- WorkID: 作品ID
- Reason: 原因，请参考下方给出的可用方式
- Describe: 描述

批量举报一个作品

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

- 返回类型: `bool`
- 返回值: 请求完成后，返回**True**

### 评论作品

`SendReviewToWork(Path: str, WorkID: str, ReviewText: str)`

- Path: Token文件路径，Token文件格式请参考README中的 **📃 文件格式**
- WorkID: 作品ID
- ReviewText: 评论内容

在一个作品下，批量发送同样的评论

- 返回类型: `bool`
- 返回值: 请求完成后，返回**True**

### 浏览作品

`ViewWork(Token: str, WorkID: str)`

- Token: **单个可用Token**
- WorkID: 作品ID

给作品加一个浏览，如果要一直刷，只需要循环这个函数就可以，一个Token就够

- 返回类型: `bool`
- 返回值: 请求完成后，返回**True**

## EDU (4)

`*EDU`

### 添加新的班级

`CreateClassOnEdu(Token: str, ClassName: str)`

- Token: 单个可用Token，需从Edu内抓包
- ClassName: 班级名称，遵循官方命名规则 

在Edu里添加一个新的班级

- 返回类型: `str`
- 返回值: 请求完成后，返回字符串形式的班级ID；如果请求失败，将返回字符“0”

### 添加新的学生到班级

`CreateStudentOnEdu(Token: str, ClassID: str, StudentNameList: list[str])`

- Token: 单个可用Token，需从Edu内抓包
- ClassID: 班级ID，自行抓包获取，或使用`CreateClassOnEdu`函数返回值
- StudentNameList: 学生名字的列表，最多100个学生，学生命名遵循官方命名规则

批量把创建新的学生并添加到班级内

- 返回类型: `bytes`
- 返回值: 请求完成后，返回含有学生账号密码表的excel二进制内容（遵循官方）。请将返回内容转存到以`.xls`结尾的表格文件中。如果请求失败，则返回None
- 处理方式:
```python
import CodemaoEDUTools
# ...省略变量定义
with open("test.xls", wb) as f:
    # 以写入字节模式打开 test.xls
    f.write(CreateStudentOnEdu(Token="abc", ClassID="114514", StudentNameList= StuNameList))
    f.close()
# 写入学生信息完毕
```

### 合并生成的表格

`MergeStudentXls(InputFolder: str, OutputFile:str)`

- InputFolder: 含有多个 **.xls** 文件的文件夹
- OutputFile: 输出文件名，需要填写 **.xlsx** 后缀

使用`CreateStudentOnEdu()`函数后会输出散乱的xls文件，如果要合成为一个xlsx文件用于登录，请使用此函数

- 返回类型: `bool`
- 返回值: 操作完成后，返回**True**

### 登录Edu账号

`LoginUseEdu(InputXlsx:str, OutputFile:str)`

- InputXlsx: 含有账号密码的xlsx表格文件的路径，文件格式请参考README中的 **📃 文件格式**
- OutputFileName: 输出文件名，需要填写 **.txt** 后缀

批量登录所有在xlsx内保存的账号密码，并打印Token到指定的文件内

- 返回类型: `bool`
- 返回值: 操作完成后，返回**True**

## 错误追踪

当请求出现问题时，日志会输出以下内容

1. `请求失败，状态码: xxx, 响应: xxx`

    这种情况是API返回了异常

2. `请求异常: xxx`

    这种情况是Python自己出现了错误