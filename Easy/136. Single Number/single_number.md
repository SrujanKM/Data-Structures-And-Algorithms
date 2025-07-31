# 136. Single Number

**Difficulty:** Easy  
🔗 [View on LeetCode](https://leetcode.com/problems/single-number/)
📄 [Solution File](./single_number.py)

## 📝 Problem Statement

Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.

You must implement a solution with:
- Linear runtime complexity
- Constant extra space

---

## ✅ Constraints

- 1 <= nums.length <= 3 * 10⁴  
- -3 * 10⁴ <= nums[i] <= 3 * 10⁴  
- Each element in the array appears twice except for one element which appears only once.

---

## 🧠 Intuition / Thought Process

- If all elements appear twice except one, we can use XOR.
- XOR of two same numbers is 0.
- XOR of a number with 0 is the number itself.
- Therefore, XOR all numbers; result will be the one that appears once.

---

## 🔄 Pseudocode
```python
initialize result = 0
for each number in nums:
result = result XOR number
return result
```
---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## ✅ Test Case Example

### Example 1
Input: nums = [2,2,1]  
Output: 1

### Example 2  
Input: nums = [4,1,2,1,2]  
Output: 4

### Example 3  
Input: nums = [1]  
Output: 1
