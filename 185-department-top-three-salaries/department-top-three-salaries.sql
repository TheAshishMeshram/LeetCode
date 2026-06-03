SELECT
    d.Name AS Department,
    e.Name AS Employee,
    e.Salary
FROM Employee e
JOIN Department d
ON e.DepartmentId = d.Id
WHERE 3 > (
    SELECT COUNT(DISTINCT Salary)
    FROM Employee
    WHERE DepartmentId = e.DepartmentId
    AND Salary > e.Salary
);