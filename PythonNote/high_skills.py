'''
Author: Frank Shen
Email: m13917334342.com
Data: 2019/10/8 18:38
'''

# *args means Uncertainty of quantitative parameters

# merge tuple  use *args and tuple unpacking
t1, t2 = (1, 2), (3, 4)
t = (*t1, *t2)
assert t == (1, 2, 3, 4)

# merge dict
d1, d2 = {1: 'a', 2: 'b'}, {3: 'c', 4: 'd'}
d = {**d1, **d2}
assert d == {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# or and 短路原则
response = False
func = lambda: print('temp')
response = response or func()

# switch in dict


def switcher(argument):
    data = {
        0: 'zero',
        1: 'one',
        2: 'two'
    }
    return data.get(argument, 'nothing')


print(switcher(0))


