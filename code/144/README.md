## 题目

[Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) <br/> [二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)

## 我的Solution

- [python](../144/144_binary_tree_preorder_traversal.py)

## 解题思路

### 1. [python](../144/144_binary_tree_preorder_traversal.py)的思路

1.1 没看题解前的思路

这个题开始不会做，是看了官方的思路才做出来的。最开始自己写的代码如下：
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node = root 
        result = []
        while node:
            result.append(node.val)
            if node.left:
                node = node.left   
            if node.right:
                node = node.right
        return result
            
```
没想到使用 `栈`，导致写着写着有点乱了。

1.2 看了官方题解的思路

前序遍历的顺序是：`top => bottom` 和 `left => right`

每次循环树的时候，使用 `stack.pop()` 出栈，获取最后的节点。

为什么要先判断 `node.right`是否为空 ? 因为栈的特点就是`后进先出`，而且前序遍历顺序是 `left => right`。所以需要右节点要`先`入栈，左节点`后`入栈，这样在出栈时左节点才会`先`出来。

[二叉树遍历学习笔记](https://github.com/dym0080/articles/blob/master/data-structure-and-algorithm/lcc06%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0-%E4%BA%8C%E5%8F%89%E6%A0%91.md)

## 提交未通过记录

## 记录、比较、分析别人的Solution

## 其他
