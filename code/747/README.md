## 题目

[Largest Number At Least Twice of Others](https://leetcode.com/problems/largest-number-at-least-twice-of-others/) <br/> [至少是其他数字两倍的最大数](https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/)

## 我的Solution

[python](../747/747_largest_number_at_least_twice_of_others.py)

## 解题思路

### 1. [python](../747/747_largest_number_at_least_twice_of_others.py)的思路

先使用 `max` 函数找出 `list` 中最大值，然后在 `for` 循环里面进行判断只要存在最大值小于其他任何一个值的两倍就返回 `-1` 。

## 提交未通过记录

## 记录、比较、分析别人的Solution

### 1. 来源[leetcode-cn](https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/comments/)的评论

先进行排序，找出第二大的数，只要跟第二大的数的两倍进行判断即可。

```python
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sort = sorted(nums)
        if len(nums) == 1:
            return 0
        if nums_sort[-1] >= nums_sort[-2]*2:
            return nums.index(nums_sort[-1])
        else:
            return -1
```

## 其他
