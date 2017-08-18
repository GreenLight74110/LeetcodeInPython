# Time:  O(n)
# Space: O(n)

# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 通过一个字典存放已经遍历过的元素
        # 依次用nums中的元素与字典中的元素做比较
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
        return []

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 最原始的两层遍历
        k = 0
        for i in nums:
            j = target - i
            k += 1
            tmp_nums = nums[k:]
            if j in tmp_nums:
                return [k - 1, tmp_nums.index(j) + k]


if __name__ == '__main__':
    print Solution().twoSum((2, 7, 11, 15), 9)
