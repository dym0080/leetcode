## 题目

[Two Sum](https://leetcode.com/problems/two-sum/) <br/> [两数之和](https://leetcode-cn.com/problems/two-sum/) 

## 我的Solution

[python](../1/1_two_sum.py)

## 提交未通过记录

第一次提交：

```python
# https://leetcode-cn.com/submissions/detail/37511200/
# 19 / 29 个通过测试用例 状态：解答错误
# 未通过输入： [3,2,4] 6  输出：[0,0]  预期：[1,2]
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,v in enumerate(nums):
            other = target -v
            if nums.count(other):
                return [i,nums.index(other)]
```
出错时因为 `other` 应该要在余下的数据中去检查，没有排除掉 `v`。

