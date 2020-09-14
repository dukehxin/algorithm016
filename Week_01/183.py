"""
189. 旋转数组
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        self.reverse(nums, 0, length - 1)
        k = k % length
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, length - 1)

    def reverse(self, nums: List[int], start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
