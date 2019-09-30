class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return 0
            if not (root.left or root.right):
                return 0

            l = 0
            r = 0
            if root.left:
                if root.val == root.left.val:
                    l = 1 + self.longestUnivaluePath(root.left)
                else:
                    self.longestUnivaluePath(root.left)
            if root.right:
                if root.val == root.right.val:
                    r = 1 + self.longestUnivaluePath(root.right)
                else:
                    self.longestUnivaluePath(root.right)
            nonlocal ans
            ans = max(ans, (l + r))
            return max(l, r)
        ans =0
        helper(root)
        return ans

