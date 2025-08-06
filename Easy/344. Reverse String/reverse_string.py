# LeetCode Problem 344: Reverse String
# Link: https://leetcode.com/problems/reverse-string/

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses the input list of characters in-place.
        :param s: List[str] - array of characters to be reversed
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]  # swap characters
            left += 1
            right -= 1

# Example test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    s1 = ["h", "e", "l", "l", "o"]
    sol.reverseString(s1)
    print(s1)  # Output: ['o', 'l', 'l', 'e', 'h']

    # Test case 2
    s2 = ["H", "a", "n", "n", "a", "h"]
    sol.reverseString(s2)
    print(s2)  # Output: ['h', 'a', 'n', 'n', 'a', 'H']
