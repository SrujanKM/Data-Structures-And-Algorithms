-- Leetcode Problem 177: Nth Highest Salary
-- Link: https://leetcode.com/problems/nth-highest-salary/

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
