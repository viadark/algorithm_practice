-- 2개 이상 중복된 email을 찾는 쿼리를 작성
-- 처음에는 distinct를 하려고 했지만 중복제거가 아니라 중복된 녀석을 찾아야 하기 떄문에
-- group by를 먼저 진행하고 그 count가 2 이상인 녀셕들만 출력함
select a.email from (
select email, count(1) as cnt from Person group by email) a where a.cnt >= 2