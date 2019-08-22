
# 逻辑运算符and or 短路原则
# 当逻辑运算表达式含有False对象， 逻辑运算结果返回False类型本身
# print(True and 2)

# 装饰器实现单例
def singleton(cls):
    _instance = {}
    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner

