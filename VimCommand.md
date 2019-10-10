
进入编辑模式（i, a, o）
1. a append
2. i insert
3. o open a line below
4. A append after line
5. I insrt before line
6. O append a line above

ESC 退出到normal模式

normal 模式下输入冒号进入命令模式 
+ :w保存
+ :q 退出
+ :vs（vertical split） :sp(split)

使用v进入Visual模式 进行批量操作
使用ctrl+v进行方块选择 输入d删除选中

快捷键
ctrl + h 删除上一个字符
ctrl + w 删除上一个单词
ctrl + u 删除当前行

ctrl + c代替ESC 或ctrl + [
 
快速删除
+ normal模式下快速删除
	x, 删除一个字符
	u 代表undo
	d dd删除行 dw 删除一个单词 daw 删除一个单词包含周围的空格 dt" 删除""内的单词 d$ 删除到行尾 d0 删除到行首
	v 开始选择

+ normal模式下快速修改
	r relace   ra 
	c change  caw ciw
	s substitute 替换并进入插入模式
+ normal模式下查询 
	
	