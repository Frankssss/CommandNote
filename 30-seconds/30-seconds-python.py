__author__ = "Frank Shen"


def all_equals(lst):
    ''' check if all element in a list are equal
    :param lst:
    :return:
    '''
    return lst[1:] == lst[:-1]


print(all_equals([1, 2, 3]))
print(all_equals([1, 1, 1]))


def all_unique(lst):
    '''return true if all the values in a flat list are unique, otherwise return false
    :param lst:
    :return:
    '''
    return len(lst) == len(set(lst))


print(all_unique([1, 2, 3]))
print(all_unique([1, 1, 1]))


def has_duplicates(lst):
    '''return false if there are duplicate values in a flat list, false otherwise
    :param lst:
    :return:
    '''
    return len(lst) != len(set(lst))


print(has_duplicates([1, 2, 3]))
print(has_duplicates([1, 1, 1]))


def flatten(lst):
    '''flatten a list of lists once
    :param lst:
    :return:
    '''
    return [x for y in lst for x in y]


print(flatten([[1, 2, 3, 4], [5, 6, 7, 8]]))


def head(lst):
    '''return the head of a list
    :param lst:
    :return:
    '''
    return lst[0]


print(head([1, 2, 3]))


def difference(a, b):
    '''return difference between two iterables
    :param lst:
    :return:
    '''
    _b = set(b)
    return [item for item in a if item not in _b]


print(difference([1, 2, 3], [1, 2]))


from copy import deepcopy
from random import randint


def shuffle(lst):
    '''randomizes the order of the values of an list, returning a new list
    :param lst:
    :return:
    '''
    temp_lst = deepcopy(lst)
    m = len(temp_lst)
    while m:
        m -= 1
        i = randint(0, m)
        temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
    return temp_lst


print(shuffle([1, 2, 3, 4, 5]))


from re import sub
def camel(s):
    '''converts a string to camelcase
    :param s:
    :return:
    '''
    s = sub(r'(\s|-|_)+', ' ', s).title().replace(' ', '')
    return s[0].lower() + s[1:]


print(camel('hello_world'))
print(camel('hello world'))
print(camel('hello\r\nworld'))


from re import sub
def palindrome(s):
    '''returns true if the given string is palindorme, false otherwise
    :param s:
    :return:
    '''
    s = sub('[\W_]', '', s.lower())
    return s == s[::-1]


print(palindrome('1234_@4321'))


def byte_size(s):
    '''return the length of a string in bytes
    :param s:
    :return:
    '''
    return len(s.encode('utf8'))


print(byte_size('123'))
print(byte_size('呵呵'))
