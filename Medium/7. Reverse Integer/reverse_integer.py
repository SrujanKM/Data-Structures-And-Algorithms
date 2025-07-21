# Leetcode Problem 9: Reverse Integer
# Link: https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x = x // 10

            # Check for 32-bit overflow before pushing the digit
            if result > (2**31 - 1) // 10 or (result == (2**31 - 1) // 10 and digit > 7):
                return 0

            result = result * 10 + digit

        return sign * result
