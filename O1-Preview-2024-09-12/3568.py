class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1_str = str(num1).zfill(4)
        num2_str = str(num2).zfill(4)
        num3_str = str(num3).zfill(4)

        key_digits = []
        for i in range(4):
            min_digit = min(num1_str[i], num2_str[i], num3_str[i])
            key_digits.append(min_digit)

        key_str = ''.join(key_digits)
        return int(key_str)