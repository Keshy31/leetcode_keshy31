import time


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        char_list = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if char_list[left] in vowels and char_list[right] in vowels:
                char_list[left], char_list[right] = char_list[right], char_list[left]
                left += 1
                right -= 1
            elif char_list[left] not in vowels:
                left += 1
            elif char_list[right] not in vowels:
                right -= 1
        print("".join(char_list))

        return "".join(char_list)


s = "leetcode"

solution = Solution()

start_time = time.perf_counter_ns()
solution.reverseVowels(s)
end_time = time.perf_counter_ns()

elapsed_time = (end_time - start_time) / 100000

print(f"Execution time: {elapsed_time:.3f} milliseconds")
