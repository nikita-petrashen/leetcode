from bisect import bisect, bisect_left


class Solution:
    def medianSlidingWindow(self, nums, k):
        window = sorted(nums[0:k])
        medians = []
        i = 0
        while i + k <= len(nums):
            # get median
            if k % 2 == 0:
                medians.append((window[k//2] + window[k//2+1]) / 2)
            else:
                medians.append(window[k // 2])
            # make a step
            zero_idx = bisect_left(window, nums[i])
            window.pop(zero_idx)
            i += 1
            if i + k > len(nums):
                break
            insert_idx = bisect(window, nums[i+k-1])
            window.insert(insert_idx, nums[i+k-1])

        return medians


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(sol.medianSlidingWindow(nums, k))
