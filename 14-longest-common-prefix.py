import time


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        print(strs)
        if len(strs) == 0:
            return ""

        if len(strs[0]) == 0:
            return ""

        commonPrefix = strs[0]
        p = 1

        while p < len(strs) and len(commonPrefix) > 0:
            testString = strs[p]
            if len(testString) == 0:
                commonPrefix = ""
                break

            print(commonPrefix)
            print(testString)

            for i in range(0, len(commonPrefix), 1):
                if testString[i] != commonPrefix[i]:
                    commonPrefix = commonPrefix[0:i]
                    break
                elif i == len(testString) - 1:
                    commonPrefix = testString
                    break
            p += 1

        print(commonPrefix)

        return commonPrefix


strs = ["abab", "aba", ""]

start_time = time.perf_counter_ns()
solution = Solution()
solution.longestCommonPrefix(strs)
end_time = time.perf_counter_ns()

elapsed_time = (end_time - start_time) / 100000

print(f"Execution time: {elapsed_time:.2f} milliseconds")
