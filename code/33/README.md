## 题目

[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) <br/> [搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)

## 我的Solution

- [python](../33/33_search_in_rotated_sorted_array.py)

## 解题思路

### 1. [python](../33/33_search_in_rotated_sorted_array.py)的思路

使用二分查找方法。根据题意，`nums`是在原先**升序**数组在某一个位置进行了旋转。旋转后取一个中心点 `mid`，**必定**存在其中一边（左边或右边）是升序的。

1-9的数组旋转的可能性如下：
```
1 2 3 4 5 6 7 8 9
2 3 4 5 6 7 8 9 1
3 4 5 6 7 8 9 1 2
4 5 6 7 8 9 1 2 3
5 6 7 8 9 1 2 3 4
6 7 8 9 1 2 3 4 9
7 8 9 1 2 3 4 9 6
8 9 1 2 3 4 9 6 7
9 1 2 3 4 9 6 7 8
```
初始值： `left, right,mid = 0, len(nums)-1 ,(left + right) // 2`
- `nums[left] < nums[mid]`：那么 `mid` 左边必定是升序。
    - `nums[l]<target<nums[mid]` : 目标值在升序中间，向左查找，丢弃右边的。
    - 否则，目标值在右边（不一定是升序），向右查找，丢弃左边的。
- 否则（即 `nums[mid] < nums[right]`）：`mid` 右边必定是升序的。
    - `nums[mid] < target < nums[right]`：目标值在升序中间，向右查询，丢弃左边的。
    - 否则，目标值在左边（不一定是升序），向左查找，丢弃右边的。

## 提交未通过记录

## 记录、比较、分析别人的Solution

## 其他
