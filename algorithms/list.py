# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))
        else:
            return "Nil"


class SinLinkedList:
    def __init__(self):
        self.head = ListNode(None)
        self.tail = self.head
        self.size = 0

    def initList(self, vals=[]):  # 根据数组初始化链表
        self.__init__()
        for val in vals:
            self.add(val)

    def add(self, val):  # 尾插法
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def get(self, idx=0):  # 得到某个位置的元素
        if self.size <= 0 or idx > self.size or idx < -1:
            print("erro: idx out of range!")
            return None
        p = self.head
        for j in range(-1, idx):
            p = p.next
        return p

    def locate(self, val=0):  # 定位某个元素的位置
        p = self.head.next
        i = 0
        while (p):
            if p.val == val:
                return i
            p = p.next
            i += 1
        return -1

    def insert(self, idx=0, val=0): # 在某个位置插入一个元素（后插）
        if self.size <= 0 or idx > self.size or idx < 0:
            print("erro: idx out of range!")
            return
        p = self.get(idx - 1)
        newNode = ListNode(val)
        newNode.next = p.next
        p.next = newNode
        self.size += 1

    def remove(self, idx=0): # 删除某个位置的元素
        if self.size <= 0 or idx > self.size - 1 or idx < 0:
            print("erro: idx out of range!")
            return
        p = self.get(idx - 1)
        p.next = p.next.next
        self.size -= 1


if __name__ == "__main__":
    sinLinkedList = SinLinkedList()
    print("=======initList function:")
    sinLinkedList.initList()
    print(sinLinkedList.head)
    sinLinkedList.initList("sddd")
    print(sinLinkedList.head)
    sinLinkedList.initList([1, 2, 3, 4, 5])
    print(sinLinkedList.head)
    print("=======locate function:")
    print(sinLinkedList.locate(23432))
    print(sinLinkedList.locate(1))
    print(sinLinkedList.locate(3))
    print(sinLinkedList.locate(sinLinkedList.size - 1))
    print(sinLinkedList.locate(sinLinkedList.size))
    print(sinLinkedList.locate(sinLinkedList.size + 1))
    print("=======get function:")
    print(sinLinkedList.get(-1))
    print(sinLinkedList.get(0))
    print(sinLinkedList.get(3))
    print(sinLinkedList.get(sinLinkedList.size - 1))
    print(sinLinkedList.get(sinLinkedList.size))
    print(sinLinkedList.get(sinLinkedList.size + 1))
    print("=======add function:")
    sinLinkedList.add(6)
    print(sinLinkedList.head)
    print("=======insert function:")
    sinLinkedList.insert(-1, -1)
    print(sinLinkedList.head)
    sinLinkedList.insert(0, 0)
    print(sinLinkedList.head)
    sinLinkedList.insert(3, 98)
    print(sinLinkedList.head)
    sinLinkedList.insert(sinLinkedList.size - 1, 99)
    print(sinLinkedList.head)
    sinLinkedList.insert(sinLinkedList.size, 100)
    print(sinLinkedList.head)
    sinLinkedList.insert(sinLinkedList.size + 1, 101)
    print(sinLinkedList.head)
    print("=======remove function:")
    sinLinkedList.remove(-1)
    print(sinLinkedList.head)
    sinLinkedList.remove(0)
    print(sinLinkedList.head)
    sinLinkedList.remove(3)
    print(sinLinkedList.head)
    sinLinkedList.remove(sinLinkedList.size - 1)
    print(sinLinkedList.head)
    sinLinkedList.remove(sinLinkedList.size)
    print(sinLinkedList.head)
    sinLinkedList.remove(sinLinkedList.size + 1)
    print(sinLinkedList.head)
