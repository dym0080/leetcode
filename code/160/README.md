## 题目

[Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) <br/> [相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/)

## 我的Solution

[python](../160/160_intersection_of_two_linked_lists.py)

## 解题思路

### 1. [python](../160/160_intersection_of_two_linked_lists.py) 的思路

使用哈希表方法，先循环链表 `A`，存入一个集合 `set` 中，再循环链表 `B`，判断当前元素是否在集合中即可。

- 时间复杂度为：`T(m+n) => T(2n) => O(n)`
- 空间复杂度为：`O(1)` 

## 提交未通过记录

## 记录、比较、分析别人的Solution

### 1. 来源 [leetcode-cn](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/tu-jie-xiang-jiao-lian-biao-by-user7208t/)，看图理解，非常巧妙的思路

java:
```java
public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
    if (headA == null || headB == null) return null;
    ListNode pA = headA, pB = headB;
    while (pA != pB) {
        pA = pA == null ? headB : pA.next;
        pB = pB == null ? headA : pB.next;
    }
    return pA;
}
```

python:
``` python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = headA
        b = headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
```

## 其他
