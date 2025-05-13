import time


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(s)
        print(t)
        if len(s) != len(t):
            return False
        left = {}
        right = {}
        for i in range(len(s)):
            left[s[i]] = left.get(s[i], 0) + 1
            right[t[i]] = right.get(t[i], 0) + 1
        print(left)
        print(right)
        if left == right:
            print(True)
            return True

        return False


s = "rat"
t = "car"

start_time = time.perf_counter_ns()
solution = Solution()
solution.isAnagram(s, t)
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000

print(f"Elapsed time: {elapsed_time:.2f}ms")
