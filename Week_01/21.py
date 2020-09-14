"""
21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。



示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newHead = ListNode(None)
        pre = newHead
        cur1, cur2 = l1, l2
        while cur1 is not None and cur2 is not None:
            if cur1.val < cur2.val: 
                pre.next = cur1
                cur1 = cur1.next
            else:
                pre.next = cur2
                cur2 = cur2.next
            pre = pre.next
        if cur1 is not None:
            pre.next = cur1
        if cur2 is not None:
            pre.next = cur2
        return newHead.next
