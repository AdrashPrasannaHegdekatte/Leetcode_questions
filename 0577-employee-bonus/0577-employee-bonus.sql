# Write your MySQL query statement below
SELECT e.name,b.bonus
FROM Employee AS e
LEFT JOIN Bonus as b
ON b.empid=e.empid
WHERE b.bonus<1000 or b.bonus IS NULL;