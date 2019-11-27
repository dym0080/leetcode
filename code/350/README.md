## 我的Solution

[python](../350/350_intersection_of_two_arrays_ii.py)

## 解题思路

把长度小的放在第一次遍历中，然后再第二个长的数组中找是否存在这个元素。

## 提交未通过记录

### 第一次提交

没有考虑“输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致”。

```python
# https://leetcode-cn.com/submissions/detail/38076482/
# 36 / 61 个通过测试用例 状态：解答错误
# 输入：[1,2,2,1] [2] 输出：[2,2] 预期：[2]
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for item in nums1:
            if item in nums2:
                result.append(item)
        return result
```

### 第二次提交

还是一样没有考虑“输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致”。只是相对于第一次提交通过了`[1,2,2,1] [2]`作为输入的测试用例。

```python
# https://leetcode-cn.com/submissions/detail/38077792/
# 36 / 61 个通过测试用例 状态：解答错误
# 输入：[3,1,2] [1,1] 输出：[1,1] 预期：[1]
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        if len(nums1) <= len(nums2):
            for item in nums1:
                if item in nums2:
                    result.append(item)
            return result
        else:
            for item in nums2:
                if item in nums1:
                    result.append(item)
            return result
```



## 记录、比较、分析别人的Solution
