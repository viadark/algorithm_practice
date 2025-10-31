-- 부서별 top 3의 salery를 구하는 문제, 동일 salery일 경우 같이 다 출력
-- dense rank를 사용할 생각을 먼저 했으며, 부서별로 salery순으로 dense rank를 구한 다음
-- inner join 하여 rank가 1~3등 사이의 값을 구함

select b.name as Department, a.name as Employee, a.salary as Salary from (
select name, salary, departmentId, dense_rank() over(partition by departmentId order by salary desc) as rk from Employee) a inner join Department b on a.departmentId = b.id
where a.rk >= 1 and a.rk <= 3