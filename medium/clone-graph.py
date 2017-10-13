#coding=utf-8

# Time:  O(n)
# Space: O(n)
#
# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
#
#
# OJ's undirected graph serialization:
# Nodes are labeled uniquely.
#
# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
#
# The graph has a total of three nodes, and therefore contains three parts as separated by #.
#
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
# Visually, the graph looks like the following:
#
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/
#
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution2:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if None == node: return None
        nodeMap = {}
        return self.cloneNode(node, nodeMap)

    def cloneNode(self, node, nodeMap):
        if None == node:
            return None
            # 访问当前点，这里不是简单的print，而是复制，若已经复制，则返回副本
        if nodeMap.has_key(node):
            return nodeMap[node]
            # 若没有副本，则复制一份，同样处理其邻接点
        else:
            clone = UndirectedGraphNode(node.label)
            nodeMap[node] = clone
            # 访问其邻居节点
            for neighbor in node.neighbors:
                clone.neighbors.append(self.cloneNode(neighbor, nodeMap))
        return clone


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        cloned_node = UndirectedGraphNode(node.label)
        cloned, queue = {node: cloned_node}, [node]

        while queue:
            current = queue.pop()
            for neighbor in current.neighbors:
                if neighbor not in cloned:
                    queue.append(neighbor)
                    cloned_neighbor = UndirectedGraphNode(neighbor.label)
                    cloned[neighbor] = cloned_neighbor
                cloned[current].neighbors.append(cloned[neighbor])
        return cloned[node]
