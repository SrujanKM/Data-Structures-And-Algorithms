# Leetcode Problem 179: Largest Number
# Link: https://leetcode.com/problems/largest-number/

from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        # Step 1: Convert integers to strings
        str_nums = list(map(str, nums))

        # Step 2: Sort with custom comparator
        sorted_nums = sorted(str_nums, key=cmp_to_key(compare))

        # Step 3: Join the result
        result = ''.join(sorted_nums)

        # Step 4: Handle leading zeros
        return result if result[0] != '0' else '0'


if __name__ == "__main__":
    sol = Solution()
    # Test Case 1
    print(sol.largestNumber([10, 2]))        # Output: "210"
    # Test Case 2
    print(sol.largestNumber([3,30,34,5,9]))  # Output: "9534330"
    # Edge Case
    print(sol.largestNumber([0, 0]))         # Output: "0"
