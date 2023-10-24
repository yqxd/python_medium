"""
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.

Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].

Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.



Constraints:

    1 <= s.length <= 16

    s contains only lower case English letters.


"""

from typing import *
import functools


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        @functools.lru_cache(maxsize=128)
        def _dfs(crt_set: frozenset, s: str):
            if len(s) == 0:
                return 0
            return 1 + max([float("-Inf")] + [_dfs(crt_set.union({s[:i]}), s[i:])
                                              for i in range(1, len(s) + 1) if s[:i] not in crt_set])

        return _dfs(frozenset(), s)


A = Solution()
s = "ababccc"
A.maxUniqueSplit(s)
