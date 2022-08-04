# import pickle
#
#
# call test_class:
#     a_number =
#     a_string = "hej"
#     a_list = [1,2,3]
#
# my_object = test_case()
#
# my_pickle_object = pickle.dump(my_object)
#
# print(f"to sa objekty spiklowane\n{my_object}")
#
# my_object.a_dickt = none
#
# my_unpickled_object = pickle.loads(my_pickled_object)
# print(f"to sa objekty odpiklowane\n{my_unpickled_object.a_dickt}")
import csv

# with open('board_catalog.csv') as f:
#     f_csv = csv.reader(f, delimiter='\t')
#     headers = next(f_csv)
#     for row in f_csv:
#         print(row)

# col_types = [str, float, str, str, float, int]
# with open('board_catalog.csv') as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv)
#     for row in f_csv:
#         row = tuple(convert(value) for convert, value in zip(col_types, row))
#         print(row)

from xml.etree.ElementTree import iterparse
from collections import Counter


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    next(doc)
    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


Country = Counter()

data = parse_and_remove('cd_catalog.xml', 'row/row')
for x in data:
    Country[x.findtext('COUNTRY')] += 1
for price, num in Country.most_common():
    print(price, num)
