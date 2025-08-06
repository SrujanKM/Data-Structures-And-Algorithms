# 197. Rising Temperature

**Difficulty**: Easy  
🔗 [View on LeetCode](https://leetcode.com/problems/rising-temperature/)
| [Solution File](./rising_temperature.sql)

## 📝 Problem Statement

| Column Name   | Type    |
|---------------|---------|
| id            | int     |
| recordDate    | date    |
| temperature   | int     |

id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.

Write a solution to find all dates' `id` with higher temperatures compared to its previous date (yesterday).

Return the result table in any order.

---

## ✅ Constraints

- `id` is the column with unique values for this table.
- There are no different rows with the same `recordDate`.
- The table contains information about the temperature on a certain day.

---

## 🧠 Intuition / Thought Process

- We need to compare each row's temperature with the previous day's temperature.
- If a row's temperature is higher than the previous day's, we include its `id`.
- This is a classic **self-join** scenario:
  - Join the table with itself where the `recordDate` of one is the day **after** the other.
  - Compare the temperatures accordingly.

---

## 🔄 Pseudocode

```sql
SELECT W1.id
FROM Weather W1
JOIN Weather W2
  ON W1.recordDate = DATE_ADD(W2.recordDate, INTERVAL 1 DAY)
WHERE W1.temperature > W2.temperature;
```
---

## ⏱️ Time & Space Complexity

- Time Complexity: O(n²) worst-case due to the self join.

- Space Complexity: O(1) – no extra storage used except output.


## ✅ Test Case Example

**Example 1:**

**Input:**

**Weather table:**

| id | recordDate | temperature |
|----|------------|-------------|
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |

**Output:** 

| id |
|----|
| 2  |
| 4  |

**Explanation:** 

- In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
- In 2015-01-04, the temperature was higher than the previous day (20 -> 30).