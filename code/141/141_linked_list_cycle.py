# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution1(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head 
        slow = head
        while fast != None and fast.next !=None:
            fast = fast.next.next # 快指针 每次走两步
            slow = slow.next      # 慢指针 每次走一步
            if fast == slow:      # 当慢指针和快指针相遇时就说明有环
                return True
        return False


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution2(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False