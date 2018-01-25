# Time:  O(n)
# Space: O(1)
#
# Given an array of integers, every element appears three times except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
import collections

class Solution5(object):
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        A = sorted(A)
        for i in range(1,len(A)-1,3):
            if A[i] != A[i+1] and A[i] != A[i-1]:
                print(A[i])
            elif A[i] == A[i+1] and A[i] != A[i-1]:
                print(A[i-1])
            elif A[i] != A[i + 1] and A[i] == A[i - 1]:
                print(A[i+1])
            # print i

class Solution(object):
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one, two = 0, 0
        for x in A:
            one, two = (~x & one) | (x & ~one & ~two), (~x & two) | (x & one)
        return one

class Solution2(object):
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one, two, carry = 0, 0, 0
        for x in A:
            two |= one & x
            one ^= x
            carry = one & two
            one &= ~carry
            two &= ~carry
        return one


class Solution3(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (collections.Counter(list(set(nums)) * 3) - collections.Counter(nums)).keys()[0]


class Solution4(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (sum(set(nums)) * 3 - sum(nums)) / 2


#  every element appears 4 times except for one with 2 times
class SolutionEX(object):
    # @param A, a list of integer
    # @return an integer
    # [1, 1, 1, 1, 2, 2, 2, 2, 3, 3]
    def singleNumber(self, A):
        one, two, three = 0, 0, 0
        for x in A:
            one, two, three = (~x & one) | (x & ~one & ~two & ~three), (~x & two) | (x & one), (~x & three) | (x & two)
        return two

if __name__ == "__main__":
    print(Solution5().singleNumber([1, 1, 1, 2, 2, 2, 3]))