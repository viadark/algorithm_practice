-- Write your MySQL query statement below
-- 2번째 salary 출력, 없으면 Null 출력
-- rank를 이용 하려고 접근 했음. CTE를 통해 Rank를 우선 구한 후, rank가 2인 애를 뽑았고,
-- 2등이 존재하지 않을 경우 null을 출력해야 했으므로 case when을 사용함
with ranktable as (
    select salary, rank() over(order by salary desc) as rk from Employee group by salary order by salary desc
)
select case when count(1) = 0 then null
        else salary
        end as SecondHighestSalary
from ranktable where rk = 2;