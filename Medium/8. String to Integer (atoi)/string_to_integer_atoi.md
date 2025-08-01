# 8. String to Integer (atoi)

**Difficulty**: Medium  
🔗 [View on LeetCode](https://leetcode.com/problems/string-to-integer-atoi/)
📄 [Solution File](./string_to_integer_atoi.py)

## 📝 Problem Statement

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.

### The algorithm:
1. **Ignore** any leading whitespaces.
2. **Check sign**: '+' or '-' (assume '+' if not present).
3. **Parse digits** from the string until a non-digit character or end of string.
4. **Clamp** the integer within the 32-bit signed range `[-2^31, 2^31 - 1]`.

---

## ✅ Constraints

- `0 <= s.length <= 200`
- `s` consists of English letters (upper/lower-case), digits (`0-9`), whitespace `' '`, `'+'`, `'-'`, and `'.'`

---

## 🧠 Intuition / Thought Process

- We parse the string character-by-character.
- We handle the whitespace, sign, and number parsing in sequence.
- We use overflow checks **before** multiplying and adding digits.
- Clamp the value at boundaries using `INT_MAX` and `INT_MIN`.

---

## 🔄 Pseudocode
```python
Set INT_MAX = 2^31 - 1, INT_MIN = -2^31
Trim leading whitespaces
Check for '+' or '-' sign
Parse digits and build number
If overflow, return clamped value
Return result with proper sign
```
---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n), where `n` is the length of the string
- **Space Complexity:** O(1), constant extra space

---

## ✅ Test Case Example

```python
Input: s = "   -042"
Output: -42

Input: s = "1337c0d3"
Output: 1337

Input: s = "words and 987"
Output: 0