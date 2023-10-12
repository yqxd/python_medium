"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

    For example, "AACCGGTT" --> "AACCGGTA" is one mutation.

There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.



Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2



Constraints:

    0 <= bank.length <= 10
    startGene.length == endGene.length == bank[i].length == 8
    startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].


"""

from typing import *


class Solution:
    def isvalid(self, fromGene, toGene):
        if sum(fromGene[i] != toGene[i] for i in range(len(fromGene))) == 1:
            return True
        else:
            return False

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        explore_list = [(startGene, 0)]
        while explore_list != []:
            crt_gene, crt_distance = explore_list.pop(0)
            for i in range(len(bank) - 1, -1, -1):
                if self.isvalid(fromGene=crt_gene, toGene=bank[i]):
                    explore_list.append((bank[i], crt_distance + 1))
                    if bank[i] == endGene:
                        return crt_distance + 1
                    else:
                        bank.pop(i)
        return -1


A = Solution()
A.minMutation(startGene="AACCGGTT", endGene="AACCGGTA", bank=["AACCGGTA"])
A.minMutation(startGene="AACCGGTT", endGene="AAACGGTA", bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"])
