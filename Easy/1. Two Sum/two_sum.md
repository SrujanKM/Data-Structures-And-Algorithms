# 1. Two Sum

**Difficulty:** Easy
🔗 [View on LeetCode](https://leetcode.com/problems/two-sum/)
📄 [Solution File](./two_sum.py)

## 📝 Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

---

### Example 1:

**Input:** nums = [2,7,11,15], target = 9  
**Output:** [0,1]  
**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].

### Example 2:

**Input:** nums = [3,2,4], target = 6  
**Output:** [1,2]

### Example 3:

**Input:** nums = [3,3], target = 6  
**Output:** [0,1]

---

## ✅ Constraints

- 2 <= nums.length <= 10⁴  
- -10⁹ <= nums[i] <= 10⁹  
- -10⁹ <= target <= 10⁹  
- Only one valid answer exists.

---

## 🧠 Intuition / Thought Process

We need to find two distinct indices whose elements add up to the target. The most efficient way is to use a hashmap to store each number and check if the complement (target - number) exists as we iterate.

---

## 🔄 Pseudocode
```python
Initialize an empty hashmap
For each index and number in nums:
Calculate complement = target - num
If complement exists in hashmap:
Return [index_of_complement, current_index]
Store num with its index in hashmap
```
---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n) — one pass through the list  
- **Space Complexity:** O(n) — for storing the hashmap

---

## ✅ Test Case Example

```python
Input: nums = [3, 2, 4], target = 6  
Output: [1, 2]