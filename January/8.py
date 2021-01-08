import unittest

from typing import List
"""
Check If Two String Arrays are Equivalent

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
A string is represented by an array if the array elements concatenated in order forms the string.

Constraints:

    1 <= word1.length, word2.length <= 103
    1 <= word1[i].length, word2[i].length <= 103
    1 <= sum(word1[i].length), sum(word2[i].length) <= 103
    word1[i] and word2[i] consist of lowercase letters.

"""
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)

class SolutionTest(unittest.TestCase):
    
    def test_equals(self):
        self.assertEqual(Solution().arrayStringsAreEqual(["ab", "c"], ["a", "bc"]), True)
    
    def test_not_equal(self):
        self.assertEqual(Solution().arrayStringsAreEqual(["a", "cb"], ["a", "bc"]), False)

    def test_empty(self):
        self.assertEqual(Solution().arrayStringsAreEqual([], []), True)

if __name__ == '__main__':
    unittest.main()
