# pylint: disable=all
"""
49. 字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
"""
# 1. 暴力 排序
# 2. hash 验证异位
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for string in strs:
            ans[tuple(sorted(string))].append(string)
        return ans.values()


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for string in strs:
            an = [0] * 26
            for i in string:
                an[ord(i) - ord("a")] += 1
            ans[an].append(i)
        return list(ans.values())
