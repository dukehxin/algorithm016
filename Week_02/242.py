# pylint: disable=all
"""
242. 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""
# 1. 暴力 sorted --> 排序后是否相等 O(nlog(n))
# 2. hash map --> 统计每个字符出现的频次

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        for i in s:
            dict1[i] = dict1.get(i, 0) + 1
        dict2 = {}
        for i in t:
            dict2[i] = dict2.get(i, 0) + 1
        return dict1 == dict2


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table1, hash_table2 = [0] * 26, [0] * 26
        for i in s:
            hash_table1[ord(i) - ord("a")] += 1
        for j in t:
            hash_table2[ord(j) - ord("a")] += 1
        return hash_table1 == hash_table2
