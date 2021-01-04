import unittest

from typing import List
"""
 Merge 2 sorted lists
 Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 Constraints:
     The number of nodes in both lists is in the range [0, 50].
     -100 <= Node.val <= 100
     Both l1 and l2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        return self.val == other.val
    
    def __repr__(self):
        return f"{self.val}"

    def __str__(self):
        return f"{self.val}"

class Solution:
    def mergeTwoLists(self, l1: List[ListNode], l2: List[ListNode]) -> List[ListNode]:
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2

class SolutionTest(unittest.TestCase):
    
    def test_full(self):
        n3 = ListNode(3, None)
        n2 = ListNode(2, n3)
        n1 = ListNode(1, n2)
        nn4 = ListNode(4, None)
        nn3 = ListNode(3, nn4)
        nn1 = ListNode(1, nn3)
        cur = Solution().mergeTwoLists(n1, nn1)
        expected = [1, 1, 2, 3, 3, 4]
        result = []
        while cur:
            result.append(cur.val)
            cur = cur.next
        self.assertEqual(result, expected)
    
    def test_empty(self):
        l1 = []
        l2 = []
        self.assertEqual(Solution().mergeTwoLists(l1, l2), [])

    def test3_one_element(self):
        l1 = None
        l2 = ListNode(0, None)
        self.assertEqual(Solution().mergeTwoLists(l1, l2), ListNode(0))

if __name__ == '__main__':
    unittest.main()
