## 题目

[Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/) <br/> [猜数字大小](https://leetcode-cn.com/problems/guess-number-higher-or-lower/)

## 我的Solution

- [python](../374/374_guess_number_higher_or_lower.py)

## 解题思路

### 1. [python](../374/374_guess_number_higher_or_lower.py)的思路

使用二分查找算法。

## 提交未通过记录

### 1. https://leetcode-cn.com/submissions/detail/39749006/

用二分查找来实现完后，我想到下面这种方法，结果报 `Line 12: MemoryError` 错误。做算法题第一次遇到这种报错。

```python
# 14 / 25 个通过测试用例 状态：执行出错
# 执行出错信息：Line 12: MemoryError
# 最后执行的输入： 2126753390 1702766719

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(1,n+1):
            if guess(i) == 0:
                return i
        return -1
```

## 记录、比较、分析别人的Solution

## 其他
