-- Write your MySQL query statement below
-- Orders에 없는 Customers id를 찾으면 되는 쉬운 where절 연습 문제

select name as Customers from Customers where id not in (
select customerId from Orders )
-- distinct 안하는게 더 빠르다!...아닌가 비슷한가