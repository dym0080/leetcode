# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        
        stack, result, node = [], [], root
        while stack or node:           
            while node:
                stack.append(node)
                node = node.left           
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result