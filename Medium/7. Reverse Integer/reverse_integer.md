# 7. Reverse Integer

**Difficulty**: Medium  
🔗 [View on LeetCode](https://leetcode.com/problems/reverse-integer/)
📄 [Solution File](./reverse_integer.py)

---

## 📝 Problem Statement

Given a signed 32-bit integer `x`, return `x` with its digits reversed.  
If reversing `x` causes the value to go outside the signed 32-bit integer range [-2³¹, 2³¹ - 1], return 0.

Assume the environment **does not allow** you to store 64-bit integers.

---

## Examples

### Example 1:
Input: x = 123
Output: 321

### Example 2:
Input: x = -123
Output: -321

### Example 3:
Input: x = 120
Output: 21

---

## Constraints

- -2³¹ <= x <= 2³¹ - 1

---

## 🧠 Intuition / Thought Process

We reverse the digits of the integer using modular arithmetic:

1. **Extract digits**: Use `x % 10` to get the last digit and `x // 10` to reduce `x`.
2. **Overflow Check**: If the current reversed number is going to exceed 32-bit range after adding the new digit, return `0`.
3. **Rebuild number**: Multiply the current result by 10 and add the new digit.
4. **Sign Handling**: Track the original sign and apply it at the end.

**Important Check**:  
To avoid overflow:
```python
if result > (2**31 - 1) // 10 or (result == (2**31 - 1) // 10 and digit > 7):
    return 0
This handles values near 2147483647 (max 32-bit signed int).
```

---

## Time & Space Complexity:

Time Complexity: O(log₁₀(x)) – we process one digit at a time.

Space Complexity: O(1) – constant space.