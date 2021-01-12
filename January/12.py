import unittest

from typing import List
"""
Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

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
    def _add(self, l1: ListNode, l2: ListNode, carry: int) -> ListNode
        if not l1 and not l2 and carry <= 0:
            return None
        total = carry
        if l1:
            total += l1.val
        if l2:
            total += l2.val
        carry = total // 10
        node = ListNode(total % 10)
        node.next = self.add(l1.next, l2.next, carry)
        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self._add(l1, l2, 0)
