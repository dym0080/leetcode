## 题目

[Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) <br/> [环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)

## 我的Solution

[python](../142/142_linked_list_cycle_ii.py)

## 解题思路

### 1. [python](../142/142_linked_list_cycle_ii.py)的思路

参照 [141-python-Solution1](../141/141_linked_list_cycle.py) 的思路

## 提交未通过记录

### 1. https://leetcode-cn.com/submissions/detail/39607358/

想参照 [141-python-Solution2](../141/141_linked_list_cycle.py) 的思路，但是报错。 需要再研究下。
```python
# 11 / 16 个通过测试用例 状态：解答错误
# 输入：[-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5] 24
# 输出：tail connects to node index 26
# 预期：tail connects to node index 24

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head 
        slow = head
        while fast != None and fast.next !=None:
            fast = fast.next.next # 快指针 每次走两步
            if fast == slow:      # 当慢指针和快指针相遇时就说明有环
                return slow            
            slow = slow.next      # 慢指针 每次走一步
        return None
        
```

## 记录、比较、分析别人的Solution

## 其他
