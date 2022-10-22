from bisect import bisect, bisect_left


class Solution:
    def maxSlidingWindow(self, nums, k):
        window = sorted(nums[0:k])
        zero_idx = bisect_left(window, nums[0])
        res = []
        for i in range(len(nums) - k):
            res.append(window[-1])
            window.pop(zero_idx)
            insert_idx = bisect(window, nums[i + k])
            window.insert(insert_idx, nums[i + k])
            zero_idx = bisect_left(window, nums[i + 1])

        res.append(window[-1])

        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(sol.maxSlidingWindow(nums, k))