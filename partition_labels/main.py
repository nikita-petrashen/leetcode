from collections import Counter


def update_counter(counter, c):
    if c in counter:
        if counter[c] == 1:
            counter.pop(c)
        else:
            counter[c] -=1


class Solution:
    def partitionLabels(self, s):
        l, r = 0, 0
        counter = Counter(s)
        res = []
        while r < len(s):
            start = l
            while True:
                update_counter(counter, s[r])
                while s[r] in counter:
                    r += 1
                    update_counter(counter, s[r])

                while s[l] not in counter and l < r:
                    l += 1

                if r == l:
                    res.append(r-start+1)
                    r += 1
                    l += 1
                    break
                else:
                    r += 1

        return res

if __name__ == "__main__":
    sol = Solution()
    s = "ababcbacadefegdehijhklij"
    print(sol.partitionLabels(s))