class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            print("gello")
            while not self.isAlphaNumeric(s[left]):
                print("test 1")
                left += 1
            while not self.isAlphaNumeric(s[right]):
                print("test 2")
                right -= 1
            print(f"{s[left]} is alphanumeric -> {self.isAlphaNumeric(s[left])}")
            print(f"{s[right]} is alphanumeric -> {self.isAlphaNumeric(s[right])}")

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

    def isAlphaNumeric(self, char: str) -> bool:
        print(f"Char is {char} and ord is {ord(char)} ")
        if ord(char) in range(65, 90):
            return True
        elif ord(char) in range(97, 122):
            return True
        elif ord(char) in range(48, 58):
            return True
        else:
            return False


s = "9,8"
solution = Solution()
print(solution.isPalindrome(s))
