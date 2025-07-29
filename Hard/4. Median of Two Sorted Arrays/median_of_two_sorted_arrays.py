# Leetcode Problem 4: Median of Two Sorted Arrays
# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/


from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        n = len(nums3)

        if n % 2 == 0:
            mid = n // 2
            ans = (nums3[mid - 1] + nums3[mid]) / 2
        else:
            mid = n // 2
            ans = nums3[mid]

        return round(ans, 5)

if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 3]
    nums2 = [2]
    print("Merged:", sorted(nums1 + nums2))
    print("Median:", solution.findMedianSortedArrays(nums1, nums2))  # Expected: 2.00000

    nums1 = [1, 2]
    nums2 = [3, 4]
    print("Merged:", sorted(nums1 + nums2))
    print("Median:", solution.findMedianSortedArrays(nums1, nums2))  # Expected: 2.50000
