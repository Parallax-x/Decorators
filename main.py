from logger import test_1
from logger_1 import test_2
from generator_from_dz import flat_generator_1

list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]


if __name__ == '__main__':
    test_1()
    test_2()
    flat_generator_1(list_of_lists_1)
