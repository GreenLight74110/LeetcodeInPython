# Time:  O(n)
# Space: O(n)

# Given an unsorted array, find the maximum difference between
#
# the successive elements in its sorted form.
#
# Try to solve it in linear time/space.
#
# Return 0 if the array contains less than 2 elements.
#
# You may assume all elements in the array are non-negative integers
#
#  and fit in the 32-bit signed integer range.

# bucket sort
# Time:  O(n)
# Space: O(n)
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        max_val, min_val = max(nums), min(nums)
        bucket_range = (int)((max_val - min_val - 1) / (len(nums) - 1)) + 1
        bucket_size = int((max_val - min_val) / bucket_range) + 1
        buckets = [None] * bucket_size

        for num in nums:
            bucket_idx = int((num - min_val) / bucket_range)
            if buckets[bucket_idx] is None:
                buckets[bucket_idx] = {"min": num, "max": num}
            else:
                buckets[bucket_idx]["min"] = min(buckets[bucket_idx]["min"], num)
                buckets[bucket_idx]["max"] = max(buckets[bucket_idx]["max"], num)

        max_gap = 0
        pre = 0
        for i in range(1, bucket_size):
            if buckets[i] is None:
                continue
            max_gap, pre = max(max_gap, buckets[i]["min"] - buckets[pre]["max"]), i

        return max_gap

    def maximumGap2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        # Init bucket.
        max_val, min_val = max(nums), min(nums)
        gap = max(1, (max_val - min_val) / (len(nums) - 1))
        bucket_size = (max_val - min_val) / gap + 1
        bucket = [{'min': float("inf"), 'max': float("-inf")} \
                  for _ in range(bucket_size)]

        # Find the bucket where the n should be put.
        for n in nums:
            # min_val / max_val is in the first / last bucket.
            if n in (max_val, min_val):
                continue
            i = (n - min_val) / gap
            bucket[i]['min'] = min(bucket[i]['min'], n)
            bucket[i]['max'] = max(bucket[i]['max'], n)

        # Count each bucket gap between the first and the last bucket.
        max_gap, pre_bucket_max = 0, min_val
        for i in range(bucket_size):
            # Skip the bucket it empty.
            if bucket[i]['min'] == float("inf") and \
                            bucket[i]['max'] == float("-inf"):
                continue
            max_gap = max(max_gap, bucket[i]['min'] - pre_bucket_max)
            pre_bucket_max = bucket[i]['max']
        # Count the last bucket.
        max_gap = max(max_gap, max_val - pre_bucket_max)

        return max_gap


# Time:  O(nlogn)
# Space: O(n)
class Solution2(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 2:
            return 0

        nums.sort()
        pre = nums[0]
        max_gap = float("-inf")

        for i in nums:
            max_gap = max(max_gap, i - pre)
            pre = i
        return max_gap


if __name__ == "__main__":
    print(Solution().maximumGap([3, 1, 1, 1, 5, 5, 71, 5]))
    print(Solution().maximumGap([1, 1, 1, 1]))
