'''
Author: Frank Shen
Email: m13917334342@163.com
Date: 2019/10/6 15:55
'''

# functools.partial
# partial() 是被用作 “冻结” 某些函数的参数或者关键字参数，同时会生成一个带有新标签的对象(即返回一个新的函数)。

from functools import partial


def add(*args):
    return sum(args)


func = partial(add, 100)
print(func(1, 2, 3))


# lambda [arg1 [,arg2,.....argn]]:expression

func = lambda x, y: x+y
print(func(1, 2))


# sorted key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
print(sorted([{'age': 1, 'name': 'Frank'}, {'age': 2, 'name': 'Jark'}], key=lambda x: x['age'], reverse=True))


