# Leetcode Problem 205: Isomorphic Strings
# Link: https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s_t = {}
        map_t_s = {}

        for c1, c2 in zip(s, t):
            if c1 in map_s_t:
                if map_s_t[c1] != c2:
                    return False
            else:
                map_s_t[c1] = c2

            if c2 in map_t_s:
                if map_t_s[c2] != c1:
                    return False
            else:
                map_t_s[c2] = c1

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isIsomorphic("egg", "add"))     # Output: True
    print(s.isIsomorphic("foo", "bar"))     # Output: False
    print(s.isIsomorphic("paper", "title")) # Output: True
    print(s.isIsomorphic("ab", "aa"))       # Output: False
