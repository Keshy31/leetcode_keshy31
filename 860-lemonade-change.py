class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        print(bills)
        till = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            print(f"Current bill: {bill}")
            match bill:
                case 5:
                    till[5] += 1
                case 10:
                    till[10] += 1
                    if till[5]:
                        till[5] -= 1
                    else:
                        return False
                case 20:
                    till[20] += 1
                    if till[10] and till[5]:
                        till[10] -= 1
                        till[5] -= 1
                    elif till[5] >= 3:
                        till[5] -= 3
                    else:
                        return False
            print(f"Till: {till}")

        return True


bills = [5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]

solution = Solution()
solution.lemonadeChange(bills)
