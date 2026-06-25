class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root == None:
            return []

        ans = []
        queue = [root]
        left = True

        while queue:

            size = len(queue)
            level = []

            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if left == False:
                level.reverse()

            ans.append(level)
            left = not left

        return ans