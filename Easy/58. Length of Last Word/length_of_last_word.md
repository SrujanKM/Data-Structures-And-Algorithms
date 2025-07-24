# Leetcode Problem 58: Length of Last Word

**Difficulty:** Easy  
🔗 [View on LeetCode](https://leetcode.com/problems/length-of-last-word/)
📄 [Solution File](./length_of_last_word.py)

---

## 📝 Problem Statement

Given a string `s` consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

---

## ✅ Constraints

- `1 <= s.length <= 10⁴`
- `s` consists of only English letters and spaces `' '`.
- There will be at least one word in `s`.

---

## 🧠 Intuition / Thought Process

- First, we remove any trailing or leading spaces using `.strip()`.
- Then we reverse the string to start counting from the end (i.e., last word).
- We count characters until we hit the first space, which marks the end of the last word.
- This approach is linear and handles edge cases efficiently (like multiple trailing spaces).

---

## 🔄 Pseudocode
```python
function lengthOfLastWord(s):
trim the input string
reverse the trimmed string
initialize count = 0
for each character in reversed string:
if character is not space:
increment count
else:
break the loop
return count
```
---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n), where n is the length of the string
- **Space Complexity:** O(1), only constant extra space is used

---

## ✅ Test Case Example

```python
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.