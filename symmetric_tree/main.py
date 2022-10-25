class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(q, mode):
    if q:
        yield q.val

        if mode == "left":
            if q.left is not None:
                yield from dfs(q.left, "left")
            else:
                yield "NULL"
            if q.right is not None:
                yield from dfs(q.right, "left")
            else:
                yield "NULL"

        else:
            if q.right is not None:
                yield from dfs(q.right, "right")
            else:
                yield "NULL"

            if q.left is not None:
                yield from dfs(q.left, "right")
            else:
                yield "NULL"
    else:
        yield "NULL"


class Solution:
    def isSymmetric(self, root):
        for l, r in zip(dfs(root.left, "left"), dfs(root.right, "right")):
            if l is None or r is None:
                return False
            if l != r:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()

    tree = TreeNode(val=2, left=TreeNode(val=3, left=TreeNode(val=4), right=TreeNode(val=5, left=TreeNode(val=8), right=TreeNode(val=9))),
                    right=TreeNode(val=3, left=TreeNode(val=5, left=TreeNode(val=9), right=TreeNode(val=8)), right=TreeNode(val=4)))
    print(sol.isSymmetric(tree))
