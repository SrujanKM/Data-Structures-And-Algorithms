# Leetcode Problem 172: Factorial Trailing Zeroes
# Link: https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count


if __name__ == "__main__":
    solution = Solution()
    
    print("Input: 3 => Output:", solution.trailingZeroes(3))     # Output: 0
    print("Input: 5 => Output:", solution.trailingZeroes(5))     # Output: 1
    print("Input: 0 => Output:", solution.trailingZeroes(0))     # Output: 0
