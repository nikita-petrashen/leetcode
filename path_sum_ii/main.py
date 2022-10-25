class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def compute_paths(root, target_sum, cur_sum, cur_path, paths):
    if root.left is None and root.right is None:
        if cur_sum + root.val == target_sum:
            paths.append(cur_path + [root.val])
    else:
        cur_sum += root.val
        cur_path.append(root.val)
        if root.left is not None:
            compute_paths(root.left, target_sum, cur_sum, cur_path, paths)

        if root.right is not None:
            compute_paths(root.right, target_sum, cur_sum, cur_path, paths)

        cur_path.pop(-1)

    return paths


class Solution:
    def pathSum(self, root, targetSum):
        if root is None:
            return []
        else:
            return compute_paths(root, targetSum, 0, [], [])


if __name__ == "__main__":
    sol = Solution()
    tree = TreeNode(val=5, left=TreeNode(val=4, left=TreeNode(val=11, left=TreeNode(val=7), right=TreeNode(val=2))),
                    right=TreeNode(val=8, left=TreeNode(val=13), right=TreeNode(val=4, left=TreeNode(val=5), right=TreeNode(val=1))))
    targetSum = 22
    print(sol.pathSum(tree, targetSum))
