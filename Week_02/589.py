#pylint: disable=all
"""
589. N叉树的前序遍历
给定一个 N 叉树，返回其节点值的前序遍历。

例如，给定一个 3叉树 :

返回其前序遍历: [1,3,5,6,2,4]。
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# 1.递归 time O(n)
# 2.迭代 time O(n)

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        self._preorder(root, result)
        return result

    def _preorder(self, root, result):
        if root is None:
            return
        result.append(root.val)
        for children in root.children:
            self._preorder(children, result)


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack, result = [root], []
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(node.children[::-1])
        return result
