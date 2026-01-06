# 🔧 贡献指南

感谢你的贡献！不过在贡献之前，请优先阅读此贡献文档

**务必确保你在dev分支！**

## 项目结构

下列列出的是你可以动的文件

- doc/
    - cli.md `CLI使用文档`
    - import.md `作为库调用的文档`
- main.py `主程序`

## 在开发前

1. 请不要加任何的第三方库，现有的库已足够完成程序的编写
2. 开发新功能时，请使用程序已规范的API调用函数，这些函数包含在[这里](import.md#API)
3. 新功能开发后，要同时进行CLI文档与Import文档的编写

## 新功能开发指南

此区域将指引您如何开发新功能，当然，作为开发者的我也三言两语说不清

本人暂时不推荐EDU与API开发，也不会写相关文档

`main.py` 分为三个部分：**函数定义**、**参数处理器**以及**主程序**

你需要先修改版本号：位于33行的`version`变量，将最后一位+1

### 0. 命名规范

功能名使用三引号注释包裹，这也是你要在文档中写出的功能名称，注释上下应各空两行

**每个单词首字母大写** 是CET的函数命名风格，包括函数内包括的参数也是同样的风格

#### 函数命名规范

| **函数后缀** | **对应功能类别** | **举例**             | **开发需要** |
|----------|------------|--------------------|----------|
| *API     | API类别      | PostAPI()          | ❌️       |
| 无        | 功能类别       | 无                  | ✅️       |
| *User    | 用户类别       | FollowUser()       | ✅️       |
| *Work    | 作品类别       | LikeWork()         | ✅️       |
| *EDU     | EDU类别      | CreateClassOnEdu() | ❌️       |

注：功能类别没有函数后缀

#### 参数命名规范（预设）

| **参数名称**  | **功能**    | **需求类型** |
|-----------|-----------|----------|
| Path      | Token文件路径 | Str      |
| UserID    | 训练师ID     | Str      |
| WorkID    | 作品ID      | Str      |
| CommentID | 评论ID      | Str      |
| Token     | 一个Token   | Str      |

这些是预设的参数命名，除此之外的参数可以随意命名，但请注意每个单词首字母大写

#### 处理器变量命名

变量名：`<函数名>_parser`

注：整个变量都是小写字母，例如：`viewwork_parser`对应`ViewWork()`

#### 参数命名（预设）

| **参数缩写** | **参数整写**     | **帮助文本**  |
|----------|--------------|-----------|
| -uid     | --user-id    | 训练师编号     |
| -wid     | --work-id    | 作品ID      |
| -cid     | --comment-id | 评论ID      |
| -t       | --one-token  | 一个可用Token |

这些是预设参数名，剩下的自行命名

#### 命令名

提取重要的部分，给个例子自己体会：

`ViewWork()` -> `view-work`

#### 多数据处理

在训练师编号、作品ID以及评论ID的参数处理器中，加入`nargs='+'`代码以允许用户写入多个参数

其他参数也可以加入此代码

#### 多线程函数命名规范

`CallToAPI_<操作名>`

例如：CollectionWork/**CallToAPI_Collection**

### 1. 函数编写

请先确认你的功能属于哪一类，类别可以在CLI文档中清晰的看到，分为**功能**、**用户**、**作品**以及**作品**。按照你的功能类别，找到每个类别最后一个函数，在它的后面开始编写

每个需要多线程的函数，都分为**主函数**以及**多线程函数**，程序包裹在多线程函数内，不需要多线程的函数只需要写主函数

这是一个带有多线程调用的函数模板，你可以按照这个模板修改：

```python
def ExampleFunction(Path: str) -> bool:
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

### 2. 配置参数处理器

参数处理器在函数`CreateParser()`下定义，同样需要保证顺序，函数写在哪里了，参数处理器就要写在哪里

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

### 3. 主程序编写

同样需要保证顺序，函数写在哪里了，参数处理器就要写在哪里

这是一个主程序模板，不包括多个参数输入：

```python
if args.command == "<命令名>":
    logging.info("请稍后...")
    if <对应的函数名>(<对应参数>):
        logging.info("执行成功")
```

包括多个参数输入：

```python
if args.command == "<命令名>":
    for i in <多个参数的参数名>:
        logging.info(f"请稍后，正在执行{i}")
        if <对应的函数名>(<对应参数>):
            logging.info("执行成功")
```

1. 不要修改提示文本
2. 函数需要`Token`参数输入值时，传入变量：`args.token_file`

### 4. 实例

接下来，写一个实例：使用GET请求接口`/test`来测试用户，接口返回值为成功/失败（通过状态码判断）

```python
...省去上方内容


"""测试用户"""


def TestUser(Path:str, UserID:str) -> bool:
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

def CreateParser():
    # TestUser(Path:str, UserID:str)
    testuser_parser = subparsers.add_parser("test-user", help="测试用户")
    
    testuser_parser.add_argument("-uid", "--user-id", required=True, nargs='+', help="训练师编号")

if __name__ == "__main__":
    if args.command == "test-user":
        for i in args.user_id:
            logging.info(f"请稍后，正在执行{i}")
            if TestUser(args.token_file, i):
                logging.info("执行成功")
```