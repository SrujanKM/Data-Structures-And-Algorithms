# 205. Isomorphic Strings

**Difficulty:** Easy  
🔗 [View on LeetCode](https://leetcode.com/problems/isomorphic-strings/)
📄 [Solution File](./isomorphic_strings.py)

---

## 📝 Problem Statement

Given two strings `s` and `t`, determine if they are **isomorphic**.

Two strings are isomorphic if the characters in `s` can be replaced to get `t`, with the following rules:

- All occurrences of a character must be replaced with **the same character**.
- The order of characters must be **preserved**.
- No two characters may map to the same character, but a character may map to itself.

---

## ✅ Constraints

- `1 <= s.length <= 5 * 10⁴`
- `t.length == s.length`
- `s` and `t` consist of any valid ASCII characters.

---

## 🧠 Intuition / Thought Process

To ensure isomorphism:
- Characters from `s` must map **one-to-one** with characters from `t`.
- We need **two mappings**:
  - `s -> t`
  - `t -> s` (to prevent multiple characters from mapping to the same character in `t`)
  
We iterate through both strings and:
- Check if the current mapping is consistent with previous mappings.
- If not, return `False`.

---

## 🔄 Pseudocode
```py
If lengths of s and t are not equal:
return False

Initialize two empty maps:
map_s_t = {}
map_t_s = {}

For each character pair (c1, c2) in s and t:
If c1 is in map_s_t and map_s_t[c1] != c2:
return False
If c2 is in map_t_s and map_t_s[c2] != c1:
return False

map_s_t[c1] = c2
map_t_s[c2] = c1
Return True
```
---

## ⏱️ Time & Space Complexity

- **Time Complexity:** `O(n)` — Single pass through the strings.
- **Space Complexity:** `O(n)` — For the two hash maps.

---

## ✅ Test Case Examples

### Example 1

**Input:**  
`s = "egg"`  
`t = "add"`

**Output:**  
`true`

**Explanation:**  
`e → a`, `g → d`

---

### Example 2

**Input:**  
`s = "foo"`  
`t = "bar"`

**Output:**  
`false`

**Explanation:**  
`o` would need to map to both `a` and `r`, which is not allowed.

---

### Example 3

**Input:**  
`s = "paper"`  
`t = "title"`

**Output:**  
`true`

**Explanation:**  
`p → t`, `a → i`, `e → l`, `r → e`