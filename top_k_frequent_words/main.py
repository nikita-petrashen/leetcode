from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, words, k):
        word_counts = Counter(words)
        top_k = heapq.nlargest(k, sorted(word_counts.keys()), key=lambda key: word_counts[key])

        return top_k


if __name__ == '__main__':
    sol = Solution()
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 3
    print(sol.topKFrequent(words, k))

