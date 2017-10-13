# Time:  O(n * h)
# Space: O(h)
#
# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#   1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]
#
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        result, path = [], []
        self.binaryTreePathsRecu2(root, path, result)
        return result

    def binaryTreePathsRecu2(self, node, path, result):
        if node is None:
            return

        if node.left is None and node.right is None:
            ans = ""
            for p in path:
                ans += str(p) + "->"
            result.append(ans + str(node.val))
            # return

        path.append(node.val)
        self.binaryTreePathsRecu2(node.left, path, result)
        self.binaryTreePathsRecu2(node.right, path, result)
        path.pop()
        # return

    def binaryTreePathsRecu(self, node, path, result):
        if node is None:
            return

        if node.left is node.right is None:
            ans = ""
            for n in path:
                ans += str(n.val) + "->"
            result.append(ans + str(node.val))

        if node.left:
            path.append(node)
            self.binaryTreePathsRecu(node.left, path, result)
            path.pop()

        if node.right:
            path.append(node)
            self.binaryTreePathsRecu(node.right, path, result)
            path.pop()


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    print Solution().binaryTreePaths(root)