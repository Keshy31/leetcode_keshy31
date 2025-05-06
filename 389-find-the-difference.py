import time


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t
        print(s)
        hashset = set(s)
        print(hashset)

        for i in range(len(t)):
            if t[i] not in hashset:
                print(t[i])
                return t[i]

        return ""


s = "a"
t = "aa"

start_time = time.perf_counter_ns()
solution = Solution()
solution.findTheDifference(s, t)
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000

print(f"Elapsed time: {elapsed_time:.2f}ms")
