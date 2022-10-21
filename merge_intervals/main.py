class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda intvl: intvl[0])
        i = 0
        while i < len(intervals) - 1:
            s1, f1 = intervals[i]
            s2, f2 = intervals[i + 1]
            if s2 <= f1:
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i, [s1, max(f1, f2)])
            else:
                i += 1

        return intervals


if __name__ == '__main__':
    sol = Solution()
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    print(sol.merge(intervals1))
    intervals2 = [[1,4],[4,5]]
    print(sol.merge(intervals2))

