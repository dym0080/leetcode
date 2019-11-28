## 我的Solution

[python](../66/66_plus_one.py)

## 解题思路

先把数组转换为连续的字符串，再把字符串转换为int，在此基础上加1，然后转换为连续的字符串，最好把字符串转换为int数组。

## 提交未通过记录

### 第一次提交

没有看清题目。
```python
# https://leetcode-cn.com/submissions/detail/38192692/
# 92 / 109 个通过测试用例 状态：解答错误
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        last = digits.pop()+1
        digits.append(last)
        return digits
```

## 记录、比较、分析别人的Solution
