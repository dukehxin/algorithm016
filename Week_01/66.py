"""
https://leetcode-cn.com/problems/plus-one/
66. 加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        self.reverse(digits)
        flag = 1
        for idc in range(len(digits)):
            flag, num = divmod(digits[idc] + flag, 10)
            digits[idc] = num
        if flag:
            digits.append(flag)
        self.reverse(digits)
        return digits

    def reverse(self, digits):
        start, end = 0, len(digits) - 1
        while start < end:
            digits[start], digits[end] = digits[end], digits[start]
            start += 1
            end -= 1
