## 我的Solution

[python](../189/189_rotate_array.py)

## 解题思路

> 特别注意是：要求使用空间复杂度为 `O(1)` 的 `原地` 算法。

## 提交未通过记录

第一次提交:
```python
# https://leetcode-cn.com/submissions/detail/37826978/
# 9 / 34 个通过测试用例 状态：解答错误
# 输入：[1,2,3,4,5,6,7] 3 |输出：[1,2,3,4,5,6,7]|输出：[1,2,3,4,5,6,7]
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """       
        return nums[-k:]+nums[-k:]

```

第二次提交：

```python
# https://leetcode-cn.com/submissions/detail/37828932/
# 25 / 34 个通过测试用例 状态：解答错误
# 输入 [1,2] 3  输出：[1,2] 预期：[2,1]
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[-k:] + nums [:-k]
```


## 记录、比较、分析别人的Solution

## 复杂度分析