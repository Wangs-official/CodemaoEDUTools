# 🐱CodemaoEduTool 🔧

编程猫社区学生账号神秘小工具，且用且珍惜

本次重构，允许用户在命令行中使用一个脚本完成多项操作，并允许用户在其他脚本中将此代码作为库调用

本人编程猫：https://shequ.codemao.cn/user/1458227103

## 🤔文件夹与分支

工具将放置在 `Tools` 文件夹内，这些东西放在重构代码中更为臃肿与麻烦，故放置于此

旧文件将放置在 `old` 分支内，不再更新

`dev` 分支是开发分支，将在完成部分功能后统一推送到 `main`

## 🔧 环境

请在使用前在命令行中运行:

`pip3 install -r requirements.txt`

如果要作为库打包在你的程序中，请在需求列表中填写以下库:

```
fake_useragent
coloredlogs
argparse
requests
openpyxl
pandas
```

## 🌏作为库使用

`import CodemaoEDUTools`

如果你想把这个程序作为库在你的代码中调用，请阅读此区域，了解可用的函数

如果你只是想从命令行使用，请阅读下一区域：**💻 从命令行使用**

1. API
2. 功能
3. 用户
4. 作品

### API (3)

`*API`

Header 已准备好，使用`UserAgent().random`随机生成UA

#### 使用POST方式调用API

`PostAPI(Path: str, PostData: dict, Token: str) -> requests.Response`

- Path: API路径，不包括 **https://api.codemao.cn** 部分
- PostData: 字典格式的请求体
- Token: 单个Token放入

携带Token，以POST方式调用一个编程猫API

- 返回: `requests.Response`

#### 使用POST方式匿名调用API

`PostWithoutTokenAPI(Path: str, PostData: dict)`

- Path: API路径，不包括 **https://api.codemao.cn** 部分
- PostData: 字典格式的请求体

不携带Token，以POST方式调用一个编程猫API

- 返回类型: `requests.Response`

#### 使用GET方式调用API

`GetAPI(Path: str, Token: str)`

- Path: API路径，不包括 **https://api.codemao.cn** 部分
- Token: 单个Token放入

携带Token，以GET方式调用一个编程猫API

- 返回类型: `requests.Response`

### 功能 (1)

#### 确定Token数量

`Check_TokenFile(Path: str)`

- Path: Token文件路径，Token文件格式请参考下方 **📃 文件格式**

查看一个Token文件内，有多少个Token（读取行数）

- 返回类型: `int`
- 返回值: Token数量

#### 登录并获取用户Token

`GetUserToken(Username: str, Password: str)`

- Username: 用户名（手机号）
- Password: 密码

获取一个用户的Token

- 返回类型: `str`
- 返回值: 可用于请求的Token

### 用户 (2)

`*User`

#### 签订友好协议

`SignatureUser(Path: str)`

- Path: Token文件路径，Token文件格式请参考下方 **📃 文件格式**

签订友好协议，推荐在使用其他功能前统一签订一次友好协议，防止出现无法请求的情况

- 返回类型: `bool`
- 返回值: 请求完成后，返回**True**

#### 关注用户

`FollowUser(Path: str, UserID: str)`

- Path: Token文件路径，Token文件格式请参考下方 **📃 文件格式**
- UserID: 训练师编号

批量关注一个用户，高情商就是刷粉丝

- 返回类型: `bool`
- 返回值: 请求完成后，返回**True**

### 作品 (5)

#### 点赞作品

`LikeWork(Path: str, WorkID: str) `

- Path: Token文件路径，Token文件格式请参考下方 **📃 文件格式**
- WorkID: 作品ID

批量点赞一个作品

- 返回类型: `bool`
- 返回值: 请求完成后，返回**True**

#### 收藏作品

`CollectionWork(Path: str, WorkID: str) `

- Path: Token文件路径，Token文件格式请参考下方 **📃 文件格式**
- WorkID: 作品ID

批量收藏一个作品

- 返回类型: `bool`
- 返回值: 请求完成后，返回**True**

#### 举报作品

`ReportWork(Path: str, WorkID: str, Reason: str, Describe: str)`

- Path: Token文件路径，Token文件格式请参考下方 **📃 文件格式**
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

#### 在作品下发送回复

`SendReviewToWork(Path: str, WorkID: str, ReviewText: str)`

- Path: Token文件路径，Token文件格式请参考下方 **📃 文件格式**
- WorkID: 作品ID
- ReviewText: 回复内容

在一个作品下，批量发送同样的评论

- 返回类型: `bool`
- 返回值: 请求完成后，返回**True**

#### 浏览作品

`ViewWork(Token: str, WorkID: str)`

- Token: **单个可用Token**
- WorkID: 作品ID

给作品加一个浏览，如果要一直刷，只需要循环这个函数就可以，一个Token就够

- 返回类型: `bool`
- 返回值: 请求完成后，返回**True**

### 错误追踪

当请求出现问题时，日志会输出以下内容

1. `请求失败，状态码: xxx, 响应: xxx`

    这种情况是API返回了异常

2. `请求异常: xxx`

    这种情况是Python自己出现了错误