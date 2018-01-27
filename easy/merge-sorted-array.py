# Time:  O(n)
# Space: O(1)
#
# Given two sorted integer arrays A and B, merge B into A as one sorted array.
#
# Note:
# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B.
# The number of elements initialized in A and B are m and n respectively.
#

class Solution:
    def merge2(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        for k in range(m + n - 1, -1, -1):
            if j < 0:
                return
            elif i < 0:
                # nums1[k], j = nums2[j], j - 1
                nums1[:k] = nums2[:j]
            elif nums1[i] < nums2[j]:
                nums1[k], j = nums2[j], j - 1
            else:
                nums1[k], i = nums1[i], i - 1
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        last, i, j = m + n - 1, m - 1, n - 1

        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[last] = A[i]
                last, i = last - 1, i - 1
            else:
                A[last] = B[j]
                last, j = last - 1, j - 1

        while j >= 0:
            A[last] = B[j]
            last, j = last - 1, j - 1


if __name__ == "__main__":
    A = [1, 3, 5, 0, 0, 0, 0]
    B = [2, 4, 6, 7]
    A = [0]
    B = [1]
    Solution().merge2(A,0,B,1)
    print(A)


# Time:  O(n)
# Space: O(n)
# you may get a input like this,
# nums1 : [0]
# m : 0
# nums2 : [1]
# n : 1
# so you need to judge if n is still large than 0
class Solution2:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]  # Space: O(n),
            # Reference:
            # - https://stackoverflow.com/questions/4948293/python-slice-assignment-memory-usage
            # - https://stackoverflow.com/questions/10623302/how-assignment-works-with-python-list-slice
