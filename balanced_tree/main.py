class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def compare_subtrees_height(root):
    if root is None:
        return True
    if root.left is None:
        left_height = 0
    else:
        left_height = compare_subtrees_height(root.left)

    if root.right is None:
        right_height = 0
    else:
        right_height = compare_subtrees_height(root.right)

    if left_height is None or right_height is None or abs(left_height - right_height) > 1:
        return None
    else:
        return 1 + max(left_height, right_height)


class Solution:
    def isBalanced(self, root):
        return compare_subtrees_height(root) is not None


if __name__ == "__main__":
    sol = Solution()
    tree = TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))
    print(sol.isBalanced(tree))
