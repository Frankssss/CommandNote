__author__ = 'Frank Shen'


def insertion_sort(collection):
    '''Pure implementation of the insertion sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    '''
    length = len(collection)
    for loop_index in range(0, length - 1):
        insertion_index = loop_index
        while (
            insertion_index >= 0
            and collection[insertion_index] > collection[insertion_index + 1]
        ):
            collection[insertion_index], collection[insertion_index + 1] = (
                collection[insertion_index + 1],
                collection[insertion_index]
            )
            insertion_index -= 1
    return collection


def test_insertion_sort():
    import random
    unsorted = [i for i in range(10)]
    random.shuffle(unsorted)
    assert insertion_sort(unsorted) == [i for i in range(10)]


if __name__ == '__main__':
    test_insertion_sort()
