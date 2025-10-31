-- salery가 나의 manager보다 높은 사람을 출력
-- 간단한 inner join 문제
select a.name as Employee from Employee a inner join Employee b on a.managerId = b.id where a.salary > b.salary