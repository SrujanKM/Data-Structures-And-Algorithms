# 217. Contains Duplicate

🔗 [View on LeetCode](https://leetcode.com/problems/contains-duplicate/)

## 📝 Problem Statement

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

--- 
### Examples

**Example 1:**

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

**Example 2:**

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

**Example 3:**

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

---

## ✅ Constraints

- `1 <= nums.length <= 10⁵`  
- `-10⁹ <= nums[i] <= 10⁹`

---

## 🧠 Intuition / Thought Process

To determine whether there are duplicates in the list:
- A `set` in Python automatically removes duplicates.
- So if `len(set(nums))` is smaller than `len(nums)`, then there must be duplicates.

---

## 🔄 Pseudocode
``` python
Convert nums to a set
If length of set == length of original list:
return False (no duplicates)
Else:
return True (duplicates found)
```
---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)

Why?
- We iterate once through the array → O(n)
- The `set` may store up to n elements → O(n) space

---

## ✅ Test Case Example

```python
Input: [1, 2, 3, 1]
Output: True
