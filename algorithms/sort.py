class Sort(object):
    temp_nums = []  # 避免频繁的创建对象

    def exchange(self, nums, i, j):
        temp = nums[j]
        nums[j] = nums[i]
        nums[i] = temp

    def merge_sorted(self, nums1, m, nums2, n):
        i, j, k = m - 1, n - 1, m + n - 1
        while k >= 0:
            if i < 0:
                nums1[k], j = nums2[j], j - 1
            elif j < 0: # j<0 说明此时已经比完了
                break
            elif nums1[i] > nums2[j]:
                nums1[k], i = nums1[i], i - 1
            else:
                nums1[k], j = nums2[j], j - 1
            k -= 1

    def merge(self, nums, lo, mid, hi):
        i, j = lo, mid + 1

        for k in range(lo, hi + 1):
            self.temp_nums[k] = nums[k]

        for k in range(lo, hi + 1):  # 左边的用尽（取右边的），　右边的用尽（取左边的），　左边的小（取左边的），右边的小（取右边的）
            if i > mid:
                nums[k], j = self.temp_nums[j], j + 1
            elif j > hi:
                nums[k], i = self.temp_nums[i], i + 1
            elif self.temp_nums[i] < self.temp_nums[j]:
                nums[k], i = self.temp_nums[i], i + 1
            else:
                nums[k], j = self.temp_nums[j], j + 1

    def sort_merge(self, nums, lo, hi):  # 自顶而下
        if (lo >= hi):
            return
        mid = (int)((lo + hi) / 2)
        self.sort_merge(nums, lo, mid)
        self.sort_merge(nums, mid + 1, hi)
        if nums[mid] > nums[mid + 1]:  # 如果发现左边序列的尾小于右边序列的头，说明数组已经是有序的了，可以跳过merge
            self.merge(nums, lo, mid, hi)

    def merge_sort_UB(self, nums):
        self.temp_nums = [None] * len(nums)
        self.sort_merge(nums, 0, len(nums) - 1)

    def merge_sort_BU(self, nums):
        self.temp_nums = [None] * len(nums)
        sz = 1
        while sz < len(nums):
            lo = 0
            while lo + sz < len(nums):
                self.merge(nums, lo, lo + sz - 1, min(lo + sz + sz, len(nums)) - 1)
                lo += sz + sz
            sz += sz

    def bucket_sort(self, nums):
        max_val, min_val = max(nums), min(nums)
        bucket_range = (int)((max_val - min_val - 1) / (len(nums) - 1)) + 1
        bucket_size = (int)((max_val - min_val) / bucket_range) + 1
        buckets = [None] * bucket_size

        for num in nums: # 现将各个元素放入桶中
            idx = (int)((num - min_val) / bucket_range)
            if buckets[idx] is None:
                buckets[idx] = [num]
            else:
                buckets[idx].append(num)

        num_len = 0
        for i in range(bucket_size): # 对桶里的元素先排序，然后再merge
            if buckets[i] is None:
                continue
            for j in range(1, len(buckets[i])):
                temp = buckets[i][j]
                for k in range(j, 0, -1):
                    if buckets[i][k - 1] > temp:
                        self.exchange(buckets[i], k - 1, k)
                    else:
                        buckets[i][k] = temp
                        break
            self.merge_sorted(nums, num_len, buckets[i], len(buckets[i]))
            num_len += len(buckets[i])
        return nums

    def selectSort(self, nums):  # 降序
        for i in range(0, len(nums)):
            max = i
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[max]:
                    max = j
            self.exchange(nums, i, max)
        print(nums)

    def selectSort2(self, nums):  # 升序
        for i in range(0, len(nums)):
            min = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min]:
                    min = j
            self.exchange(nums, i, min)
        print(nums)

    def insertSort(self, nums):
        for i in range(1, len(nums)):
            temp = nums[i]
            for j in range(i, 0, -1):
                if nums[j - 1] < temp:
                    self.exchange(nums, j - 1, j)
                else:
                    nums[j] = temp
                    break
        print(nums)

    def bubbleSort(self, nums):
        for i in range(len(nums) - 1, 0, -1):
            for j in range(0, i):
                if nums[j + 1] > nums[j]:  # 小的换到后面去，所以是降序
                    self.exchange(nums, j, j + 1)
        print(nums)

    def bubbleSort2(self, nums):
        for i in range(0, len(nums)):
            for j in range(len(nums) - 1, i, -1):
                if nums[j - 1] > nums[j]:
                    self.exchange(nums, j - 1, j)
        print(nums)

    # decrease, general
    def quickSort(self, nums, lo, hi):
        if lo >= hi:
            return
        baseline = nums[lo]
        i = lo + 1
        j = hi
        while 1:
            while nums[i] >= baseline and i < hi:
                i += 1
            while nums[j] <= baseline and j > lo:
                j -= 1
            if i >= j:
                break
            self.exchange(nums, i, j)
        # 为什么是j而不是i，因为j最终记录到的是小于baseline的数，i最终记录的是大于baseline的数
        # 而结果要求baseline左边的数比它小，所以要将j最终记录到的数与baseline交换
        self.exchange(nums, lo, j)

        self.quickSort(nums, lo, j - 1)
        self.quickSort(nums, j + 1, hi)

    # increase,perform better when too many same items
    def quickSort_plus(self, nums, lo, hi):
        if lo >= hi:
            return
        baseline = nums[lo]
        lt = lo
        gt = hi
        i = lo + 1
        while i <= gt:
            diff = nums[i] - baseline
            if diff < 0:
                self.exchange(nums, i, lt)
                i += 1
                lt += 1
            elif diff > 0:
                self.exchange(nums, i, gt)
                gt -= 1
            else:
                i += 1
        self.quickSort_plus(nums, lo, lt - 1)
        self.quickSort_plus(nums, gt + 1, hi)


if __name__ == '__main__':
    nums = [4, 14, 23, 4, 2, 64, 21, 3, 35, 3]
    print(nums)
    # Sort().selectSort(nums)
    # Sort().insertSort(nums)
    # Sort().bubbleSort(nums)
    # Sort().quickSort(nums, 0, len(nums) - 1)
    # print(nums)
    # Sort().quickSort_plus(nums, 0, len(nums) - 1)
    # Sort().merge_sort_BU(nums)
    # print(nums)
    # Sort().merge_sort_UB(nums)
    # print(nums)
    Sort().bucket_sort(nums)
    print(nums)
