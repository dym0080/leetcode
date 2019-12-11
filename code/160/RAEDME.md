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

## 其他
