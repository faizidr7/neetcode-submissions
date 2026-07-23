class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.res = True

        def dfs(curr):
            if not curr:
                return 0
            else:
                left = dfs(curr.left)
                right = dfs(curr.right)

                if abs(left - right) > 1:
                    self.res = False
                
                return 1 + max(left, right)
        
        dfs(root)
        return self.res