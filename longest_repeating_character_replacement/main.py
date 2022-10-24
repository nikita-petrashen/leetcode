from collections import Counter


def remove_from_counter(counter, c):
    if counter[c] == 1:
        counter.pop(c)
    else:
        counter[c] -= 1


class Solution:
    def characterReplacement(self, s, k):
        if k >= len(s):
            return len(s)
        cur_window_len = k if k != 0 else 1
        counter = Counter(s[:cur_window_len])
        max_len = cur_window_len
        cur_i = 0
        while cur_i + cur_window_len <= len(s):
            if cur_i + cur_window_len < len(s):
                added_c = s[cur_i + cur_window_len]
            else:
                added_c = None
            removed_c = s[cur_i]
            best_char_num = counter.most_common(1)[0][1]
            if cur_window_len - best_char_num <= k:
                cur_len = best_char_num + k
                if cur_len > max_len:
                    max_len = cur_len
                next_window_len = cur_window_len + 1
                next_i = cur_i
            else:
                remove_from_counter(counter, removed_c)
                next_i = cur_i + 1
                next_window_len = cur_window_len

            if cur_i + cur_window_len < len(s):
                counter[added_c] = counter.get(added_c, 0) + 1

            cur_i = next_i
            cur_window_len = next_window_len

        return min(max_len, len(s))


if __name__ == "__main__":
    sol = Solution()
    s = "ABAB"
    k = 2
    print(sol.characterReplacement(s, k))
    s = "AABABBA"
    k = 1
    print(sol.characterReplacement(s, k))
    s = "AAAA"
    k = 0
    print(sol.characterReplacement(s, k))
    s = "AABA"
    k = 0
    print(sol.characterReplacement(s, k))
    s = "ABAA"
    k = 0
    print(sol.characterReplacement(s, k))


