"""
@description:
@author: merle
@contact: merle.liukun@gmail.com
@date: 17-8-2
"""

from data_structure.link_list.singly_linked_list import CircularSinglyLinkedList

my_list = CircularSinglyLinkedList()

print(my_list.is_empty())

my_list.prepend(3)
my_list.prepend(2)
my_list.prepend(1)
my_list.append(4)
my_list.append(5)

print(my_list.is_empty())
my_list.print_all()

my_list.pop()
my_list.print_all()

my_list.pop_last()
my_list.print_all()
