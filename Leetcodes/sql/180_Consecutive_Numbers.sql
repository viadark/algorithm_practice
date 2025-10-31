-- # Write your MySQL query statement below
-- 세번 이상 연속으로 나온 숫자들을 구하는 문제,
-- 생각보다 까다로웠다고 생각함
-- 3칸이 동일해야 해서 window function을 사용하려고 생각함
-- window function을 거친 3개의 결과중 min 값과 max값이 동일하면 3개의 값이 동일하다는 점을 이용
-- current 가 현재 row를 의미하고 2 following 이 앞선 2개의 행 이므로, 이렇게 3개의 행을 묶은 다음
-- min과 max를 비교 하도록 함. 또한 3개가 정확히 선택 되었는지를 확인하기 위해 count도 같이 진행함
select distinct(cnt) as ConsecutiveNums from (
select case when 
    min(num) over(
        rows between current row and 2 following
    ) = max(num) over (
        rows between current row and 2 following
    ) and count(num) over (
        rows between current row and 2 following
    ) = 3
    then num
    else null
    end
as cnt from Logs ) as a
where a.cnt is not null