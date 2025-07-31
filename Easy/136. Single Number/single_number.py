# Leetcode Problem 136: Single Number
# Link: https://leetcode.com/problems/single-number/

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR operation
        return result


if __name__ == "__main__":
    sol = Solution()
    
    # ✅ Test Case 1
    print(sol.singleNumber([2, 2, 1]))  # Output: 1
    
    # ✅ Test Case 2
    print(sol.singleNumber([4, 1, 2, 1, 2]))  # Output: 4
    
    # ✅ Test Case 3
    print(sol.singleNumber([1]))  # Output: 1
