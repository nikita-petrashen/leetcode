class Solution:
    def search(self, nums, target) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m

        return -1


if __name__ == '__main__':
    sol = Solution()
    numss = [0, 1, 2, 3, 4, 5]
    targett = 5
    print(sol.search(numss, targett))
