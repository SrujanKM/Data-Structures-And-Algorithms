# 26. Remove Duplicates from Sorted Array

**Difficulty:** Easy  
🔗 [View on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

---

## 📝 Problem Statement

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

You must do this **without allocating extra space** for another array.

---

### Examples

**Example 1:**

Input: `nums = [1,1,2]`  
Output: `2, nums = [1,2,_]`

**Example 2:**

Input: `nums = [0,0,1,1,1,2,2,3,3,4]`  
Output: `5, nums = [0,1,2,3,4,_,_,_,_,_]`

---

## ✅ Constraints

- `1 <= nums.length <= 3 * 10⁴`  
- `-100 <= nums[i] <= 100`  
- `nums` is sorted in non-decreasing order

---

## 🧠 Intuition / Thought Process

- The array is already sorted, so duplicates will always be adjacent.
- Use two pointers:
  - `i` to traverse the array
  - `j` to place the next unique number
- Whenever we find a new unique number, we place it at index `j` and increment `j`.

---

## 🔄 Pseudocode
```python
if nums is empty:
return 0
initialize j = 1
for i from 1 to len(nums)-1:
if nums[i] != nums[i-1]:
nums[j] = nums[i]
j += 1
return j
```

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1) (in-place)

Why?
- Single traversal through the array → O(n)
- No extra data structures used

---

## ✅ Test Case Example

```python
Input: [0,0,1,1,1,2,2,3,3,4]
Output: 5
Only the first 5 elements of the modified array matter: [0, 1, 2, 3, 4]
