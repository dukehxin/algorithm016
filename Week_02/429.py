# pylint: disable=all
"""
给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

例如，给定一个 3叉树 :
返回其层序遍历:

[
     [1],
     [3,2,4],
     [5,6]
]
 

说明:

树的深度不会超过 1000。
树的节点总数不会超过 5000。
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        stack, result = [[root]], []
        while stack:
            node_list = stack.pop()
            temp = []
            next_list = []
            for node in node_list:
                temp.append(node.val)
                if next_list:
                    next_list.extend(node.children) 
            stack.append(next_list)
            result.append(temp)
        return result
