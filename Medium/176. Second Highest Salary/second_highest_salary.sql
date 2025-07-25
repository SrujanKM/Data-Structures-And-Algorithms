-- Leetcode Problem 176: Second Highest Salary
-- Link: https://leetcode.com/problems/second-highest-salary/

SELECT COALESCE((
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
), NULL) AS SecondHighestSalary;
