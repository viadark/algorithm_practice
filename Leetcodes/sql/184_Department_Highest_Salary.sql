-- Department에서 가장 높은 salery를 가진 사람을 출력하는 문제
-- 나의 풀이는 rank를 이용 하려고 했음 생각해보니 max만 구하면 됐었을듯
-- rank를 partition by 및 order by 하여 부서별로 1등을 구해서 출력하였음
-- rank 1 찾는 것 보다 아래의 솔루션 group by 하여 max를 구하는 것이 더 나은 풀이로 보임

# Write your MySQL query statement below
select c.Department, c.name as Employee, c.salary as Salary from (
select a.name as name, a.salary as salary, a.departmentId as departmentId, b.name as Department, rank() over(partition by a.departmentId order by a.salary desc) as rk from Employee a inner join Department b
on a.departmentId = b.id ) as c where c.rk = 1

-- Solution 1 Using JOIN
-- this is better...
-- SELECT D.name AS Department,
--        E.name AS Employee,
--        E.salary AS Salary
-- FROM Employee E
-- JOIN Department D
--   ON E.departmentId = D.id
-- WHERE (E.departmentId, E.salary) IN (
--     SELECT departmentId, MAX(salary)
--     FROM Employee
--     GROUP BY departmentId
-- );