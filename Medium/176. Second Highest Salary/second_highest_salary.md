# 176. Second Highest Salary

**Difficulty**: Medium  
🔗 [View on LeetCode](https://leetcode.com/problems/second-highest-salary/)
📄 [Solution File](./second_highest_salary.sql)


## 📝 Problem Statement

Write a solution to find the **second highest distinct salary** from the Employee table. If there is no second highest salary, return null.

**Table: Employee**

| Column Name | Type |
|-------------|------|
| id          | int  |
| salary      | int  |

- `id` is the primary key for this table.
- Each row of this table contains information about the salary of an employee.

---

## ✅ Constraints

- At least one row exists in the Employee table.
- Salary may contain duplicate values.
- Only distinct salaries should be considered.
- If no second highest exists, return `null`.

---

## 🧠 Intuition / Thought Process

- We want to fetch the **second highest distinct** salary from the Employee table.
- First, we **remove duplicates** using `DISTINCT`.
- Then we **sort** the values in descending order.
- We **skip the highest salary** using `OFFSET 1` and **limit the result to 1** row.
- We use `COALESCE(..., NULL)` to return `null` if no second highest exists.

---

## 🔄 Pseudocode
```sql
Select distinct salary from Employee
Order by salary descending
Skip the top 1 row (OFFSET 1)
Limit result to 1 row
If nothing returned, show NULL
```
---

## ⏱️ Time & Space Complexity

- **Time Complexity:** O(N log N) — due to sorting with `ORDER BY`.
- **Space Complexity:** O(1) — no extra space used apart from query processing.

---

## ✅ Test Case Example

### Example 1:
**Input:**

```sql
Employee table:
|----|--------|
| id | salary |
|----|--------|
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
|----|--------|

Output:

| SecondHighestSalary |
|---------------------|
| 200                 |


Example 2:
Input:

Employee table:
|----|--------|
| id | salary |
|----|--------|
| 1  | 100    |
|----|--------|

Output:

| SecondHighestSalary |
|---------------------|
| null                |