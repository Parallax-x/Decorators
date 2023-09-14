from logger_1 import logger1


@logger1('main2.log')
def flat_generator_1(list_of_list: list):

    for item in list_of_list:
        if type(item) is not list:
            yield item
        else:
            yield from flat_generator_1(item)
