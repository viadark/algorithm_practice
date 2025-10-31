-- function을 작성해야 했던 문제,
-- 입력받은 N번째의 salery를 출력하는 문제
-- subquery를 통해 우선 salery와 dense_rank를 구하도록 했고, 똑같이 구해진 결과값이 있으면 출력하고 아니면 null을 출력 하기 위해서
-- case when 구문을 사용함

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  
  RETURN (
      # Write your MySQL query statement below.
      select case when count(1) >= 1 then a.salary
      else Null end
      from (
        select salary, dense_rank() over(order by salary desc) as rk from Employee) a where a.rk = N
  );
END