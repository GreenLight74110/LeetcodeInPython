#


class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        i = 1
        while(i < len(nums)):
            ans ^= nums[i]
            i += 1
        return ans

import operator


class Solution:
    """
    :type nums: List[int]
    :rtype: int
    """
    def singleNumber(self, A):
        return reduce(operator.xor, A)

if __name__ == '__main__':
    print(Solution2().singleNumber([1, 1, 2, 2, 3]))