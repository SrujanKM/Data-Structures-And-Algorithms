# Leetcode Problem 8: String to Integer (atoi)
# Link: https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)

        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check for optional sign
        sign = 1
        if i < n and s[i] in ['+', '-']:
            if s[i] == '-':
                sign = -1
            i += 1

        # Step 3: Convert digits to integer
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Step 4: Overflow check before updating num
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num


if __name__ == "__main__":
    sol = Solution()
    
    print(sol.myAtoi("42"))             # 42
    print(sol.myAtoi("   -042"))        # -42
    print(sol.myAtoi("1337c0d3"))       # 1337
    print(sol.myAtoi("0-1"))            # 0
    print(sol.myAtoi("words and 987"))  # 0