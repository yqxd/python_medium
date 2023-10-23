"""
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.



Constraints:

    1 <= arr.length <= 16
    1 <= arr[i].length <= 26
    arr[i] contains only lowercase English letters.


"""

from collections import Counter
from typing import *


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def dfs_val(crt_set: set, arr: List[set]):
            if len(arr) == 0:
                return 0
            else:
                idx = 0
                while crt_set.intersection(arr[idx]).__len__() != 0:
                    idx += 1
                    if idx >= arr.__len__():
                        return 0
                return max(dfs_val(crt_set, arr[idx + 1:]), arr[idx].__len__() + dfs_val(crt_set.union(arr[idx]), arr[idx + 1:]))

        arr = list(filter(lambda x: max(Counter(x).values()) <= 1, arr))
        arr = [set(i) for i in arr]
        return dfs_val(set(), arr)


A = Solution()
arr = ["un", "iq", "ue"]
A.maxLength(arr)
