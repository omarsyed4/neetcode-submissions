# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = root.val

        def dfs(root):

            nonlocal res

            # Base case. 
            if not root:
                return 0

            # Find the left max and find the right max.
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Take the result and set it equal to the max with both of the roots subtrees 
            no_split = root.val + max(leftMax, rightMax)

            # Verify that it's greater than the root with its children. 
            split = root.val + leftMax + rightMax

            # Get the max between a split and a non-split. 
            res = max(res, split)

            return no_split
        
        dfs(root)
        return res













"""

We have to get the max path sum. 
Rules:
1. We can't traverse both the left and right children. We would have to traverse one or the other per parent node.
2. We can also just take the parent and its two children, and that could be a path.
3. We have to be wary of negative values. 

Visit each parent node, and for each subtree of that parent node, we should find the maximum path sum. 

Add the maximum path sum, whether it's on the left or the right. 

We should also check the case of whether allowing a split would be more 

And then evaluate that total sum on your way back up. 


"""