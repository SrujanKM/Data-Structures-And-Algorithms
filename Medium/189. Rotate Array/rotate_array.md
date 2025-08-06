# 189. Rotate Array

**Difficulty**: Medium  
🔗 [View on LeetCode](https://leetcode.com/problems/rotate-array/)
📄 [Solution File](./rotate_array.py)

## 📝 Problem Statement

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

**Example 1:**

**Input:** 
nums = [1,2,3,4,5,6,7], k = 3

**Output:** 
[5,6,7,1,2,3,4]

**Explanation:**

rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
**Example 2:**

**Input:** 
nums = [-1,-100,3,99], k = 2

**Output:** 
[3,99,-1,-100]

**Explanation:** 

rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

---

## ✅ Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

---

## 🧠 Intuition / Thought Process

The idea is to rotate the array to the right by `k` positions. Instead of rotating one-by-one, we use the **reverse approach**, which is optimal and in-place.

### Reverse Approach:
- Reverse the entire array
- Reverse the first `k` elements
- Reverse the remaining `n-k` elements

This works because reversing twice puts the segments in the correct order after shifting.

---

## 🔄 Pseudocode
```py
function rotate(nums, k):
n = length of nums
k = k % n // handle large k

reverse(nums, 0, n-1)
reverse(nums, 0, k-1)
reverse(nums, k, n-1)

function reverse(nums, start, end):
while start < end:
swap nums[start] and nums[end]
start += 1
end -= 1
```
---

## ⏱️ Time & Space Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)` (in-place)

---

## ✅ Test Case Example

```python
Input: nums = [1,2,3,4,5,6,7], k = 3  
Output: [5,6,7,1,2,3,4]

Input: nums = [-1,-100,3,99], k = 2  
Output: [3,99,-1,-100]