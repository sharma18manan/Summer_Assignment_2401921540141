class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root == None:
            return False

        targetSum = targetSum - root.val

        if root.left == None and root.right == None:
            return targetSum == 0

        left = self.hasPathSum(root.left, targetSum)
        right = self.hasPathSum(root.right, targetSum)

        return left or right