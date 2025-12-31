# 🐱CodemaoEduTool 🔧

编程猫社区学生账号神秘小工具，且用且珍惜

这个程序不仅可以在CLI（命令行）环境中使用，还可以作为一个库被调用

本人编程猫：https://shequ.codemao.cn/user/1458227103

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

## ✌️ 开始使用吧！

- 🌏 如果你想把这个程序作为库在你的代码中调用，请点击[这里](doc/import.md)
- 💻 如果你想从命令行使用，请点击[这里](doc/cli.md)

需要批量调用的部分使用了多线程，速度会更快

## 📃 文件格式

程序不是活人，所以你得知道文件格式

### Token文件的格式

所有与Token有关的都需要使用

**每行一个Token即可**

只要是纯文本格式，什么后缀都可以

### 表格文件的格式

`LoginUseEdu()` 函数所需

由函数`MergeStudentXls()`生成的表格可直接使用 (-em)

也就是没有标题，不要带标题就行，直接就 **账号名-账号-密码**

| {账号名} | {账号} | {密码} |
|:-----:|:----:|:----:|
| {账号名} | {账号} | {密码} |

仅接受 `.xlsx` 后缀文件

## 📂 分支

旧文件将放置在 `old` 分支内，不再更新

`dev` 分支是开发分支，将在完成部分功能后统一推送到 `main`

## 🤔 免责声明/我怎么提问题？

> [!CAUTION]
> 我只是一个搬运工，我把这些API组合到了一起，用的永远是你的Token，不是我的 ，出现的风险，官方找你什么的，别找我，技术无罪，我也无罪
> 
> 还请分清界限，也别给我举报到官方去，你要真想让编程猫变好，不如先从自己开始变好

至于问题解决，如果是你自己的问题，自己百度解决。如果是我的问题，提Issues，我会考虑解决

或者你自己解决，提交PR

## 😇 感谢以下项目的支持！

给我和他们一个 **⭐Star️** 哦

[Aumiao](https://github.com/Aurzex/Aumiao)

[编程猫API文档](https://api.docs.codemao.work/)

本项目是以下项目的改体：

- CodemaoCommunityHistory/CodemaoEduAutoReg
- CodemaoCommunityHistory/CodemaoPL