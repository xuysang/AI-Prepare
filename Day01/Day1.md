### 1、工具准备

工具：vscode\anaconda\git\python
![[Day1.png]]

vscode插件安装，python和git集成
`Ctrl+Shift+P`→ 输入 `Python: Select Interpreter`
**VS Code 设置**搜索 `git.path` 点击 ​**​“在 settings.json 中编辑”**

conda安装包
```
conda --version
conda create -n ai-python python=3.10
conda activate ai-python
```

git基础用法：
1.**查看状态​**​：
```
git status
```
2.**添加文件到暂存区​**​：​
```
git add file.txt    # 添加单个文件
git add .           # 添加所有新文件和修改（不含删除）
git add -A          # 添加所有变更（包括删除）
```
3.**​提交到本地仓库​**​：
```
git commit -m "描述修改内容"  # -m后接简明提交信息
```
4.**​推送到远程仓库​**​：
```
git push origin main  # 首次推送加`-u`关联分支：`git push -u origin main`
```

	注意环境配置，虚拟环境设置，工具用法基础掌握

---
### 2、python核心语法

- [x] 数据类型（list / dict / tuple / set）
- [x] 条件 & 循环
- [x] 函数（位置参数、关键字参数、可变参数）
- [x] 异常处理（try-except）
- [x] 模块导入（import）
- [x] 列表推导式 / 字典推导式

### 3、常用内置库
- `os`（目录与文件操作）
- `sys`（系统参数）
- `json`（读写 JSON）
- `re`（正则表达式）
- `datetime`（时间处理）

| 模块           | 常用方法                                                         | 说明            |
| ------------ | ------------------------------------------------------------ | ------------- |
| **os**       | `getcwd()`, `listdir()`, `mkdir()`, `rmdir()`, `path.join()` | 目录、文件操作       |
| **sys**      | `argv`, `version`, `path`, `exit()`                          | 系统参数、模块搜索路径   |
| **json**     | `dumps()`, `loads()`, `dump()`, `load()`                     | Python ↔ JSON |
| **re**       | `search()`, `findall()`, `sub()`, `match()`                  | 正则匹配/替换       |
| **datetime** | `now()`, `strftime()`, `strptime()`, `timedelta`             | 时间获取、格式化、计算   |
### 4、csv数据清理助手

实现功能如下：
1. 读取 `data.csv`
2. 去除空值 & 重复行
3. 按某一列排序
4. 输出到 `cleaned_data.csv`

```
import csv

def clean_csv(input_file,output_file):
    rows = []
    seen = set()
    with open(input_file,"r",encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if tuple(row) not in seen and all(row):
                seen.add(tuple(row))
                rows.append(row)
    rows.sort(key=lambda x:x[0])
    with open(output_file,"w",encoding="utf-8",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

if __name__=="__main__":
    clean_csv("2025-08-26_news.csv","cleaned_data.csv")
```

