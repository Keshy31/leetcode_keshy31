import time


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        print(flowerbed)
        if not n:
            return True
        p = 0
        while p < len(flowerbed):
            if flowerbed[p] == 0 and flowerbed[p - 1] != 1 and flowerbed[p + 1] != 1:
                flowerbed[p] = 1
                n = n - 1
                if n == 0:
                    return True
            print(flowerbed[p])
            p += 1
        return False


flowerbed = [1, 0, 0, 0, 0, 1]
n = 2

start_time = time.perf_counter_ns()
solution = Solution()
print(solution.canPlaceFlowers(flowerbed, n))
end_time = time.perf_counter_ns()
elapsed_time = (end_time - start_time) / 100000
print(f"Elapsed time: {elapsed_time:.2f}ms")
