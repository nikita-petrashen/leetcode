from functools import reduce


class Solution:
    def singleNumber(self, nums):
        return reduce(lambda a, b: a ^ b, nums)


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 3, 2, 1, 4, 5, 6, 5, 6]
    print(sol.singleNumber(nums))

