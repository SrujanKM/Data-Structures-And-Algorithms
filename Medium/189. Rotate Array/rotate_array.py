# LeetCode Problem 189: Rotate Array
# Link: https://leetcode.com/problems/rotate-array/

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotates the array to the right by k steps in-place.
        """
        n = len(nums)
        k %= n  # In case k > n

        def reverse(start: int, end: int) -> None:
            """Helper function to reverse elements between start and end."""
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Reverse the entire array
        reverse(0, n - 1)

        # Reverse the first k elements
        reverse(0, k - 1)

        # Reverse the rest
        reverse(k, n - 1)


if __name__ == "__main__":
    # ✅ Test Case 1
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(arr1, 3)
    print("Rotated Array 1:", arr1)  # Output: [5,6,7,1,2,3,4]

    # ✅ Test Case 2
    arr2 = [-1, -100, 3, 99]
    Solution().rotate(arr2, 2)
    print("Rotated Array 2:", arr2)  # Output: [3,99,-1,-100]
