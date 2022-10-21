class Solution:
    def maxArea(self, height):
        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            cur_area = (r - l) * min(height[l], height[r])
            if cur_area > max_area:
                max_area = cur_area

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area

if __name__ == "__main__":
    sol = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(sol.maxArea(height))