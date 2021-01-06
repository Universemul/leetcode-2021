import unittest

from typing import List
"""
Kth Missing Positive Number
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

Constraints:
    1 <= arr.length <= 1000
    1 <= arr[i] <= 1000
    1 <= k <= 1000
    arr[i] < arr[j] for 1 <= i < j <= arr.length
"""
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if not arr:
            return None
        start = 1
        while k:
            if start not in arr:
                k = k - 1
            start = start + 1
        return start - 1
            
class SolutionTest(unittest.TestCase):
    
    def test_5kth(self):
        input_ = [2,3,4,7,11]
        expected = 9
        self.assertEqual(Solution().findKthPositive(input_, 5), expected)
    
    def test_one_element(self):
        input_ = [2]
        expected = 1
        self.assertEqual(Solution().findKthPositive(input_, 1), expected)

    def test_empty(self):
        l1 = []
        self.assertEqual(Solution().findKthPositive([], 2), None)

    def test3_2kth(self):
        input_ = [1,2,3,4]
        expected = 6
        self.assertEqual(Solution().findKthPositive(input_, 2), expected)

if __name__ == '__main__':
    unittest.main()
