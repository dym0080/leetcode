## 题目

[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) <br/> [环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)

## 我的Solution

[python](../141/141_linked_list_cycle.py)

## 解题思路

### 1. [python-Solution1](../141/141_linked_list_cycle.py) 的思路

使用双指针方法：如果有环，快指针最终将与慢指针相遇。

### 2. [python-Solution2](../141/141_linked_list_cycle.py) 的思路

> 这个解决方案是看了官方的 `Java` 版本写出来的。

使用哈希表法，依次循环链表往 `set` 中添加当前元素，如果遇到 `set` 已存在之前添加过的，说明有闭环，此时返回 `Ture` 退出循环。如果没有闭环，在循环结束返回 `False`。

## 提交未通过记录

## 记录、比较、分析别人的Solution

## 其他
