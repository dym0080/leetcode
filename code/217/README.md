## 我的Solution

[python](../217/217_contains_duplicate.py)

## 解题思路

思路1：如第一次提交的代码所示，遍历数组，使用count()找出是否有重复的。

思路2：把数组转换为集合set，因为set会自动去除重复项。于是只要判断集合的长度小于数组的长度，就说明有重复项。

## 提交未通过记录

第一次提交(根据思路1)：

```python
# https://leetcode-cn.com/submissions/detail/37836392/
# 17 / 18 个通过测试用例 状态：超出时间限制
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for item in nums:
            if nums.count(item)>1:
                return True
        return False
        
```
`nums.count(item)`是具有时间复杂度（估计是 `O(n)` 或者 `O(logN)`,没找到具体资料证实）的，放在 `for` 循环后，整个时间复杂度就变成了`O(N^2)` 或 `O(N*logN)`，所以才会超时。

## 记录、比较、分析别人的Solution
