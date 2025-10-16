class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for x in range(low, high + 1):
            s = str(x)
            if len(s) % 2 == 0:  # Only check even-length numbers
                mid = len(s) // 2
                left_sum = sum(int(d) for d in s[:mid])
                right_sum = sum(int(d) for d in s[mid:])
                if left_sum == right_sum:
                    count += 1
        return count