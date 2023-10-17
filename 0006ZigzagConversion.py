"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);



Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"



Constraints:

    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000
"""

from typing import *


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ""
        circle = 2 * numRows - 2
        if circle == 0:
            return s
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                result += s[i::circle]
            else:
                s1 = s[i::circle]
                s2 = s[circle-i::circle]
                if len(s1) == len(s2):
                    result += "".join([s1[j] + s2[j] for j in range(len(s1))])
                else:
                    result += "".join([s1[j] + s2[j] for j in range(len(s2))]) + s1[-1]
        return result

s = "A"
numRows = 1
A = Solution()
print(A.convert(s, numRows))
