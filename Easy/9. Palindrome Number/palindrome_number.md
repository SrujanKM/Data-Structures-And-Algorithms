# Leetcode Problem 9: Palindrome Number

**Difficulty:** Easy  
**Link:** [Palindrome Number](https://leetcode.com/problems/palindrome-number/)

---

## ❓ Problem Statement

Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

---

## 📥 Examples

### Example 1:

Input: x = 121
Output: true
Explanation: Reads the same forwards and backwards.

### Example 2:

Input: x = -121
Output: false
Explanation: Reads 121- from the back.

### Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from the back.

---

## ✅ Constraints
- $-2^{31} \leq x \leq 2^{31} - 1$

---

## 🧠 Intuition / Thought Process

To check if an integer is a palindrome:

- A number is a palindrome if it reads the same forward and backward.
- Convert the integer to a string and reverse it.
- Compare the reversed string with the original string.
- If they match → it's a palindrome.

❗Note: Negative numbers are **never** palindromes because of the minus sign (`-`).

---

## 🔄 Pseudocode
```python
Convert integer x to a string strX
If strX is equal to reversed(strX):
return True
Else:
return False
```
---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n)

n is the number of digits in the integer.

String reversal and comparison both take O(n) time.

- **Space Complexity:** O(n)

A new string is created when converting the number and when reversing it.