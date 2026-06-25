class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def check(left, right):

            if left == None and right == None:
                return True

            if left == None or right == None:
                return False

            if left.val != right.val:
                return False

            a = check(left.left, right.right)
            b = check(left.right, right.left)

            return a and b

        return check(root.left, root.right)