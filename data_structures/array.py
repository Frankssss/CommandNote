'''
Author: Frank Shen
Email: m13917334342.com
Data: 2019/10/8 17:46
'''


class Array:
    def __init__(self, size, init=None):
        self._size = size
        self._items = [init] * self._size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def clear(self, value=None):
        for index in range(len(self._items)):
            self._items[index] = value

    def __len__(self):
        return self._size

    def __iter__(self):
        for elem in self._items:
            yield elem


def test_array():
    array = Array(32)
    array[5] = 'Frank'
    assert array[5] == 'Frank'
    assert len(array) == 32
    array.clear()
    assert [elem for elem in array if elem is not None] == []


if __name__ == '__main__':
    test_array()

