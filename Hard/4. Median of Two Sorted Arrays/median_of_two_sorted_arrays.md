# 4. Median of Two Sorted Arrays

**Difficulty:** Hard
🔗 [View on LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/)
📄 [Solution File](./median_of_two_sorted_arrays.py)

## 📝 Problem Statement

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

---

## ✅ Constraints

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

---

## 🧠 Intuition / Thought Process

- Since both arrays are sorted, we can **merge them** into one sorted list and then compute the median.
- If the total length is odd: median = middle element.
- If the total length is even: median = average of the two middle elements.
- While this is not O(log(m+n)), it's a simple and intuitive solution.

---

## 🔄 Pseudocode
``` python
Merge the two sorted arrays into one
Find the length of the merged array
If odd, return the middle element
If even, return the average of the two middle elements
Round the result to 5 decimal places
```
---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(n log n) – for sorting the merged array
- **Space Complexity:** O(n) – to store the merged array

---

## ✅ Test Case Example

```python
Input: nums1 = [1, 3], nums2 = [2]
Output: 2.00000