# DjangoNote

+ Django2.0与1.11区别
	+ 路由的编写方式右正则改为简单的path表达式 同时通过re_path向上兼容
	+ 外键要加上on_delete参数
	+ ...
	
+ 设置环境变量
	+ import os
	+ os.environ['DJANGO_SETTINGS_MODULE'] = 'Blog.settings'

+ 在python解释器设置Django shell
	+ import django
	+ django.setup()
	
+ DJANGO 路由匹配中路由分发（include） 集中又分治 解耦
	+ URL取别名name参数 可以反向解析URL， 反向URL匹配   反向URL查询 URL反查
		+ 视图中 reverse('name')
		+ 模板中 {% url 'name' %}
		+ orm get_absolute_url
	+ URL命名空间可以保证反查到唯一的URL
		+ 应用命名空间 区分多个app app_name = "app_name"
		+ 实例命名空间 一个app开以创建多个实例， 可以使用多个URL映射到同一个app  namespace=""
		+ 注意： 在使用实例命名空间之前，必须先指定一个应用命名空间

+HTTP
	+HTTP请求方法
		+GET请求特定的路径资源
		+POST向指定路径资源提交数据
		+OPTIONS 1.获取服务器支持的HTTP请求方法 2.用来检查服务器的性能
		+DELETE请求删除指定资源
		+PUT请求更新指定资源
		+HEAD
		+TARCE
	+GETPOST区别
		+本质
			+GET是请求特定的路径资源
			+POSt是向指定路径资源提交数据
		+request提交数据方式
			+GET方法将用户提交数据已key=value的形式，以&符号组合在一起成为一个整体字符串， 最后添加前缀？最后将字符串拼接到URL。
			+POST方法将组合表单数据对它们进行编码，打包发送
		+GET安全性低而POST安全性高隐私性好但是POST执行效率比GET低一些
		+传输数据大小
			HTTP协议规范没有对URL长度进行限制，也没有对传输的数据大小进行限制，
			但是特定浏览器和服务器对URL长度有限制，如IE对URL长度限制是2083字节,		
	+Httpstatuscode
		+400badrequest
		+403httpforbidden
		+500servererror
		+404pagenotfound
		

Fields 负责验证输入并直接在模板中使用 widget 负责渲染网页上HTML表单的输入元素和提取提交的原始数据
	








+请求生命周期
	1web服务器（wsgi）请求封装后交给web框架
	2中间件，对请求进行校验或在请求对象中添加其他相关数据
	3路由匹配
	4视图函数
	5中间件对响应的数据进行处理
	6web服务器(wsgi)将响应的内容发送给浏览器
		
+Django查找文件是惰性查找从上而下的短路操作
	+MEDIA_ROOT
	+django查找template文件的方法
	+静态文件
		+STATIC_ROOT是在部署静态文件时所有的静态文件聚合目录绝对地址
		+STATICFILES_DIRS先到STATICFILES_DIRS设定的目录寻找静态文件，其次再到各个app的static文件夹里面查找
		+STATIC_URL
			+利用前缀static_url来映射STATIC_ROOT,STATIC_URL用于引用STATIC_ROOT所指向的静态文件
			+通过模板标签static和给定的相对路径来构成一个URL{%loadstatic%}
		+MEDIA_ROOTsetupload_topath
		+MEDIA_URL通过模板标签和给定的相对路径构建URL

+Django缓存
	+缓存方式
		+全局缓存粒度大
			```	
			MIDDLEWARE[
				'djangomiddlewarecacheUpdateCacheMiddleware',
				
				'djangomiddlewarecacheFetchFromCacheMiddleware',
			]
			```
		+视图缓存粒度适中
			@cache_page(60)
		+模板缓存粒度小
			```
			{%loadcache%}
			{{now}}
			{%cache60key%}
				{{now}}
			{%endcache%}
			```
	
	+文件缓存即硬盘缓存，数据库连接是socket通信，速度不如本地文件块，且数据库数据还需要渲染
		```
		CACHES{
			'default':{
				'BACKEND':'djangocorecachebackendsfilebasedFileBasedCache',
				'LOCATION':'D:\cache',
				}
		}
		```
	+数据库缓存:存储好的是渲染好的字符串,使用前创建缓存表pythonmanagepycreatecachetable
		```
		CACHES{
			'default':{
				'BACKEND':'djangocorecachebackendsdbDatabaseCache',
				'LOCATION':'my_cache_table',
			}
		}
		```
	+Redis缓存
		```
		CACHES{
			'default':{
				'BACKEND':'django_rediscacheRedisCache',
				'LOCATION':'redis:127001:6379',
				OPTIONS:{
					CLIENT_CLASS:django_redisclientDefaultClient,
				},
			},
		}
		```

+cookie与Session
	+数据安全
		+cookie暴露在浏览器端，数据不安全
			```
			set_cookie(self,key,value'',max_ageNone,expiresNone,path'/',
						domainNone,secureFalse,httponlyFalse,samesiteNone)
			```
		+session基于cookie数据保存在服务端，客户端只存sessionid安全
			```
			requestsessionusername
			```
	+大小
		+cookie在客户端存储值有大小的,大约几KB,session没有限制


+csrf机制
	+用户请求页面，服务端产生一个随机字符串作为token值，保存在Session表，同时将这个token值放到cookie中传给浏览器
	+用户向指定路径资源提交数据会带着有token值的cookie，服务器校验用户传过来的cookie中的token值与session中的token值是否一致		
		
+djangomigrations机制:
	+makemigrations
		+比对models里面的model与migrations代码里的model对比，如果有新的修改，就生成新的migrations代码
	+migrate
		+将相关的迁移脚本翻译成SQL语句，在数据库中执行这个SQL语句
		+如果SQL执行成功，将迁移脚本的名字记录到django_migrations中
	+migrate怎么判断哪些迁移脚本需要执行
		+比对代码中的迁移脚本和数据库中django_migrations中的迁移脚本进行对比，如果数据库中没有这个迁移脚本，那么就会执行这个迁移脚本
	+执行migrate命令报错解决办法
		+找到不同的迁移脚本使用fake将代码中的迁移脚本添加到django_migrations但是不会执行sql
		+终极解决方案，删除数据库以及代码所有迁移文件重新makemigrations最后migratefakeinitial不会执行sql
		

+url补全slash
	+末尾带斜杠默认为目录，返回目录下的默认首页
	+末尾不带斜杠，默认为文件，首先会查找文件，找不到文件会自动的读取根目录下的default文件，因此可能会多一次判断的过程

+html转义：将html关键字(包括标签，特殊字符等)进行过滤替换
+
+django中的转义https:wwwcnblogscom/MnCu8261/p/5903225html

+管道符|可将其视为各命令间传递信息的管道，用来将某个命令或程序的输出提供给另一个命令或程序

+django模板标签本质上也是函数，标签名一般即为函数，主要作用包括载入代码渲染模板或对传递过来的参数进行一定的逻辑判断或计算后返回
	+django模板标签分类
		+simple_tag简单标签处理数据,返回一各字符串或者给context设置或添加变量
		+inclusion_tag包含标签处理数据返回一个渲染过的模板

+url和path区别命名捕获组(P<name>pattern)name:分组名;pattern:正则表达式

+modelmeta
	+abstract定义当前模型类是不是抽象类，抽象类不会实例化，不会对应数据库表
	+app_label指定模型类所属包
	+db_table自定义数据库表名
	+db_tablespace定义数据库表空间
	+get_latest_by指定最近一条记录是按照哪个field
	+managed不自动生成映射的数据库表
	+ordering指定字段排序
	+order_with_respect_to
	+permissions
	+verbose_name模型类的名字
	+verbose_name_plural模型复数名字

+反射说的是在运行状态中，对于任何一个类，我们都能够知道这个类有哪些方法和属性
+CBVgetattr反射
+FBVCBV区别
	+CBV提高了代码的重复性
	+CBV增加了代码的可读性
	+CBV比FBV更面对对象更多态Mixin
	+CBV添加装饰器@method_decorator(func)csfttoken装饰起只能加到dispatch
		1直接添加到Dispatch上，这样每个函数都会执行
		2添加到每一个函数上
		3直接添加到类上，后面的name表示被装饰的方法
	
+include路由转发集中又分治亦是一种解耦的方式

+gunicron

+render将给定的模板与给定的上下文字典组合在一起，并以渲染的文本返回一个HttpResponse对象

+redirect将一个HttpResponseRedirect返回到传递的参数的适当URL
	+HttpResponseRedirect只支持硬编码
	+redirect根据对象obj重定向，根据视图重定向
		+obj重定向模型定义了get_absolute_urlredirect会自动调用
		+视图重定向？？？？？？？https:blogcsdnnet/bluishglc/article/details/7953614
+reverseurl反向解析

+MTV保证了各组件间的松散耦合

+ORMObjectRelationMapping对象关系映射
	+优势
		1面向对象编程
		2实现了数据模型与数据库的解耦，屏蔽了不同数据库之间的差异

+中间件及其作用
	+中间件是一个用来处理Django的请求和响应的框架级别的钩子，它是一个轻量、低级别的插件系统，用于在全局范围内改变Django的输入和输出。

+中间件五个方法：
+Request预处理函数process_request
	+View预处理函数process_view
	+Template模板渲染函数process_template_response(默认不执行，只有在视图函数的返回结果对象中有render方法才会执行)
	+Exception后处理函数process_exception（View函数抛出未被捕获的异常时才会被调用）
	+Response后处理函数process_response
	
+中间件流程
	+processrequest（url匹配前View未知）如果返回None继续request返回HttpResponse直接执行当前middleware的process_response并返回
	+url匹配获得视图函数名称和参数
	+processview（View函数执行前，View已知）如果返回None继续返回HttpResponse直接返回
	+view（View函数执行后并且生成了Response对象）

+信号：django中提供了信号调度，用于在框架执行操作中解耦

+django中实现原生SQL

+路由匹配原则
	+如果第一条和第二条同时满足匹配规则，优先匹配第一条
	+如果第一为正则模糊匹配，第二条为精确匹配，优先匹配第一条
	

+解耦解除类之间的关系

+rest_framework

+解决跨域的常用方式

+信号的作用

+queryset什么情况下用Q

+on_deletemodelscascade级联删除on_updatemodelsmodelscascade级联更新
+当你更新或删除主键表，外键表也会跟随一起更新或删除

+orm取消级联
	+usermodelsForeignKey(User,blankTrue,nullTrue,on_deletemodelsSET_NULL)

+查询集的两大特性，什么是惰性执行

+查询集返回的列表过滤器有哪些
	+all返回所有数据
	+filter返回满足条件的数据
	+exclude返回满足条件之外的数据
	+order_by排序
	


+null与blank区别
	+null是针对数据库而言，如果nullTrue,表述数据库中的该字段可以违抗
	+blank是针对表单的，如果blankTrue表明表单填写该字段的时候可以为空

+Tornado的核是什么


	
			
+WSGIuwsgiuWSGI区分

+django使用原生SQL
	1
	```
	fromdjangodbimportconnection
		cursorconnectioncursor
		cursorexecute(insertintoblogapp_tag(name)values('tag2'))
	```
	2tagsTagobjectsraw('selectfromblogapp_tag')
	
+Django中查询queryset时什么情况下用Q

+django中的model的继承有几种形式

+ormcodefirstdbfirst

+模型的继承
	+抽象基类
		+继承meta子类abstractfalse没有管理器
	+多表继承
		+orderingget_latest_by会被继承
	+代理模型
		+约束
			+代理模型必须继承自一个非抽象的基类，并且不能同时继承多个非抽象基类
			+代理模型可以同时继承任意多个抽象基类，前提是这些抽象基类没有定义任何模型字段
			+代理模型可以同时继承多个别的代理模型，前提是这些代理模型继承同一个非抽象激烈
		+代理模型会继承父类的管理器
		
	
+抽象基类（Abstractbaseclass）：抽象基类就是类里定义了纯虚成员函数的类。纯虚函数只提供了接口，并没有具体实现
+抽象基类不能被实例化（不能创建对象），通常是作为基类供子类继承，子类中重写虚函数，实现具体的接口。
+简言之，ABC描述的是至少使用一个纯虚函数的接口，从ABC派生出的类将提供派生类的具体特征，使用常规虚函数来实现这种接口
+虚函数：程序在运行的时候动态的选择合适的成员函数
+多表继承就是各个子类有单独的表，但是通过父类来共享通用的方法

+多重继承和多表继承

+钩子

+django提供的反向解析URL工具
	+模板url
	+视图reverse
	+模型get_absolute_url
	
	+URL命名空间可以保证反查到唯一的URL
	
+app_namenamespace区别
	+app_name应用命名空间：表示正在部署的应用的名称
	+namespace实例命名空间：表示应用的一个特定的实例，根据实例在进行代码服用
	
quick
	
+djangocommand
	+djangoadmincommand
		+djangoadminckeckapp检查django项目有没有常见问题
		+
	+pythonmanagepycommand
	+pythonmdjangocommand