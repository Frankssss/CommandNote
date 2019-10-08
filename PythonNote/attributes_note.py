'''
Author: Frank Shen
Email: m13917334342.com
Data: 2019/10/8 18:21
'''


# __getitem__, __setitem__, __delitem__ 用于列表下标操作

'''
对象属性获取
getattr(obj, name) 从object对象中获取name字符串对应的属性  获取的属性来自对象所属的类或超类 触发 __getattribute__()方法  获取属性失败触发__getattr__方法
hasattr(obj, name) 如果object对象中存在指定的属性，返回True
setattr(obj, name, value) 给object对象新建或覆盖一个新属性  触发__setattr__
vars(object) 返回对象的__dict__属性 返回对象内部存储的所有属性名和属性值组成的字典 直接通过__dict__属性读写属性不会触发特殊方法  
del obj.attr 触发 __delattr__
'''
