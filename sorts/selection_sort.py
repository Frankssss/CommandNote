'''
Author: Frank Shen
Email: m13917334342.com
Data: 2019/10/8 19:16
'''


def selection_sort(collection):
    '''Pure implementation of the selection sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    '''
    length = len(collection)
    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            if collection[k] < collection[least]:
                least = k
        if least != i:
            collection[least], collection[i] = collection[i], collection[least]
    return collection


def test_selection_sort():
    import random
    unsorted = [i for i in range(10)]
    random.shuffle(unsorted)
    assert selection_sort(unsorted) == [i for i in range(10)]


if __name__ == '__main__':
    test_selection_sort()
