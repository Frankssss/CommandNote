
# 逻辑运算符and or 短路原则
# 当逻辑运算表达式含有False对象， 逻辑运算结果返回False类型本身
# print(True and 2)

# classonlymethod 修饰的方法只能被类调用
# classmethod 可以被一个实例或类调用

# 在密码学中，是指通过在密码任意固定位置插入特定的字符串，让散列后的结果和使用原始密码的散列结果不相符，这种过程称之为“加盐”。

# 装饰器实现单例
def singleton(cls):
    _instance = {}
    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner

