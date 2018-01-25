# coding=utf-8

# Time:  O(n)
# Space: O(1)
#
# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution2():
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        carry = 0
        current = dummy

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry = val / 10
            val = val % 10
            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(1)

        return dummy.next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # dummy表示头指针
        dummy = ListNode(0)
        # carry表示进位
        current, carry = dummy, 0

        # 遍历两个链表
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = val / 10, val % 10
            current.next = ListNode(val)
            current = current.next

        # 如果最后一位还有进位，也要加上
        if carry == 1:
            current.next = ListNode(1)

        return dummy.next


if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(7)
    result = Solution2().addTwoNumbers(a, b)
    print("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))
