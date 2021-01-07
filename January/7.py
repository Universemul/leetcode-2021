import unittest

from typing import List
"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.
Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        idx = start = res = 0
        while idx < len(s):
            tmp = s[idx]
            if tmp in cache:
                start = max(start, cache[tmp] + 1)
            if res < (idx - start + 1):
                res = idx - start + 1
            cache[tmp] = idx
            idx += 1
        return res

class SolutionTest(unittest.TestCase):
    
    def test_full(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("abcabcbb"), 3)
    
    def test_identical_letters(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("bbbbb"), 1)

    def test_empty(self):
        self.assertEqual(Solution().lengthOfLongestSubstring(""), 0)

if __name__ == '__main__':
    unittest.main()
