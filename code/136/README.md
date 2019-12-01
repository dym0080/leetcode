## 题目

[Single Number](https://leetcode.com/problems/single-number/) <br/> [只出现一次的数字](https://leetcode-cn.com/problems/single-number/)

## 我的Solution

[python](../136/136_single_number.py)

## 解题思路

> 根据题目要求：你的算法应该具有线性时间复杂度 `O(n)`。 你可以不使用额外空间来实现吗？

由于必须要放在一个循环里面，所以时间复杂度为 `O(n)`，所以不能在循环里面去判断类似 `x in nums` 的查找操作了，这个操作也是 `O(n)` 的时间复杂度，因为这样的话会超时。

## 提交未通过记录

### 第一次提交：

想先排序，再比较找出，未考虑全面。

```python
# https://leetcode-cn.com/submissions/detail/37961413/
# 1 / 16 个通过测试用例 状态：执行出错
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        while i < len(nums):
            if nums[i] != nums[i+1] :
                return nums[i]
            i +=1
    
```

### 第二次提交：

在第一次提交基础上加入了`nums`只有一个元素的判断而已

```python
# https://leetcode-cn.com/submissions/detail/37961633/
# 6 / 16 个通过测试用例 状态：解答错误
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        i = 0
        while i < len(nums):
            if nums[i] != nums[i+1] :
                return nums[i]
            i +=1
```
### 第三次提交：

`nums.count(item)` 的时间复杂度为 `O(n)`，放在 `for` 循环后整个时间复杂度为 `O(n^2)`，所以超时。

```python
# https://leetcode-cn.com/submissions/detail/37963806/
# 15 / 16 个通过测试用例 状态：超出时间限制
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for item in nums:
            if nums.count(item) ==1:
                return item
    
```


## 记录、比较、分析别人的Solution


### Solution1

> 来源：[leetcode-cn](https://leetcode-cn.com/problems/single-number/solution/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode/)

使用数学概念 `2∗(a+b+c)−(a+a+b+b+c)=c`

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)

```
- 时间复杂度：`O(n + n) = O(n)` 。`sum` 会调用 `next` 将 `nums` 中的元素遍历一遍。我们可以把上述代码看成 `sum(list(i, for i in nums))` ，这意味着时间复杂度为 `O(n)` ，因为 `nums` 中的元素个数是 nn 个。
- 空间复杂度： `O(n+n)=O(n)` 。 `set` 需要的空间跟 `nums` 中元素个数相等。


