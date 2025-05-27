class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            while not self.isAlphaNumeric(s[left]):
                left += 1
            while not self.isAlphaNumeric(s[right]):
                right -= 1
            print(f"{s[left]} is alphanumeric -> {self.isAlphaNumeric(s[left])}")
            print(f"{s[right]} is alphanumeric -> {self.isAlphaNumeric(s[right])}")

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

    def isAlphaNumeric(self, char: str) -> bool:
        if ord(char) in range(65, 90):
            return True
        elif ord(char) in range(97, 122):
            return True
        elif ord(char) in range(48, 57):
            return True
        else:
            return False


s = "A man, a plan, a canal: Panama"
solution = Solution()
solution.isPalindrome(s)
