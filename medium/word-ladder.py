# Time:  O(n * d), n is length of string, d is size of dictionary
# Space: O(d)
#
# Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:
#
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# For example,
#
# Given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
#

# BFS
class Solution2:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, word_list):
        lad_len = 0
        cur = [start]
        visited = [start]

        while cur:
            _next = []

            for word in cur:
                if word == end:
                    return lad_len + 1
                for i in range(len(word)):
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate not in visited and candidate in word_list:
                            visited.append(candidate)
                            _next.append(candidate)
            lad_len += 1
            cur = _next
        return 0


class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, word_list):
        distance, cur, visited = 0, [start], set([start])

        while cur:
            _next = []

            for word in cur:
                if word == end:
                    return distance + 1
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate not in visited and candidate in word_list:
                            _next.append(candidate)
                            visited.add(candidate)
            distance += 1
            cur = _next

        return 0


if __name__ == "__main__":
    print(Solution().ladderLength("hit", "cog", set(["hot", "dot", "dog", "lot", "log"])))
    print(Solution().ladderLength("hit", "cog", set(["hot", "dot", "dog", "lot", "log", "cog"])))
    print(Solution2().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(Solution2().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
