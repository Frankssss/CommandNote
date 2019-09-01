# HtmlCommand

HTML是网页内容的载体
CSS样式是表现
JavaScript是用来表现网页上的特效效果

<!DOCTYPE HTML> HTML5标准网页声明

<html> 根标签  
	<head>...</head> 头部标签
	<body>...</body> 内容标签
</html>

<!--这是注释标签-->

<head>
	<title>
	<script>
	<meta>
	<style>
	<link>
<body>
	<h1> 标题标签
	<p>  段落标签
	<a>  超链标签   target="_blank 新窗口打开  mailto 链接邮件地址 <a href="mailto:yy@imooc.com?cc=1@1.com@bcc=1@1.com&subject=主题&body=邮件内容"></a>
	<img> 图片标签  src 图片位置  alt 图片描述性文本（图片不可见显示） title 图片的描述 （鼠标滑过） 
	<em> 强调标签  斜体
	<strong> 更加强调的标签 粗体 	
	<span> 标签没有语义， 设置单独的样式
	<q> 短文本引用  ""
	<blockquote> 长文本引用 
	<br /> 换行标签
	&nbsp; 空格标签
	<hr />  水平分割线标签
	<address> 地址标签 斜体
	<code> 单行代码标签
	<pre> 多行代码标签 
	<ul><li> 列表标签 每项前自带一圆点
	<ol><li> 有序列表标签 每项前自带序号
	<div> 容器标签 
	<table><thead><tbody><tfooter><tr> <th> <td> 表格标签 <table summary="">  为表格添加摘要
	<caption> 表格标题标签
	<form> 表单标签  action服务器文件 method 数据传送的方式 
	<input> 输入框标签  type 类型 text 文本输入框 password 密码输入框 radio 单选框 checkbox 复选框 submit 提交按钮 reset 重置按钮 name 文本框命名 value 文本框默认值 checked="checked"默认选中  
	<option> 下拉框 value 提交值 selected="selected" 默认被选中  multiple="multiple" 设置多选
	<textarea> 文本输入域标签   rows 函数  cols 列数
	<label> 文本标签  点击文本 焦点触发到相应的表单控件    <label for="">  for属性的值应当与相关控件的id属性值相同
id 标签的唯一标识

CSS 样式用于定义HTML内容在浏览内的显示样式
CSS 样式 选择符和声明  声明有属性和值组成  ”｛｝”中的的就是声明 属性和值之间用英文冒号“：”分隔。当有多条声明时，中间可以英文分号“;”
CSS注释  /* 这里是注释 */

内联式css样式  直接写在现有的HTML标签中
嵌入式CSS样式 写在当前的文件中  
<style type="text/css"></style>
外部式css样式 写在单独的文件中 在引用   <link href="" rel="stylesheet" type="text/css">   
优先级 内联式大于嵌入式大于外部式 

标签选择器 h1 body h1 p img 
类选择器    class="stress" .stress{} 
ID选择器   id="stress"    #stress{}

类选择器和ID选择器的区别 
相同点 可以应用于任何元素
不同点 1.ID选择器在文档中使用一次
	   2.可以使用类选择器列表方法为一个元素同时设置多个样式

子选择器 .food>li  大于符号链选择器 
后代选择器 .first span 空格 
> 作用于元素的第一代后代， 空格作用于元素的所有后代

通用选择器 *

伪类选择符  它允许给html不存在的标签（标签的某种状态）设置样式
a:hover 鼠标划过的状态 

分组选择符 为html多个标签元素设置同一个样式  h1,span{}

CSS的某些样式 具有继承性  color     不具有继承性 border  solid

标签的权值为1， 类选择器的权值为10， ID选择器的权值最高为100

层叠 相同权重值根据前后顺序来决定  后面的覆盖前面的

设置重要性 p{color:red!important;}

设置字体 body{font-family:"Microsoft Yahei";}
字号、颜色 body{font-size:12px;color:#666}
设置粗体 p span{font-weight:bold;}
设置斜体 font-style:italic
下划线 text-decoration:underline;
删除线 text-decoration:line-througn;
缩进 text-index:2em
行间距 line-height:1.5em
中文字母间距 letter-spcing:50px
单词间距  word-spcing:50px
对齐  text-align:center  text-align:left   right  

元素分类 
块状元素 
	div p h1-h6 ol ul dl table address blockquote form
内联元素 
	a span br i em strong label q var cite code 
内联块状元素
img input

设置display:block 将元素显示为块状元素 

块状元素特点
1.每个块状元素从新的一行开始， 并且的元素也另起一行
2.元素的高度、宽度、行高以及顶和底边距都可设置
3.元素宽度在不设置的情况下是它父容器的100% 

设置display:inline将元素显示为内联元素

内联元素特点：
1.和其他元素都在一行上
2.元素的高度。宽度以及顶部和底部边距不可设置
3.元素的宽度就是它所包含的文字或图片的宽度 不可改变

设置display;inline-block 将元素设置为内联块状元素 

内联块状元素特点
1.和其他元素都在一行上
2.元素的高度，宽度，行高，以及顶和底边距都可设置

块极标签都具有盒子模型的特点
内边距 padding 外边距 margin  边框 border
	padding-left padding-right  padding-top padding-bottom
	
margin 层的边框以外留的空白
background-color 背景颜色
background-image 背景图片
padding 层的边框到层的内容之间的空白
border 边框
content 内容
填充默认顺序 上、右、下、左   上下一致可省略下 右左一致可省略左
	
边框样式  border-width:2px;border-style:solid;border-color:red;

布局模型 
1.流动模型 （Flow）
2.浮动模型 （Float）
3.层模型 （Layer）

流动布局模型特征
1.块状元素都会在所处的包含元素内自上而下按顺序垂直延伸分布
  因为在默认状态下，块状元素的宽度都为100%， 实际上 块状元素都会以行的形式占据位置。
2.在流动模型下，内联模型都会在所处的包含元素内从左到右水平分布显示

浮动模型 float:left 

层模型 三种形式 
1.绝对定位 position:absolute
2.相对定位 position:relative
3.固定定位 position:fixed

Relative Absoulte组合使用 相对其他元素进行定位
1.参照定位的元素必须是相对定位元素的前辈元素
2.参照定位的元素必须加入position:relatve
3.定位元素加入 position:absolute

颜色值缩写 
每两位的值相同，可以缩写一般 #000000 #000 #336699 #369
颜色命令颜色 color:red
RGB颜色 color:rgb(133, 45, 200)
十六进制颜色 color:#00ffff

长度值   px(像素)、 em、 % 百分比 相对单位
像素指的是显示器上的一个小点
em 就是给定的font-size值    如果给font-size设置单位为em时， 则以父元素的font-size为基础
百分比 设置行高为字体的130%   font-size:12px;line-height:130%

设置水平居中：
行内元素  如果被设置元素为文本、图片等行内元素时， 水平居中时通过给父元素设置text-align:center来实现的
定宽块状元素（width为固定值）  margin: auto <=>  margin-left:auto;margin-right:auto;
不定宽块状元素 
	1.加入table标签 利用table标签的长度自适应性
	2.设置display;inline 显示类型为行内元素
	3.设置position:relative和left:50%  
	
设置垂直居中：
单行文本  设置父元素的height和line-height高度一致来实现的 

隐性改变display类型 
1.position:absolute
2.float:left or float:right 
元素的display显示类型自动变为 display:inline-block









