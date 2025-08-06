# 344. Reverse String

**Difficulty:** Easy  
🔗 [View on LeetCode](https://leetcode.com/problems/reverse-string/)
📄 [Solution File](./reverse_string.py)

## 📝 Problem Statement

Write a function that reverses a string.  
The input string is given as an array of characters `s`.  
You must do this by modifying the input array **in-place** with **O(1)** extra memory.

---

## ✅ Constraints

- 1 <= s.length <= 10⁵  
- `s[i]` is a printable ASCII character  
- Must be solved in-place with constant extra memory

---

## 🧠 Intuition / Thought Process

- Since strings are represented as character arrays, we can reverse them using the **two-pointer approach**.
- We swap characters from both ends, moving inward, until the `left` and `right` pointers meet or cross.

---

## 🔄 Pseudocode
```py
function reverseString(s):
left ← 0
right ← len(s) - 1

while left < right:
swap s[left] with s[right]
left ← left + 1
right ← right - 1
```
---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## ✅ Test Case Example

```python
Input:  s = ["h", "e", "l", "l", "o"]
Output: ["o", "l", "l", "e", "h"]

Input:  s = ["H", "a", "n", "n", "a", "h"]
Output: ["h", "a", "n", "n", "a", "H"]