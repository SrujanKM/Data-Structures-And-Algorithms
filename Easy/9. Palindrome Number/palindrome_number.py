# Leetcode Problem 9: Palindrome Number
# Link: https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        return strX == strX[::-1]
