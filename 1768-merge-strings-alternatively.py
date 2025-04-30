import time


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        merged = ""

        while p1 < len(word1) or p2 < len(word2):
            if p1 < len(word1):
                merged += word1[p1]
                p1 += 1
            if p2 < len(word2):
                merged += word2[p2]
                p2 += 1
            print(merged)
        return merged


word1 = "abcd"
word2 = "pq"

solution = Solution()
start_time = time.perf_counter_ns()
solution.mergeAlternately(word1, word2)
end_time = time.perf_counter_ns()

elapsed_time = (end_time - start_time) / 100000

print(f"Execution time: {elapsed_time:.2f} milliseconds")
