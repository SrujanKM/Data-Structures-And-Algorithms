# Leetcode Problem 58: Length of Last Word
# Link: https://leetcode.com/problems/length-of-last-word/

from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        rev_s = s[::-1]
        count = 0
        for i in rev_s:
            if i != " ":
                count += 1
            else:
                break
        return count


if __name__ == "__main__":
    solution = Solution()

    # ✅ Test Case 1
    s1 = "Hello World"
    print(f"Input: '{s1}' | Output: {solution.lengthOfLastWord(s1)}")  # Output: 5

    # ✅ Test Case 2
    s2 = "   fly me   to   the moon  "
    print(f"Input: '{s2}' | Output: {solution.lengthOfLastWord(s2)}")  # Output: 4

    # ✅ Test Case 3
    s3 = "luffy is still joyboy"
    print(f"Input: '{s3}' | Output: {solution.lengthOfLastWord(s3)}")  # Output: 6
