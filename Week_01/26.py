"""
26. 删除排序数组中的重复项
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        newTail = 0
        for idc in range(1, len(nums)):
            if nums[newTail] == nums[idc]:
                continue
            newTail += 1
            nums[newTail] = nums[idc]
        return newTail + 1
