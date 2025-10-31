-- # Write your MySQL query statement below
-- dense rank만 구하면 되는 문제
select score, dense_rank() over(order by score desc) as `rank` from Scores