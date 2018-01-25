# Time:  O(1)
# Space: O(1)
#
# Given an integer, write a function to determine if it is a power of two.


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


class Solution3:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        else:
            result = 0
            for i in range(n):
                result += (n & 1)
                n >>= 1
            return result == 1