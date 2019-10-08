__author__ = 'Frank Shen'


def bubble_sort(collection):
    """Pure implementation of bubble sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    """

    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break
    return collection


def test_bubble_sort():
    import random
    unsorted = [i for i in range(10)]
    random.shuffle(unsorted)
    assert bubble_sort(unsorted) == [i for i in range(10)]


if __name__ == '__main__':
    test_bubble_sort()