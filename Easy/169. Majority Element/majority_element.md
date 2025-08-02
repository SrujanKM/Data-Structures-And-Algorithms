# 169. Majority Element

**Difficulty:** Easy  
🔗 [View on LeetCode](https://leetcode.com/problems/majority-element/)
📄 [Solution File](./majority_element.py)

---

## 📝 Problem Statement

Given an array `nums` of size `n`, return the **majority element**.

The majority element is the element that appears **more than ⌊n / 2⌋ times**.  
You may assume that the majority element **always exists** in the array.

---

## ✅ Constraints

- `n == nums.length`
- `1 <= n <= 5 * 10⁴`
- `-10⁹ <= nums[i] <= 10⁹`

---

## 🧠 Intuition / Thought Process

To find the majority element efficiently:

- The **Boyer-Moore Voting Algorithm** is optimal for this.
- It maintains a `candidate` and a `count`.
- If `count` is zero, we choose the current number as the new candidate.
- If the current number is the same as the candidate, we increase the count; otherwise, decrease it.
- Since a majority element is guaranteed to exist, this algorithm works perfectly.

---

## 🔄 Pseudocode
```python
Initialize count = 0
Initialize candidate = None

For each number in nums:
If count == 0:
candidate = num
If num == candidate:
count += 1
Else:
count -= 1

Return candidate
```
---

## ⏱️ Time & Space Complexity

- **Time Complexity:** `O(n)` — Single pass through the array.
- **Space Complexity:** `O(1)` — Constant space.

---

## ✅ Test Case Example

**Input:**  
`nums = [2,2,1,1,1,2,2]`

**Output:**  
`2`

**Explanation:**  
`2` appears 4 times which is more than `⌊7 / 2⌋ = 3`.
