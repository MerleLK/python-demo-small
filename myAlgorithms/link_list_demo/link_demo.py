"""
@description: This is a link list demo with python
@author: merle
@contact: merle.liukun@gmail.com
@date: 17-7-28
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class OneWeyLoopLink(object):
    def __init__(self):
        self.head = Node(Node)
        self.head.set_next(self.head)

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head.get_next())
        self.head.set_next(temp)

    def remove(self, item):
        prev = self.head
        while prev.get_next() != self.head:
            cur = prev.get_next()
            if cur.get_data() == item:
                prev.set_next(cur.get_next())
            prev = prev.get_next()

    def search(self, item):
        cur = self.head.get_next()
        while cur != self.head:
            if cur.get_data() == item:
                return True
            cur = cur.get_next()

    def empty(self):
        return self.head.get_next() == self.head

    def size(self):
        count = 0
        cur = self.head.get_next()
        while cur != self.head:
            count += 1
            cur = cur.get_next()

        return count


if __name__ == '__main__':
    link = OneWeyLoopLink()
    print('link.empty()=={}, link.size()=={}'.format(link.empty(), link.size()))

    link.add(19)
    link.add(60)
    print('link.empty()=={}, link.size()=={}'.format(link.empty(), link.size()))
