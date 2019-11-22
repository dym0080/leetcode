## 我的Solution

[python](https://github.com/dym0080/leetcode/blob/master/code/724/724_find_pivot_index.py)

## 提交未通过记录

第一次提交:

```python
# https://leetcode-cn.com/submissions/detail/37486819/
# 732 / 741 个通过测试用例。状态：超出时间限制
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        a = []
        for i,v in enumerate(nums):
            left = nums[:i]
            right = nums[i+1:]
            if(sum(left) == sum(right)):
                a.append(i)
        if len(a) == 0:
            return -1
        else:
            return a[0]
```

第三次提交：尝试修改第一次提交的方案：

```python
# https://leetcode-cn.com/submissions/detail/37491940/
# 734 / 741 个通过测试用例 状态：超出时间限制
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i,v in enumerate(nums):
            left = nums[:i]
            right = nums[i+1:]
            if(sum(left) == sum(right)):
                return i
        return -1
```

超出时间限制是因为空间复杂度没控制在`O(1)`。使用了`a`,`left` ,`right`。

## 复杂度分析

官方题解：使用了[前缀和](https://leetcode-cn.com/problems/find-pivot-index/solution/xun-zhao-shu-zu-de-zhong-xin-suo-yin-by-leetcode/)方法
```python
class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1

```
- 时间复杂度：O(N)，其中 `N` 是 `nums` 的长度。
- 空间复杂度：O(1)，使用了 `S` 和 `leftsum` 。