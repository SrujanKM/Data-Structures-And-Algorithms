# 178. Rank Scores

**Difficulty**: Medium  
🔗 [View on LeetCode](https://leetcode.com/problems/rank-scores/)
📄 [Solution File](./rank_scores.sql)

## 📝 Problem Statement

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| score       | decimal |

id is the primary key (column with unique values) for this table.
Each row of this table contains the score of a game. Score is a floating point value with two decimal places.


Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:

- The scores should be ranked from the highest to the lowest.
- If there is a tie between two scores, both should have the same ranking.
- After a tie, the next ranking number should be the next consecutive integer value. No holes between ranks.
- Return the result table ordered by score in descending order.

### Example 1:

**Input:**  
Scores table:

| id | score |
|----|-------|
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |

**Output:**

| score | rank |
|-------|------|
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |

## ✅ Constraints

- `id` is the primary key.
- `score` is a floating point value with 2 decimal places.

## 🧠 Intuition / Thought Process

- Since we want to rank scores from **highest to lowest**, we use `ORDER BY score DESC`.
- We need to avoid gaps in ranks when scores tie — for that, `DENSE_RANK()` is perfect.
- A **window function** over `ORDER BY score DESC` gives us the exact required ranking.

## 🔄 Pseudocode
```sql
SELECT
score,
DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores;
```

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(N log N) due to internal sorting by SQL engine on `score DESC`.
- **Space Complexity:** O(N) to store intermediate ranking.

## ✅ Test Case Example

| id | score |
|----|-------|
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |

**Result:**

| score | rank |
|-------|------|
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |