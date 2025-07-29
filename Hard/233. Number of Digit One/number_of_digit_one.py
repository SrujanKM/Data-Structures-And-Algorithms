# Leetcode Problem 233: Number of Digit One
# Link: https://leetcode.com/problems/number-of-digit-one/

class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        position = 1
        
        while n // position > 0:
            higher = n // (position * 10)
            curr = (n // position) % 10
            lower = n % position
            
            if curr == 0:
                count += higher * position
            elif curr == 1:
                count += higher * position + lower + 1
            else:
                count += (higher + 1) * position
                
            position *= 10
        
        return count


if __name__ == "__main__":
    s = Solution()
    test_cases = [13, 0, 99, 100, 199]
    for n in test_cases:
        print(f"n = {n} → Count of 1s = {s.countDigitOne(n)}")
