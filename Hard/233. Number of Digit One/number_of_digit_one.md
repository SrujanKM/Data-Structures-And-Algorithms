# 233. Number of Digit One

**Difficulty:** Hard
🔗 [View on LeetCode](https://leetcode.com/problems/number-of-digit-one/)
📄 [Solution File](./number_of_digit_one.py)

## 📝 Problem Statement  
Given an integer `n`, count the total number of digit `1` appearing in all non-negative integers less than or equal to `n`.

---

### ✅ Constraints
- `0 <= n <= 10⁹`

---

### 🧠 Intuition / Thought Process  
We process each digit place (units, tens, hundreds...) independently. For each digit, we divide the number into:
- `higher` digits (left to current digit),
- `curr` digit (current digit we are examining),
- `lower` digits (right of the current digit).

We calculate the number of `1`s contributed by the current digit using this strategy:
- If `curr == 0`: Only higher digits contribute.
- If `curr == 1`: Higher digits contribute + all lower values + 1.
- If `curr > 1`: Higher digits contribute one extra full set.

This greedy base-10 breakdown avoids iterating through all numbers up to `n`, achieving a logarithmic solution.

---

### 🔄 Pseudocode
```python
Initialize count = 0 and position = 1
While n divided by position > 0:
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
Return count
```
---

### ⏱️ Time & Space Complexity
- **Time Complexity:** O(log₁₀n) → We process digit by digit (at most 10 digits for 10⁹)
- **Space Complexity:** O(1) → Constant space

---

### ✅ Test Case Example

**Input:** `n = 13`  
**Output:** `6`  
**Explanation:**  
Numbers from 0 to 13 with digit 1 are:  
1, 10, 11, 12, 13 → Count = 6