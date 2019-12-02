## 题目

[Reverse Integer](https://leetcode.com/problems/reverse-integer/) <br/> [整数反转](https://leetcode-cn.com/problems/reverse-integer/)

## 我的Solution

[python](../7/7_reverse_integer.py)

## 解题思路

### 1.[python](../7/7_reverse_integer.py)的思路

先判断是否大于0，然后转换为字符串进行反转，再转换为int，最后判断值的范围。

## 提交未通过记录

### 1. https://leetcode-cn.com/submissions/detail/38569138/

未考虑 `32` 位的有符号整数，则其数值范围为 `[−2^31,  2^31 − 1]`

```python
# 1027 / 1032 个通过测试用例 状态：解答错误
# 输入：1534236469 输出：9646324351 预期：0
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            temp1 = str(x)[::-1]
            return int(temp1)
        else:
            temp2 = str(-1*x)[::-1]
            return -1 * int(temp2)
```

## 记录、比较、分析别人的Solution
