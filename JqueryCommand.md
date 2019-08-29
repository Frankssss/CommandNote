$(document).ready 的作用是等页面的文档（document）中的节点都加载完毕后，再执行后续的代码

jQuery对象自身提供一个.get() 方法允许我们直接访问jQuery对象中相关的DOM节点
div = $('dvi).get(0)

var div = document.getElementsByTagName('div');
var $div = $(div);

id选择器 $("#id") 
类选择器 $(".class")
元素选择器 $("p")
全选择器 $("*")
层级选择器 
	$("parent > child") 子选择器   
	$("ancestor descendant") 后代选择器 
	$("prev + next") 相邻兄弟选择器
	$("prev ~ sublings") 一般兄弟选择器
	
