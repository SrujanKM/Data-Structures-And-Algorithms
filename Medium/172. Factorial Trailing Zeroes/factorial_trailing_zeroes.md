# 172. Factorial Trailing Zeroes

**Difficulty**: Medium  
🔗 [View on LeetCode](https://leetcode.com/problems/factorial-trailing-zeroes/)
📄 [Solution File](./factorial_trailing_zeroes.py)

---

## 📝 Problem Statement

Given an integer `n`, return the number of trailing zeroes in `n!`.

Note that `n! = n × (n - 1) × (n - 2) × ... × 3 × 2 × 1`.

---

## ✅ Constraints

- 0 <= n <= 10⁴

---

## 🧠 Intuition / Thought Process

- Trailing zeroes come from the number of times 10 is a factor in `n!`.
- A factor of 10 = 2 × 5.
- Since 2s are more common than 5s in prime factorizations, we only need to count how many times **5** is a factor in `n!`.
- This includes:
  - All multiples of `5` (like `5, 10, 15, ...`)
  - All multiples of `25`, `125`, etc. (which add **extra** 5s)

---

## 🔄 Pseudocode
```python
Initialize count = 0
while n > 0:
n = n // 5
count += n
return count
```
---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(log₅ n)
- **Space Complexity:** O(1)

---

## ✅ Test Case Example

### Example 1
**Input:** n = 3  
**Output:** 0  
**Explanation:** 3! = 6 → no trailing zero.

### Example 2  
**Input:** n = 5  
**Output:** 1  
**Explanation:** 5! = 120 → one trailing zero.