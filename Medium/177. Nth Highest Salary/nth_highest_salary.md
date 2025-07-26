# 177. Nth Highest Salary

**Difficulty**: Medium  
🔗 [View on LeetCode](https://leetcode.com/problems/nth-highest-salary/)
📄 [Solution File](./nth_highest_salary.sql)


## 📝 Problem Statement

Write a solution to find the nth highest distinct salary from the `Employee` table.  
If there are less than `n` distinct salaries, return null.

### SQL Schema

```sql
Table: Employee

| Column Name | Type |
|-------------|------|
| id          | int  |
| salary      | int  |

id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
```

## ✅ Constraints

- id is the primary key.
- Salaries may be duplicated.
- n is a positive integer.

## 🧠 Intuition / Thought Process

- To find the Nth highest distinct salary, we need to:
- Eliminate duplicate salaries using DISTINCT.
- Sort the result in descending order to prioritize the highest salaries.
- Use OFFSET N-1 to skip the top N-1 salaries and get the Nth salary.
- We also need to handle the case where there are fewer than N distinct salaries — in that case, return NULL.

## 🔄 Pseudocode
```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE result INT;

  SET N = N - 1;

  SELECT DISTINCT salary
  INTO result
  FROM Employee
  ORDER BY salary DESC
  LIMIT 1 OFFSET N;

  RETURN result;
END;
```

## ⏱️ Time & Space Complexity

- Time Complexity: O(n log n) – due to sorting distinct salaries.

- Space Complexity: O(1) – no extra space used apart from function memory.

## ✅ Test Case Example
**Example 1:** 

**Input:**

Employee table:

| id | salary |
|----|--------|
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |

n = 2

**Output:**

| getNthHighestSalary(2) |
|------------------------|
| 200                    |

**Example 2:**

**Input:**

Employee table:

| id | salary |
|----|--------|
| 1  | 100    |

n = 2

**Output:**

| getNthHighestSalary(2) |
|------------------------|
| null                   |
