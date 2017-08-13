"""
@description:
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-2
"""

from data_structure.link_list.doubly_linked_list import DoublyLinkedList

my_list = DoublyLinkedList()
print(my_list.is_empty())

my_list.prepend(3)
my_list.prepend(2)
my_list.prepend(1)
my_list.print_all()

my_list.append(4)
my_list.append(5)
my_list.print_all()

my_list.pop()
my_list.print_all()

my_list.pop_last()
my_list.print_all()
