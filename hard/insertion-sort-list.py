# Time:  O(n ^ 2)
# Space: O(1)
#
# Sort a linked list using insertion sort.
#

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


class Solution:
    def findPositioon(self, goal, head):
        cur = head
        prev = None
        while cur:
            if cur.val <= goal:
                prev = cur
                cur = cur.next
            else:
                break
        return prev

    def insertionSortList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        dummy = ListNode(-2147483648)
        cur = head
        while cur:
            # position = self.findPositioon(cur.val, dummy)
            sorted_cur = dummy
            position = None
            while sorted_cur: # 从已排序列中找到要插入的位置
                if sorted_cur.val <= cur.val:
                    position = sorted_cur
                    sorted_cur = sorted_cur.next
                else:
                    break
            tmp = cur.next # 将cur插入
            cur.next = position.next
            position.next = cur
            cur = tmp # 更新cur
        return dummy.next

    # @param head, a ListNode
    # @return a ListNode
    # @statement 选择排序，左边是已经排序好的，对右边的元素依次遍历，插入到左边序列
    def insertionSortList(self, head):
        if head is None or self.isSorted(head):
            return head

        dummy = ListNode(2147483648)
        dummy.next = head  # dummy用来记录链表的头
        cur, sorted_tail = head.next, head  # cur用来记录右边当前正在遍历的元素，sorted_tail用来记录左边已排序列的尾
        while cur:
            prev = dummy
            while prev.next.val > cur.val:  # 遍历左边序列，找到要插入的位置
                prev = prev.next
            if prev == sorted_tail:  # 如果已经到达已排序列的尾，说明cur不用动，移向下一个元素，同时更新已排序列的尾信息
                cur, sorted_tail = cur.next, cur
            else:  # 否则将cur插入到所找到的位置，更新已排序列的尾指向cur的下个元素，更新cur
                cur.next, prev.next, sorted_tail.next = prev.next, cur, cur.next
                cur = sorted_tail.next

        return dummy.next

    def isSorted(self, head):
        while head and head.next:
            if head.val > head.next.val:
                return False
            head = head.next
        return True


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(1)
    head = Solution().insertionSortList(head)
    print(head)
    head = Solution().insertionSortList2(head)
    print(head)
