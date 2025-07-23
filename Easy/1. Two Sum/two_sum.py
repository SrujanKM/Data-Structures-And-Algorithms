# Leetcode Problem 1: Two Sum
# Link: https://leetcode.com/problems/two-sum/


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 4]
    target = 6
    result = sol.twoSum(nums, target)
    print(result)  # Expected Output: [1, 2]