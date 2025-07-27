# 179. Largest Number

**Difficulty**: Medium  
🔗 [View on LeetCode](https://leetcode.com/problems/largest-number/)
📄 [Solution File](./largest-number.py)

---

### 📝 Problem Statement

Given a list of non-negative integers `nums`, arrange them such that they form the **largest number** and return it.

Since the result may be very large, you need to return a **string** instead of an integer.

---

### ✅ Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 10⁹`

---

### 🧠 Intuition / Thought Process

- The trick is in **arranging numbers** such that their **concatenation results in the largest value**.
- Compare combinations like `"30"+"3"` vs `"3"+"30"` to decide order.
- Use a **custom comparator** during sort to handle this string-based numerical ordering.
- Handle edge case where the result is multiple zeroes like `[0, 0]`, in which case return just `"0"`.

---

### 🔄 Pseudocode
```python
Convert all numbers to strings.
Sort using a custom comparator:
Compare combined results: x+y vs y+x
Join the sorted array.
If the result starts with '0', return '0' (to handle multiple zeros).
```

---

### ⏱️ Time & Space Complexity

- **Time Complexity:** `O(n log n)` (due to sorting)
- **Space Complexity:** `O(n)` (for storing string conversions)

---

### ✅ Test Case Example

**Input:**
nums = [3,30,34,5,9]

**Output:**
"9534330"