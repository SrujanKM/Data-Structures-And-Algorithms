# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Pointer to place the next unique element
        j = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1

        return j
