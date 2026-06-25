class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = []

        def inorder(node):
            if node == None:
                return

            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        inorder(root)

        return ans