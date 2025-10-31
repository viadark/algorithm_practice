-- 어제보다 온도가 증가한 날을 구하면 되는 문제
-- 우선 정렬을 한 다음, from 뒤에 2개 이상 들어가도 되는 것을 여기서 배움,
-- 두개를 넣게 되면 cartesian product로 도는듯?
-- 그래서 p1보다 p2가 높고 날짜의 차이가 하루만 나는 것을 추출하여 출력함

with sort_weather as (
    select * from Weather order by recordDate
)
select p2.id as id from sort_weather p1, sort_weather p2 where p1.temperature < p2.temperature and date_add(p1.recordDate, interval 1 day) = p2.recordDate