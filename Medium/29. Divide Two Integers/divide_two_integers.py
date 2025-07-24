# Leetcode Problem 29: Divide Two Integers
# Link: https://leetcode.com/problems/divide-two-integers/

from typing import List

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Edge case for overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign
        negative = (dividend < 0) != (divisor < 0)

        # Convert to positive
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1

            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1

            dividend -= temp_divisor
            quotient += multiple

        return -quotient if negative else quotient

if __name__ == "__main__":
    sol = Solution()
    print(sol.divide(10, 3))     # Output: 3
    print(sol.divide(7, -3))     # Output: -2
