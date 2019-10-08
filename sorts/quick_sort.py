__author__ = 'Frank Shen'


def quick_sort(collection):
    '''Pure implementation of quick sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable item inside
    :return:  the same collection ordered by ascending
    '''
    length = len(collection)
    if length <= 1:
        return collection
    else:
        pivot = collection.pop()
        greater, lesser = [], []
        for elem in collection:
            if elem > pivot:
                greater.append(elem)
            else:
                lesser.append(elem)
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


def test_quick_sort():
    import random
    unsorted = [i for i in range(10)]
    random.shuffle(unsorted)
    assert quick_sort(unsorted) == [i for i in range(10)]


if __name__ == '__main__':
    test_quick_sort()