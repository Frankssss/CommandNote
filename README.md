# GitCommand

HEAD 关键字指当前分支末梢最新的一个提交

git init 
创建一个空的Git仓库或重新初始化一个现有仓库

git add <file>
将工作区文件添加到暂存区

git commit -m <message>
将暂存区的文件与描述提交到分支

git add origin master <url>
添加远程仓库

git clone <url> 
克隆远程存储库

git status 
查看暂存区和工作区的状态

git log
查看提交日志历史信息

git diff <file>
对比工作区和暂存区文件的差异

git diff HEAD -- <file>
查看工作区和当前分支最新提交区别

git reset HEAD <commit>
将当前分支HEAD复位到指定状态

git reset --hard <commit>
将暂存区和工作区自上一次commit后的更改都丢弃， 并把HEAD指向<commit>

git rm <file>
删除工作区和暂存区的文件

git checkout -- <file>
将暂存区文件恢复到工作区

git mv <source> <destination>
移动工作区文件

git branch
查看当前分支

git branch <branchname>
创建分支

git checkout <branchname>
切换到指定分支

git checkout -b  <branchname>
创建并切换到分支

git merge <branchname>
合并分支

git branch -d <branchname>
删除分支

