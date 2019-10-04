# GitCommand

> HEAD 关键字指当前分支末梢最新的一个提交

> branch  分支 一条线

> tag 标签 一个点

> git init   
>> 创建一个空的Git仓库或重新初始化一个现有仓库

> git add <file>  
>> 将工作区文件添加到暂存区

> git commit -m <message>  
>> 将暂存区的文件与描述提交到分支

> git add origin master <url>  
>> 添加远程仓库

> git remote rm origin   
>> 删除指定的远程

> git remote -v  
>> 列出所有的远程

> git clone <url>  
>> 克隆远程存储库

> git status  
>> 查看暂存区和工作区的状态

> git log  
>> 查看提交日志历史信息

> git diff <file>  
>> 对比工作区和暂存区文件的差异

> git diff HEAD -- <file>  
>> 查看工作区和版本库区别

> git diff --staged / git diff --cached  
>> 比较暂存区和版本库差异

> git reset HEAD <commit>  
>> 将当前分支HEAD复位到指定状态

> git reset --hard <commit>  
>> 将暂存区和工作区自上一次commit后的更改都丢弃， 并把HEAD指向<commit>

> git rm <file>  
>> 删除工作区和暂存区的文件

> git checkout -- <file>  
>> 将暂存区文件恢复到工作区

> git mv <source> <destination>  
>> 移动工作区文件

> git mv <filename> <filename>
>> 重命名工作区文件

> git branch  
>> 查看当前分支

> git branch <branchname>  
>> 创建分支

> git checkout <branchname>  
>> 切换到指定分支

> git checkout -b  <branchname>  
>> 创建并切换到分支

> git merge <branchname>  
>> 合并分支

> git branch -d <branchname>  
>> 删除分支

> git tag  
>> 查看所有标签

> git tag <name>  
>> 给当前分支添加标签

> git tag <name> <commit>  
>> 给提交历史加标签

> git tag -d name  
>> 删除标签

> git push origin name  
>> 标签发布

> git config --global alias.st status
>> 配置别名

