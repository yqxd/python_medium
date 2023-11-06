"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.



Example 1:

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false



Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= n, m <= 300
    -109 <= matrix[i][j] <= 109
    All the integers in each row are sorted in ascending order.
    All the integers in each column are sorted in ascending order.
    -109 <= target <= 109


"""

from typing import List
from functools import cache


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        begin_i = m
        end_i = -1
        for i in range(m - 1, -1, -1):
            if matrix[i][0] <= target:
                end_i = i
                break
        for i in range(m):
            if matrix[i][n - 1] >= target:
                begin_i = i
                break
        if begin_i > end_i:
            return False

        @cache
        def binary_search(i, target):
            begin = 0
            end = n - 1
            while begin <= end:
                mid = (begin + end) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    begin = mid + 1
                else:
                    end = mid - 1
            return False

        for i in range(begin_i, end_i + 1):
            if binary_search(i, target):
                return True
        return False


A = Solution()
matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 21
A.searchMatrix(matrix, target)
