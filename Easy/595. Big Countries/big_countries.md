# 595. Big Countries

**Difficulty**: Easy  
🔗 [View on LeetCode](https://leetcode.com/problems/big-countries/)
| 📄 [Solution File](./big_countries.py)

## 📝 Problem Statement

| Column Name | Type    |
|-------------|---------|
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |

name is the primary key (column with unique values) for this table.
Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.


A country is considered **big** if:

- It has an **area ≥ 3,000,000 km²**, or
- It has a **population ≥ 25,000,000**

You are given a table `World` with the following schema:

| Column Name | Type    |
|-------------|---------|
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |

Write a SQL and Pandas solution to find the **name, population, and area** of all the big countries.

Return the result table in **any order**.

---

## ✅ Constraints

- `name` is the **primary key**
- `area`, `population`, and `gdp` contain **positive integers**
- You may assume no null values

---

## 🧠 Intuition / Thought Process

We only need to:
- **Filter** the rows based on the `area` or `population` condition.
- **Select** the specific columns required in the output.

Since this is a **basic filtering and projection problem**, both SQL and Pandas solutions are straightforward.

---

## 🔄 Pseudocode

```py
For each row in the World table:
    If area >= 3000000 OR population >= 25000000:
        Include row in result

Return only 'name', 'population', 'area' columns
```
---

## ⏱️ Time & Space Complexity

- Time Complexity: O(n) – we perform a single pass to filter the records

- Space Complexity: O(n) – for storing the output result set

---

## ✅ Test Case Example

**Example 1:**

**Input:** 

| name        | continent | area    | population | gdp          |
|-------------|-----------|---------|------------|--------------|
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |

**Output:** 

| name        | population | area    |
|-------------|------------|---------|
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |