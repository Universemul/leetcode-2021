import unittest

from typing import List
"""
Remove Duplicates from Sorted List II
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
 Constraints:
    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if other:
            return self.val == other.val
        return False
    
    def __repr__(self):
        return f"{self.val}"

    def __str__(self):
        return f"{self.val}"

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        if head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next) 
        head.next = self.deleteDuplicates(head.next)
        return head

class SolutionTest(unittest.TestCase):
    
    def test_full(self):
        l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
        cur = Solution().deleteDuplicates(l1)
        expected = [1, 2, 5]
        result = []
        while cur:
            result.append(cur.val)
            cur = cur.next
        self.assertEqual(result, expected)
    
    def test_empty(self):
        l1 = []
        self.assertEqual(Solution().deleteDuplicates(l1), [])

    def test3_one_element(self):
        l1 = ListNode(0, None)
        expected_node = ListNode(0, None)
        result = Solution().deleteDuplicates(l1)
        self.assertEqual(result, expected_node)
        self.assertIsNone(result.next)
if __name__ == '__main__':
    unittest.main()
