# 29. Divide Two Integers

**Difficulty**: Medium  
🔗 [View on LeetCode](https://leetcode.com/problems/divide-two-integers/)
📄 [Solution File](./divide_two_integers.py)

---

### 📝 Problem Statement

Given two integers dividend and divisor, divide two integers **without using multiplication, division, and mod operator**.

The integer division should **truncate toward zero**, which means losing its fractional part. For example, `8.345` would be truncated to `8`, and `-2.7335` would be truncated to `-2`.

Return the quotient after dividing dividend by divisor.

**Note:**  
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range:  
`[-2^31, 2^31 − 1]`.  
For this problem, if the quotient is **strictly greater than 2^31 − 1**, then return **2^31 − 1**, and if the quotient is **strictly less than -2^31**, then return **-2^31**.

---

### ✅ Constraints

- `-2^31 <= dividend, divisor <= 2^31 - 1`
- `divisor != 0`

---

### 🧠 Intuition / Thought Process

- We're restricted from using `*`, `/`, or `%`, so we simulate division using subtraction and bit shifts.
- We double the divisor (using `<<`) until it surpasses the dividend to subtract large chunks quickly.
- We carefully manage edge cases like:
  - **Overflow**: when dividend is `-2^31` and divisor is `-1`
  - **Sign management**: keep track of whether the result is negative or positive.

---

### 🔄 Pseudocode
```python
If dividend == INT_MIN and divisor == -1:
return INT_MAX

Determine if the result is negative:
If dividend < 0 xor divisor < 0:
negative = True
else:
negative = False

Convert both dividend and divisor to positive

Initialize quotient = 0

While dividend >= divisor:
temp = divisor
multiple = 1

While dividend >= (temp << 1):
    temp <<= 1
    multiple <<= 1

Subtract temp from dividend
Add multiple to quotient
Return -quotient if negative else quotient
```
---

### ⏱️ Time & Space Complexity

- **Time Complexity:** `O(log N)` — where N is the dividend, because we subtract using doubling.
- **Space Complexity:** `O(1)` — constant extra space.

---

### ✅ Test Case Example

```python
Input: dividend = 10, divisor = 3
Output: 3

Input: dividend = 7, divisor = -3
Output: -2