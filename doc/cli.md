# 🖥️ 在命令行中使用

这里是 **CodemaoEDUTools CLI Version** 使用文档，在此文档中，你可以了解所有可用的命令

安装/使用方法参见[此处](../README.md#😎 使用)

## 约束

- 使用大括号包裹的参数，是必填且允许你输入多个参数值的参数（使用空格分隔）：`{}`
- 使用中括号包裹的参数，是必填参数：`<>`
- 使用小括号包裹的参数，是非必填参数（拥有默认值）：`()`

## 全局参数与指令

- `-tf`：参数，Token文件路径，默认值为 **tokens.txt**
- `cet version`：获取当前版本信息
- `cet -h`：获取指令帮助

## 用户类别

这些功能被定义在 `user.py`，是一些与用户有关的功能

### 登录并获取用户Token

`cet get-token -u <用户名（手机号）> -p <密码>`

### 查看Token数量

`cet check-token`

### 签订友好协议

`cet signature -tf (Token文件路径)`

### 关注用户

`cet follow-user -tf (Token文件路径) -uid {训练师编号}`

## 作品类别

这些功能被定义在 `work.py`，是一些与作品互动的功能

### 获取用户所有作品

`cet get-work -uid {训练师编号}`

### 作品点赞

`cet like-work -tf (Token文件路径) -wid {作品ID}`

### 作品收藏

`cet collect-work -tf (Token文件路径) -wid {作品ID}`

### 举报作品

`cet report-work -tf (Token文件路径) -wid {作品ID} -r <举报原因> -d <举报理由>`

- 默认只取Token文件内前二十个进行请求，如果要使用更多，请修改 `__init__.py` 中的变量值

- 可用于举报的原因（Reason），与官网一致，直接填入即可，推荐使用**违法违规**举报理由

  1. 违法违规

  2. 色情低俗

  3. 脏话暴力

  4. 造谣、引战

  5. 抄袭

  6. 广告

  7. 其他

### 评论作品

`cet review-work -tf (Token文件路径) -wid {作品ID} -r <回复内容>`

### 置顶评论（越权）

`cet review-top -wid <作品ID> -cid <评论ID> -t <单个可用Token>`

- 此功能只需要一个 Token，请自行填写

### 取消置顶评论（越权）

`cet review-untop -wid <作品ID> -cid <评论ID> -t <单个可用Token>`

- 此功能只需要一个 Token，请自行填写

### 浏览作品（单刷）

`cet view-work -wid <作品ID> -t <单个可用Token>`

- 此功能只需要一个 Token，请自行填写。默认一直执行，如果需要停止，请 Ctrl+C

### 再创作作品

`cet fork-work -wid {作品ID}`

## EDU类别

这些功能被定义在  `edu.py`，是一些关于编程猫教育平台的功能

注：这部分的Token需要从编程猫教育平台（[https://edu.codemao.cn](https://edu.codemao.cn)）抓取，注册请自行寻法

### 创建新的班级

`cet create-class -t <EDU Token> -cn <班级名称>`

### 添加学生到班级

`cet create-student -t <EDU Token> -cid <班级ID> -sl (学生列表) -o (输出文件名)`

- 学生列表请使用单引号包裹，否则会导致终端误解析！
- 学生列表有默认值，请查看 `__init__.py` 中的变量值
- 输出文件名默认为 `output.xls`

### 合并生成的表格

`cet merge-xls -if <含有多个xls文件的文件夹> -o (输出文件名)`

- 输出文件名默认为 `output.xlsx`

### 批量登录EDU账号

`cet login-edu -i <含有账号密码的xlsx表格路径> -o <输出文件名> -s <是否同时签署友好协议>`

- 输出文件名默认为 `tokens.txt`
- -s 参数接受布尔
