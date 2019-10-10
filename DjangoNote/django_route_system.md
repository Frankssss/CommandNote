# Django Route System

路由是指根据请求路径映射到对应处理程序的过程。

路由模型是指框架中定义的处理路由过程的策略，是路由过程实现的设计思想

namespace app_name name 含义
1. 代表的是命名空间
2. 保证逆向解析映射到唯一的URL

django中的三类路由映射模型
1. 普通url映射
	+ url和对应的处理器
2. 动态url映射
	+ url中包含动态可变的内容
3. 两级url映射
	+ url定义url文件路径指示的文件

app_name 应用命名空间
表示正在部署的应用的名称。一个应用的每个实例具有相同的应用命名空间
namespace 实例命名空间
表示应用的一个特定的实例， 实例的命名空间是唯一的，

path
返回URLPattern 如果接收的视图参数是可调用对象
返回URLResolver 如果接收的是tuple

include 
返回(urlconf_module, app_name, namespace) urlconf_module 为urlpatterns列表

URLResolver.resolve 返回ResolveMatch对象