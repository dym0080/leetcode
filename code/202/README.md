## 题目

[Happy Number](https://leetcode.com/problems/happy-number/) <br/> [快乐数](https://leetcode-cn.com/problems/xxhappy-numberx/)

## 我的Solution

[python](../202/202_happy_number.py)

## 解题思路

### 1. [python](../202/202_happy_number.py)的思路

这个题开始想着用递归来实现，但是发现太麻烦。于是看了 [金字塔下的小蜗牛的思路，C++版本](https://leetcode-cn.com/problems/happy-number/solution/shi-yong-kuai-man-zhi-zhen-si-xiang-zhao-chu-xun-h/) 才写出python版本的。

使用“快慢指针”思想找出循环：“快指针”每次走两步，“慢指针”每次走一步，当二者相等时，即为一个循环周期。此时，判断是不是因为1引起的循环，是的话就是快乐数，否则不是快乐数。

注意：此题不建议用集合记录每次的计算结果来判断是否进入循环，因为这个集合可能大到无法存储；另外，也不建议使用递归，同理，如果递归层次较深，会直接导致调用栈崩溃。不要因为这个题目给出的整数是int型而投机取巧。


## 提交未通过记录

## 记录、比较、分析别人的Solution

## 其他
