class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif (p is None and q is not None) or (p is not None and q is None):
            return False

        if p.val != q.val:
            return False
        else:
            p_left_val = p.left.val if p.left else None
            p_right_val = p.right.val if p.right else None
            q_left_val = q.left.val if q.left else None
            q_right_val = q.right.val if q.right else None

            if p_left_val == q_left_val and p_right_val == q_right_val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False


if __name__ == "__main__":
    sol = Solution()
    tree1 = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
    print(sol.isSameTree(tree1, tree1))
    tree2 = TreeNode(val=1, left=None, right=TreeNode(val=2))
    tree3 = TreeNode(val=1, left=TreeNode(val=2), right=None)
    print(sol.isSameTree(tree2, tree3))
