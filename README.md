# CodemaoTool

批量调用API解决方案

且用且珍惜，本项目是以下项目的集合体：

- CodemaoCommunityHistory/CodemaoEduAutoReg
- CodemaoCommunityHistory/CodemaoPL

本人编程猫：https://shequ.codemao.cn/user/1458227103

更新随缘

## 需求

1. 需要安装Python
2. 需要安装 `requests`, `openpyxl`, `queuelib` 库
3. CPU好一点，因为跑8线程
4. 你得有EDU账号

## 使用（API）

全部文件调用的Token都在`tokens.txt`文件内，请先执行登录

### 登录

通过编程猫官方的登录API，获取账号的Token

`python3 login.py`

执行后输入Excel表格路径即可，仅支持 **.xlsx** 文件

登录后Token会保存到本地的`tokens.txt`文件内，其他脚本会自动获取Token，请注意安全保存

文件格式请查看下方的 **注意事项**

### 签订友好协议

不过的话，有些东西用不了

`python3 signature.py`

### 关注

`python3 follow.py`

### 点赞＋收藏

`python3 2l.py`

### 刷浏览量

`python3 view.py`

**需要一个Token，随便找一个就好**

### 打作品

`python3 report.py`

注意！请额外创建一个文件放入少量（约100个Token），禁止几千个Token一起往里扔！

> 据好心人测试，只需要放入25个Token就可以打死，所以自己悠着来
> 作品显示正在审核，这就是打成功了

## 使用（EduReg）

文件夹：`Edu_Reg`

还请注意，根据目前的编程猫EDU策略，每个教师最多可创建1000个学生，脚本会默认创建1000个学生

脚本不会自己注册，请自行注册后抓包获取Token后填写

### 第一步：开始注册

`python3 reg.py`

### 第二步：合并

`python3 merge.py`

### 第三步：换地方

将文件夹下生成的xlsx文件拖到上一层目录

## 开发

程序已简化API调用流程，请在开始前引用 control 库

```python
import control
```

### 值

#### API路径

- 类型: String
- 取值: 取 https://api.codemao.cn/ 路径后的所有内容
- 举例: `nemo/v2/works/114514/collection`

#### POST报文

- 类型: JSON
- 取值：JSON格式即可

#### Token

- 类型: String
- 取值：填入一个Token，多线程请自己分配

### 用法

#### POST请求

```python
import control

control.call_api(API路径, POST报文, Token)
```

#### GET请求

```python
import control

control.get_api(API路径, Token)
```

#### 返回

与 requests 返回值获取方式一致

```python
import control

print(control.get_api("test/api","Token...").status_code)
```

这个示例可以打印请求后的状态码

## 注意事项

### 表格文件的格式

**由上一部分生成的表格可直接使用**

直接下载的表格可能会有标题，请把他们变成这样的格式，或者查看 `other/example.xlsx`		

也就是没有标题，不要带标题就行，直接就 **账号名-账号-密码**

| {账号名} | {账号} | {密码} |
|:-----:|:----:|:----:|
| {账号名} | {账号} | {密码} |

> 官网下载的可能不是xlsx，记得另存为 .xlsx !

### 如何获取Token?

1. 使用API获取

    执行 `python3 get_mytoken.py` , 按照提示登录即可

2. 抓包提取请求头

    在请求头中寻找 **Authorization** 所对应的值，**Bearer**后面的**所有内容**（像乱码一样）就是你的Token

### 返回

有的文件我偷懒了没写完成提示，还有的完成提示不一样

如果脚本正常结束了，没有报错，那就是完成了

没完成的时候别动

## 免责声明

我只是一个搬运工，我把这些API组合到了一起

用的永远是你的Token，不是我的

出现的风险，官方找你什么的，别找我，技术无罪，我也无罪

## 问题解决

自己百度解决，我写的没问题，我的测试全部通过

## 特别鸣谢

[编程猫API文档](https://api.docs.codemao.work/)

