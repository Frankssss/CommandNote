# HtmlCommand

HTML����ҳ���ݵ�����
CSS��ʽ�Ǳ���
JavaScript������������ҳ�ϵ���ЧЧ��

<!DOCTYPE HTML> HTML5��׼��ҳ����

<html> ����ǩ  
	<head>...</head> ͷ����ǩ
	<body>...</body> ���ݱ�ǩ
</html>

<!--����ע�ͱ�ǩ-->

<head>
	<title>
	<script>
	<meta>
	<style>
	<link>
<body>
	<h1> �����ǩ
	<p>  �����ǩ
	<a>  ������ǩ   target="_blank �´��ڴ�  mailto �����ʼ���ַ <a href="mailto:yy@imooc.com?cc=1@1.com@bcc=1@1.com&subject=����&body=�ʼ�����"></a>
	<img> ͼƬ��ǩ  src ͼƬλ��  alt ͼƬ�������ı���ͼƬ���ɼ���ʾ�� title ͼƬ������ ����껬���� 
	<em> ǿ����ǩ  б��
	<strong> ����ǿ���ı�ǩ ���� 	
	<span> ��ǩû�����壬 ���õ�������ʽ
	<q> ���ı�����  ""
	<blockquote> ���ı����� 
	<br /> ���б�ǩ
	&nbsp; �ո��ǩ
	<hr />  ˮƽ�ָ��߱�ǩ
	<address> ��ַ��ǩ б��
	<code> ���д����ǩ
	<pre> ���д����ǩ 
	<ul><li> �б��ǩ ÿ��ǰ�Դ�һԲ��
	<ol><li> �����б��ǩ ÿ��ǰ�Դ����
	<div> ������ǩ 
	<table><thead><tbody><tfooter><tr> <th> <td> ����ǩ <table summary="">  Ϊ������ժҪ
	<caption> �������ǩ
	<form> ����ǩ  action�������ļ� method ���ݴ��͵ķ�ʽ 
	<input> ������ǩ  type ���� text �ı������ password ��������� radio ��ѡ�� checkbox ��ѡ�� submit �ύ��ť reset ���ð�ť name �ı������� value �ı���Ĭ��ֵ checked="checked"Ĭ��ѡ��  
	<option> ������ value �ύֵ selected="selected" Ĭ�ϱ�ѡ��  multiple="multiple" ���ö�ѡ
	<textarea> �ı��������ǩ   rows ����  cols ����
	<label> �ı���ǩ  ����ı� ���㴥������Ӧ�ı��ؼ�    <label for="">  for���Ե�ֵӦ������ؿؼ���id����ֵ��ͬ
id ��ǩ��Ψһ��ʶ

CSS ��ʽ���ڶ���HTML����������ڵ���ʾ��ʽ
CSS ��ʽ ѡ���������  ���������Ժ�ֵ���  ���������еĵľ������� ���Ժ�ֵ֮����Ӣ��ð�š������ָ������ж�������ʱ���м����Ӣ�ķֺš�;��
CSSע��  /* ������ע�� */

����ʽcss��ʽ  ֱ��д�����е�HTML��ǩ��
Ƕ��ʽCSS��ʽ д�ڵ�ǰ���ļ���  
<style type="text/css"></style>
�ⲿʽcss��ʽ д�ڵ������ļ��� ������   <link href="" rel="stylesheet" type="text/css">   
���ȼ� ����ʽ����Ƕ��ʽ�����ⲿʽ 

��ǩѡ���� h1 body h1 p img 
��ѡ����    class="stress" .stress{} 
IDѡ����   id="stress"    #stress{}

��ѡ������IDѡ���������� 
��ͬ�� ����Ӧ�����κ�Ԫ��
��ͬ�� 1.IDѡ�������ĵ���ʹ��һ��
	   2.����ʹ����ѡ�����б���Ϊһ��Ԫ��ͬʱ���ö����ʽ

��ѡ���� .food>li  ���ڷ�����ѡ���� 
���ѡ���� .first span �ո� 
> ������Ԫ�صĵ�һ������� �ո�������Ԫ�ص����к��

ͨ��ѡ���� *

α��ѡ���  �������html�����ڵı�ǩ����ǩ��ĳ��״̬��������ʽ
a:hover ��껮����״̬ 

����ѡ��� Ϊhtml�����ǩԪ������ͬһ����ʽ  h1,span{}

CSS��ĳЩ��ʽ ���м̳���  color     �����м̳��� border  solid

��ǩ��ȨֵΪ1�� ��ѡ������ȨֵΪ10�� IDѡ������Ȩֵ���Ϊ100

��� ��ͬȨ��ֵ����ǰ��˳��������  ����ĸ���ǰ���

������Ҫ�� p{color:red!important;}

�������� body{font-family:"Microsoft Yahei";}
�ֺš���ɫ body{font-size:12px;color:#666}
���ô��� p span{font-weight:bold;}
����б�� font-style:italic
�»��� text-decoration:underline;
ɾ���� text-decoration:line-througn;
���� text-index:2em
�м�� line-height:1.5em
������ĸ��� letter-spcing:50px
���ʼ��  word-spcing:50px
����  text-align:center  text-align:left   right  

Ԫ�ط��� 
��״Ԫ�� 
	div p h1-h6 ol ul dl table address blockquote form
����Ԫ�� 
	a span br i em strong label q var cite code 
������״Ԫ��
img input

����display:block ��Ԫ����ʾΪ��״Ԫ�� 

��״Ԫ���ص�
1.ÿ����״Ԫ�ش��µ�һ�п�ʼ�� ���ҵ�Ԫ��Ҳ����һ��
2.Ԫ�صĸ߶ȡ���ȡ��и��Լ����͵ױ߾඼������
3.Ԫ�ؿ���ڲ����õ������������������100% 

����display:inline��Ԫ����ʾΪ����Ԫ��

����Ԫ���ص㣺
1.������Ԫ�ض���һ����
2.Ԫ�صĸ߶ȡ�����Լ������͵ײ��߾಻������
3.Ԫ�صĿ�Ⱦ����������������ֻ�ͼƬ�Ŀ�� ���ɸı�

����display;inline-block ��Ԫ������Ϊ������״Ԫ�� 

������״Ԫ���ص�
1.������Ԫ�ض���һ����
2.Ԫ�صĸ߶ȣ���ȣ��иߣ��Լ����͵ױ߾඼������

�鼫��ǩ�����к���ģ�͵��ص�
�ڱ߾� padding ��߾� margin  �߿� border
	padding-left padding-right  padding-top padding-bottom
	
margin ��ı߿��������Ŀհ�
background-color ������ɫ
background-image ����ͼƬ
padding ��ı߿򵽲������֮��Ŀհ�
border �߿�
content ����
���Ĭ��˳�� �ϡ��ҡ��¡���   ����һ�¿�ʡ���� ����һ�¿�ʡ����
	
�߿���ʽ  border-width:2px;border-style:solid;border-color:red;

����ģ�� 
1.����ģ�� ��Flow��
2.����ģ�� ��Float��
3.��ģ�� ��Layer��

��������ģ������
1.��״Ԫ�ض����������İ���Ԫ�������϶��°�˳��ֱ����ֲ�
  ��Ϊ��Ĭ��״̬�£���״Ԫ�صĿ�ȶ�Ϊ100%�� ʵ���� ��״Ԫ�ض������е���ʽռ��λ�á�
2.������ģ���£�����ģ�Ͷ����������İ���Ԫ���ڴ�����ˮƽ�ֲ���ʾ

����ģ�� float:left 

��ģ�� ������ʽ 
1.���Զ�λ position:absolute
2.��Զ�λ position:relative
3.�̶���λ position:fixed

Relative Absoulte���ʹ�� �������Ԫ�ؽ��ж�λ
1.���ն�λ��Ԫ�ر�������Զ�λԪ�ص�ǰ��Ԫ��
2.���ն�λ��Ԫ�ر������position:relatve
3.��λԪ�ؼ��� position:absolute

��ɫֵ��д 
ÿ��λ��ֵ��ͬ��������дһ�� #000000 #000 #336699 #369
��ɫ������ɫ color:red
RGB��ɫ color:rgb(133, 45, 200)
ʮ��������ɫ color:#00ffff

����ֵ   px(����)�� em�� % �ٷֱ� ��Ե�λ
����ָ������ʾ���ϵ�һ��С��
em ���Ǹ�����font-sizeֵ    �����font-size���õ�λΪemʱ�� ���Ը�Ԫ�ص�font-sizeΪ����
�ٷֱ� �����и�Ϊ�����130%   font-size:12px;line-height:130%

����ˮƽ���У�
����Ԫ��  ���������Ԫ��Ϊ�ı���ͼƬ������Ԫ��ʱ�� ˮƽ����ʱͨ������Ԫ������text-align:center��ʵ�ֵ�
�����״Ԫ�أ�widthΪ�̶�ֵ��  margin: auto <=>  margin-left:auto;margin-right:auto;
�������״Ԫ�� 
	1.����table��ǩ ����table��ǩ�ĳ�������Ӧ��
	2.����display;inline ��ʾ����Ϊ����Ԫ��
	3.����position:relative��left:50%  
	
���ô�ֱ���У�
�����ı�  ���ø�Ԫ�ص�height��line-height�߶�һ����ʵ�ֵ� 

���Ըı�display���� 
1.position:absolute
2.float:left or float:right 
Ԫ�ص�display��ʾ�����Զ���Ϊ display:inline-block









