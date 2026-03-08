# 1. 初始化 Git 仓库（如果之前没做过）
git init

# 2. 将你的所有代码添加到暂存区
git add .

# 3. 提交代码到本地仓库，并附上备注信息
git commit -m "第一次提交：我的 PySpark 学习代码"

# 4. 关联远程 GitHub 仓库（地址就是你截图里的那个）
git remote add origin https://github.com/zhanghaoshan-star/python_practice.git

# 5. 将本地代码推送到 GitHub 的 main 分支
git push -u origin master

git config --global user.name "zhanghaoshan-star"
git config --global user.email "s_stimmen@163.com"

# 二、日常操作
# 1. 查看当前有哪些文件被修改了
git status

# 2. 添加所有修改的文件
git add .

# 3. 提交并写备注
git commit -m "更新了什么内容"

# 4. 推送到 GitHub
git push



📝 各种场景的命令大全
场景一：第一次上传新项目
bash
git init                    # 初始化仓库
git add .                   # 添加所有文件
git commit -m "第一次提交"   # 提交
git remote add origin 地址   # 连接远程仓库
git push -u origin master   # 推送到 GitHub
场景二：日常更新代码（最常用）
bash
git add .                   # 添加所有修改
git commit -m "更新了xx功能" # 提交
git push                    # 推送
场景三：只添加某个文件
bash
git add first.py            # 只添加 first.py 文件
git commit -m "修改了first.py"
git push
场景四：查看历史
bash
git status                  # 查看当前状态（哪些文件改了）
git log                     # 查看提交历史
git log --oneline           # 简洁版历史
场景五：如果出错了想撤销
bash
# 还没 git add 时
git checkout -- 文件名       # 撤销某个文件的修改

# 已经 git add 但没 commit
git reset HEAD 文件名        # 取消添加

# 已经 commit 但没 push
git reset --soft HEAD~1     # 撤销最后一次提交，保留修改
🎯 你以后的标准流程
bash
# 1. 写代码前，先拉取最新的（如果是多人协作）
git pull

# 2. 写代码...

# 3. 写完后，查看修改了哪些文件
git status

# 4. 添加所有修改
git add .

# 5. 提交（备注要写清楚改了啥）
git commit -m "添加了xxx功能"  # 或者 "修复了xxxbug"

# 6. 推送到 GitHub
git push
✅ 常用命令速查表
命令	作用	使用频率
git status	查看当前状态	⭐⭐⭐ 每次都用
git add .	添加所有修改	⭐⭐⭐ 每次都用
git commit -m "备注"	提交修改	⭐⭐⭐ 每次都用
git push	推送到 GitHub	⭐⭐⭐ 每次都用
git pull	拉取最新代码	⭐⭐ 多人协作用
git log	查看历史	⭐ 偶尔用
git branch	查看分支	⭐ 偶尔用
💡 小技巧
备注要写清楚：git commit -m "修复了登录bug" 比 git commit -m "更新" 好

先 status 后操作：每次操作前先 git status 看看

如果 push 失败：可能是别人先推送了，先 git pull 再 git push