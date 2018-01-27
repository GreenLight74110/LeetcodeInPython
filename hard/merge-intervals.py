# Time:  O(nlogn)
# Space: O(1)
#
# Given a collection of intervals, merge all overlapping intervals.
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
#

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)


class Solution(object):
    def exchange(self, intervals, i, j):
        tmp = intervals[i]
        intervals[i] = intervals[j]
        intervals[j] = tmp

    def quicksort(self, intervals, lo, hi):
        if hi < lo:
            return

        lt = lo
        gt = hi
        i = lo + 1
        bs = intervals[lt]
        while i <= gt:
            diff = intervals[i].start - bs.start
            if diff < 0:
                self.exchange(intervals, i, lt)
                i += 1
                lt += 1
            elif diff > 0:
                self.exchange(intervals, i, gt)
                gt -= 1
            else:
                i += 1
        self.quicksort(intervals, lo, lt - 1)
        self.quicksort(intervals, gt + 1, hi)

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals

        # bubblesort
        # for i in range(0, len(intervals)):
        #     for j in range(len(intervals) - 1, i, -1):
        #         if intervals[j].start < intervals[j - 1].start:
        #             temp = intervals[j]
        #             intervals[j] = intervals[j - 1]
        #             intervals[j - 1] = temp
        # print(intervals)

        # quicksort
        self.quicksort(intervals, 0, len(intervals)-1)
        print(intervals)

        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i].start > result[-1].end:
                result.append(intervals[i])
            elif intervals[i].end > result[-1].end:
                result[-1].end = intervals[i].end
        return result

    def merge2(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x.start)
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            prev, current = result[-1], intervals[i]
            if current.start <= prev.end:
                prev.end = max(prev.end, current.end)
            else:
                result.append(current)
        return result


if __name__ == "__main__":
    # lst = [1,2,3]
    # prev = lst[1]
    # print(prev)
    # prev = 4
    # print(prev)
    print(Solution().merge([Interval(1, 4), Interval(0, 1)]))
    print(Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]))
