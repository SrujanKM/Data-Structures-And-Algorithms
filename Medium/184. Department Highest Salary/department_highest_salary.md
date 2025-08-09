# 184. Department Highest Salary

**Difficulty**: Medium  
🔗 [View on LeetCode](https://leetcode.com/problems/department-highest-salary/)
| 📄 [Solution File](./department_highest_salary.sql)

---

## 📝 Problem Statement

### Employee
| Column Name  | Type    | Description |
|--------------|---------|-------------|
| id           | int     | Primary key |
| name         | varchar | Employee's name |
| salary       | int     | Employee's salary |
| departmentId | int     | Foreign key to Department.id |

id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.

### Department
| Column Name  | Type    | Description |
|--------------|---------|-------------|
| id           | int     | Primary key |
| name         | varchar | Department's name |

id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.

Given two tables `Employee` and `Department`, write a solution to find employees who have the **highest salary** in each department.

Return the result table in any order.

---

## ✅ Constraints

- `id` in `Employee` is **unique**.
- `id` in `Department` is **unique**.
- `departmentId` in `Employee` references `Department.id`.
- Department name is **NOT NULL**.
- Multiple employees can have the same highest salary in the same department.

---

## 🧠 Intuition / Thought Process

We need to:
1. Find the **maximum salary** for each department.
2. Return **all employees** whose salary matches this maximum.
3. Include the department name alongside employee details.

**Approach:**
- Use a **subquery** to get `(departmentId, maxSalary)` for each department.
- Filter the `Employee` table based on these results.
- Join with the `Department` table to get department names.

---

## 🔄 Pseudocode
```sql
FOR each department in Department table:
FIND maxSalary = MAX(salary) from Employee table where departmentId matches
FOR each employee in Employee table with that departmentId:
IF employee.salary == maxSalary:
OUTPUT (DepartmentName, EmployeeName, Salary)
```
---

## ⏱️ Time & Space Complexity

- Time Complexity: O(N) — single pass for grouping, plus filtering.

- Space Complexity: O(1) — SQL uses constant space for joins (excluding output storage).

---

## ✅ Test Case Example

**Input:**

**Employee table:**

| id | name  | salary | departmentId |
|----|-------|--------|--------------|
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |

**Department table:**

| id | name  |
|----|-------|
| 1  | IT    |
| 2  | Sales |

**Output:** 

| Department | Employee | Salary |
|------------|----------|--------|
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |

**Explanation:** 
Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.