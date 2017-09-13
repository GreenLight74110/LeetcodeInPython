# coding=utf-8

# Time:  O(1)
# Space: O(1)
#
# Given an integer, write a function to determine if it is a power of two.

# 如果一个数n是2的平方，那它的形式一定是1000....
# n-1则为0111....
# 所以n & n-1就是00000....

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0


class Solution2:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n > 0 and (n & ~-n) == 0

print 12
print ~-12