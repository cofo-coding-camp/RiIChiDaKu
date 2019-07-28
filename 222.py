
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)

        return left + right + 1
    def BFS(self,root:TreeNode):
        if not root:
            return 0
        count = 0
        l = [root]
        while l:
            p = l.pop()#拿走并reutrn
            count += 1
            if p.left :
                l.append(p.left)
            if p.right :
                l.append(p.right)
        return count




