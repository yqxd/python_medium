"""
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.



Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2

Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10



Constraints:

    1 <= expression.length <= 20
    expression consists of digits and the operator '+', '-', and '*'.
    All the integer values in the input expression are in the range [0, 99].


"""

from typing import *
import re
from itertools import chain


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        expression = expression.replace(" ", "")
        nums = [int(i) for i in re.split(r"\+|-|\*", expression)]
        ops = [op for op in expression if op in ["+", "-", "*"]]

        def operation(n1, n2, ops):
            if ops == "+":
                return [i + j for i in n1 for j in n2]
            elif ops == "-":
                return [i - j for i in n1 for j in n2]
            else:
                return [i * j for i in n1 for j in n2]

        results = [[[] for _ in range(len(nums))] for _ in range(len(nums))]
        for i in range(len(nums)):
            results[i][i] = [nums[i]]
        for k in range(1, len(nums)):
            for i in range(len(nums) - k):
                results[i][i + k] = list(chain(*(operation(results[i][j], results[j + 1][i + k], ops[j]) for j in range(i, i + k))))
        return sorted(list(results[0][len(nums) - 1]))


A = Solution()
expression = "2*3-4*5"
print(A.diffWaysToCompute(expression))
