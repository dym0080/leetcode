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

### 1. 来源: [力扣（LeetCode）](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/er-cha-shu-de-qian-xu-bian-li-by-leetcode/)

> todo: 这个方法还需要再研究下

方法 ：莫里斯遍历
方法基于 莫里斯的文章，可以优化空间复杂度。算法不会使用额外空间，只需要保存最终的输出结果。如果实时输出结果，那么空间复杂度是 O(1)。

算法

算法的思路是从当前节点向下访问先序遍历的前驱节点，每个前驱节点都恰好被访问两次。

首先从当前节点开始，向左孩子走一步然后沿着右孩子一直向下访问，直到到达一个叶子节点（当前节点的中序遍历前驱节点），所以我们更新输出并建立一条伪边 `predecessor.right = root 更新这个前驱的下一个点。如果我们第二次访问到前驱节点，由于已经指向了当前节点，我们移除伪边并移动到下一个顶点。

如果第一步向左的移动不存在，就直接更新输出并向右移动。
```python
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node, output = root, []
        while node:  
            if not node.left: 
                output.append(node.val)
                node = node.right 
            else: 
                predecessor = node.left 

                while predecessor.right and predecessor.right is not node: 
                    predecessor = predecessor.right 

                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node  
                    node = node.left  
                else:
                    predecessor.right = None
                    node = node.right         

        return output
```

## 其他
