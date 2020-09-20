# pylint: disable=all
"""
94. 二叉树的中序遍历
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self._inorderTraversal(root, result)
        return result

    def _inorderTraversal(self, root, result):
        if root is None:
            return
        self._inorderTraversal(root.left, result)
        result.append(root.val)
        self._inorderTraversal(root.right, result)


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # black-未处理 red-已处理
        stack, result = [[root, "black"]], []
        while stack:
            (top, color) = stack[-1]
            if top.left is not None and color == "black":
                stack[-1][1] = "red"
                stack.append([top.left, "black"])
                continue
            node, _ = stack.pop()
            result.append(node.val)
            if node.right is not None:
                stack.append([node.right, "black"])
        return result
