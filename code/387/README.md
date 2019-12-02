## 题目

[First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) <br/> [字符串中的第一个唯一字符](https://leetcode-cn.com/problems/first-unique-character-in-a-string/)

## 我的Solution

[python](../387/387_first_unique_character_in_a_string.py)

## 解题思路

### 1. [python](../387/387_first_unique_character_in_a_string.py.py)的思路

遍历字符串，判断当前字符串在整个字符串中的数量为1时，返回当前字符的位置。

## 提交未通过记录

### 1. https://leetcode-cn.com/submissions/detail/38574763/

因为 `s.count(s[i])` 的时间复杂度为 `O(n)`，放在 `for` 循环后整个的时间复杂度为 `O(n^2)`，所以超时。
```python
# 31 / 104 个通过测试用例 超出时间限制
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        for i in range(n):
            if s.count(s[i]) == 1:
                return i
        return -1
        
```

## 记录、比较、分析别人的Solution

## 其他

在[python](../387/387_first_unique_character_in_a_string.py.py)的解决方案中使用到了`collections.Counter(s)`转换为一个哈希表，非常有用，很好的解决了[这次提交](https://leetcode-cn.com/submissions/detail/38574763/)因为时间复杂度超出的问题。

```python
>>> s = "leetcode"
>>> collections.Counter(s)
Counter({'e': 3, 'l': 1, 't': 1, 'c': 1, 'o': 1, 'd': 1})
```