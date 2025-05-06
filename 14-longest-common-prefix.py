import time


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        print(strs)
        if not strs:
            return ""

        commonPrefix = strs[0]

        for p in range(1, len(strs)):
            testString = strs[p]
            if not commonPrefix or not testString:
                return ""

            print(commonPrefix)
            print(testString)

            for i in range(len(commonPrefix)):
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
