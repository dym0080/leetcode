## 我的Solution

[python](https://github.com/dym0080/leetcode/blob/master/code/27/27_remove_element.py)

## 记录、比较、分析别人的解决方案

方案一：源自[leetcode-cn](https://leetcode-cn.com/explore/orignial/card/all-about-array/230/define-with-good-care/952/)

```python
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        i = -1
        # 定义nums[0...i]为非val的数列
        j = 0
        while j <= n-1:
            if nums[j] != val:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i+1
```
