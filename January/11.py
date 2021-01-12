import unittest

from typing import List
"""
Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Constraints:

    0 <= n, m <= 200
    1 <= n + m <= 200
    nums1.length == m + n
    nums2.length == n
    -109 <= nums1[i], nums2[i] <= 109

"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        _l = m+n - 1
        while p1 >= 0 or p2 >= 0:
            if nums1[p1] <= nums2[p2]:
                nums1[_l] = nums2[p2]
                p2 -= 1
            else:
                nums1[_l] = nums1[p1]
                p1 -= 1
            _l -= 1
        while p2 >= 0:
            nums1[_l] = nums2[p2]
            p2 -= 1
            _l -= 1
