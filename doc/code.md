# 🔧 开发文档

这里是 **CodemaoEDUTools** 的开发文档，在此文档中，你可以了解如何给此项目进行贡献

## 项目结构

```txt
.
├── CodemaoEDUTools
│   ├── __init__.py
│   ├── __main__.py
│   ├── __pycache__
│   ├── api.py
│   ├── cli.py
│   ├── edu.py
│   ├── user.py
│   └── work.py
├── doc
│   ├── cli.md
│   ├── code.md
│   └── import.md
├── LICENSE
├── README.md
└── setup.py
```

## 命名规范

### 函数命名规范

| **函数后缀** | **对应功能类别** | **举例**             |
|:----------:|:------------:|:--------------------:|
| *API | API类别      | PostAPI()          |
| 无        | 功能类别       | 无                  |
| *User    | 用户类别       | FollowUser()       |
| *Work    | 作品类别       | LikeWork()         |
| *EDU     | EDU类别      | CreateClassOnEdu() |

注：功能类别没有函数后缀

### 多线程函数命名规范

`CallToAPI_<操作名>`

例如：CollectionWork/**CallToAPI_Collection**

### 参数命名规范（预设）

| **参数名称**  | **功能**    | **需求类型** |
|:-----------:|:-----------:|:----------:|
| Path      | Token文件路径 | Str      |
| UserID    | 训练师编号     | Str      |
| WorkID    | 作品ID      | Str      |
| CommentID | 评论ID      | Str      |
| Token     | 一个Token   | Str      |

### 处理器变量命名

变量名：`<函数名>_parser`

注：整个变量都是小写字母，例如：`viewwork_parser`对应`ViewWork()`

### 参数命名（预设）

| **参数缩写** | **参数整写**     | **帮助文本**  |
|----------|--------------|-----------|
| -uid     | --user-id    | 训练师编号     |
| -wid     | --work-id    | 作品ID      |
| -cid     | --comment-id | 评论ID      |
| -t       | --one-token  | 一个可用Token |

这些是预设参数名，剩下的自行命名

### 命令名

提取重要的部分，给个例子自己体会：

`ViewWork()` -> `view-work`

## 新功能开发

请先确认你的功能属于哪一类，每个类别都有属于自己的文件，看命名就能看出来

在每个文件的最后面来写你的新功能，不要插队

### 函数开发

每个需要多线程的函数，都分为**主函数**以及**多线程函数**，程序包裹在多线程函数内，不需要多线程的函数只需要写主函数

这是一个带有多线程调用的函数模板，你可以按照这个模板修改：

```python
def ExampleFunction(Path: str) -> bool:
    """函数功能描述"""
    if not os.path.exists(Path):
        logging.error(f"找不到Token文件: {Path}")
        return False
    elif CheckToken(Path) == 0:
        logging.warning("可用的Token数为0")
        return False
    else:
        with open(Path, "r") as f:
            TokenList = [line.strip() for line in f if line.strip()]
            f.close()

        def CallToAPI_ExampleAction(Token: str) -> bool:
            try:
                response = PostAPI(Path=f"<API地址>", PostData={}, Token=Token)

                if response.status_code == 200:
                    return True
                else:
                    logging.error(f"请求失败，状态码: {response.status_code}, 响应: {response.text[:100]}")
                    return False
            except Exception as e:
                logging.error(f"请求异常: {str(e)}")
                return False

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(CallToAPI_ExampleAction, TokenList))
            sum(results)

        return True
```

1. 函数参数：要求标明参数，如果这个函数的请求结果没有任何实质性的作用（只用来确认是否成功），那函数返回`bool`类型即可，若有实质性内容，返回`str | bool`
2. 返回值：如果没有实质性内容，按照请求情况返回True/False，若有实质性内容，返回对应内容
3. 其实，你需要做的只有修改函数名和API地址，以及修改对应的API调用函数和报文
4. 不知道咋说了

### 配置参数处理器

打开文件 `cli.py`，开始配置参数处理器

需要保证顺序，函数写在哪里了，参数处理器就要写在哪里

这是一个参数处理器模板：

```python
# ExampleFunction(WorkID: str)
examplefunction_parser = subparsers.add_parser("<命令名>", help="<帮助文本>")

sendrevietowork_parser.add_argument("-wid", "--work-id", required=True, nargs='+', help="作品ID")

sendrevietowork_parser.add_argument("<参数简写>", "<参数整写>",required=True, help="<帮助文本>")
```

1. 最上面的注释：直接把函数定义复制过来
2. 帮助文本需要直观
3. 非需要参数（`required=True`）需要填写默认值

### 入口编写

打开 `__main__.py`，开始配置入口

同样需要保证顺序，函数写在哪里了，入口就要写在哪里

这是一个主程序模板，不包括多个参数输入：

```python
if args.command == "<命令名>":
    from CodemaoEDUTools import <对应的函数名>

    logging.info("请稍后...")
    if <对应的函数名>(<对应参数>):
        logging.info("执行成功")
```

包括多个参数输入：

```python
if args.command == "<命令名>":
    from CodemaoEDUTools import <对应的函数名>

    for i in <多个参数的参数名>:
        logging.info(f"请稍后，正在执行{i}")
        if <对应的函数名>(<对应参数>):
            logging.info("执行成功")
```

1. 不要修改提示文本
2. 函数需要`Token`参数输入值时，传入变量：`args.token_file`
3. 记得 import

### 实例

接下来，写一个实例：使用GET请求接口`/test`来测试用户，接口返回值为成功/失败（通过状态码判断）

#### user.py

```python
...省去上方内容

def TestUser(Path:str, UserID:str) -> bool:
    """测试用户"""
    if not os.path.exists(Path):
        logging.error(f"找不到Token文件: {Path}")
        return False
    elif CheckToken(Path) == 0:
        logging.warning("可用的Token数为0")
        return False
    else:
        with open(Path, "r") as f:
            TokenList = [line.strip() for line in f if line.strip()]
            f.close()

        def CallToAPI_TestUser(Token: str) -> bool:
            try:
                response = GetAPI(Path=f"/test", Token=Token)

                if response.status_code == 200:
                    return True
                else:
                    logging.error(f"请求失败，状态码: {response.status_code}, 响应: {response.text[:100]}")
                    return False
            except Exception as e:
                logging.error(f"请求异常: {str(e)}")
                return False

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(CallToAPI_ExampleAction, TokenList))
            sum(results)

        return True
```

#### cli.py

```python
# TestUser(Path:str, UserID:str)
testuser_parser = subparsers.add_parser("test-user", help="测试用户")

testuser_parser.add_argument("-uid", "--user-id", required=True, nargs='+', help="训练师编号")
```

**\_\_main\_\_.py**

```python
if args.command == "test-user":
    from CodemaoEDUTools import TestUser

    for i in args.user_id:
        logging.info(f"请稍后，正在执行{i}")
        if TestUser(args.token_file, i):
            logging.info("执行成功")
```

### 导入功能

打开 `__init__.py` 文件，进行修改

注释已标明应修改的位置，自127行开始，你需要在对应的类别中加上新功能的函数名，并以半角逗号结尾

并且，你也要修改自170行开始的 `__all__`，你需要在对应的类别中加上新功能的函数名，使用引号包裹，并以半角逗号结尾

### 文档编写

你需要在`doc/cli.md`以及`doc/import.md`中进行文档的编写

同样需要保证顺序，函数写在哪里了，文档就要写在哪里

至于格式，我相信你能看懂，我就不过多去说了

### 代码格式化

如果你在使用 VScode，请使用 **Ruff** 插件格式化文件！

## 修改现有的功能/BUG修复

修改现有的功能时，如果要修改函数参数值，请在后续代码中和文档中做出修改

不要乱动代码格式

## 贡献要求

请Fork本仓库，将代码PR到`dev`分支，不接受任何推送到`main`分支的PR

### Commit Message 要求

没有格式要求，具体说明这个提交的修改

### Pull Requests 发起要求

请按照模板填写两个框，其中的**更新日志**这样填写：

```txt
[+] 这是新功能的TAG，在这里写添加的新功能
[x] 这是删除功能的TAG，在这里填写删除的功能
[~] 这是轻修改TAG，在这里填写修复BUG/对代码进行优化的描述
```

比如添加了一个TestUser的功能，就这样写，要写无序列表

```txt
- [+] 新增功能：测试用户，使用`test-user`
```

### Pull Requests 标题要求

`<更新标签><更新内容>`

更新标签：

- Feat: 新功能
- Fix: 修复
- Version: 版本合并
- Lite: 轻量化更新

例如添加了一个新功能和修复了一个BUG，那就写：

`[Feat/Fix]添加一个功能和修复内容`

### 版本号修改要求

版本号位于 `__init__.py` 中的 `__version__` 变量，更新时，请将版本号最后一位+1

可能不会接受版本号未修改的PR
