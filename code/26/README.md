## 题目

 [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) <br /> [删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)

## 我的Solution

[python](../26/26_remove_dulicates_from_sorted_array.py)

## 提交未通过记录

### 1. https://leetcode-cn.com/submissions/detail/37356096/

```python

# 39 / 161 个通过测试用例 状态：解答错误
# 输入：[1,1,1,1] 输出：[1,1] 预期：[1]
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for item in nums:
            if nums.count(item)>1:
                nums.remove(item)
        return len(nums)
```

### 2. https://leetcode-cn.com/submissions/detail/37359258/

`nums.count()` 的时间复杂度为 `O(n)`，因此下面代码整个的时间复杂度为`O(n^3)`，所以超出时间限制。
```python
# 160 / 161 个通过测试用例 状态：超出时间限制
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for item in nums:
            if nums.count(item)>1:
                while nums.count(item)>1:                    
                    nums.remove(item)
        return len(nums)
```


## 记录、比较、分析别人的Solution

## 其他

这一题前面提交的几次都是没通过，后面看了题解（使用**双指针**方法,之前没接触过这个概念）才写出来的。

[双指针概念](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/shan-chu-pai-xu-shu-zu-zhong-de-zhong-fu-xiang-by-/)