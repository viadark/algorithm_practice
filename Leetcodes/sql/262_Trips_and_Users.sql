-- 취소율을 추출해 내는 것 이지만,
-- 첫번째 조건으로 13년 10월 1일 부터 3일 까지라는 제약 사항이 있다 (제일 먼저 걸어야 할 조건)
-- 그 다음부턴 ban 된 사용자들은 아에 빼버리는 작업을 들어갔다 (cte를 이용해 밴 안된 이용자만 남김)
-- 그리고 날짜별로 group by를 해서 날짜별로 취소된 날짜와 총 날짜를 구해서 나누는 것으로 cancel rate를 구했다


with date_filter as (
    select * from Trips where request_at >= "2013-10-01" and request_at <= "2013-10-03"
),
trip_ban as (
    select a.id, a.client_id, a.driver_id, a.status as status, a.request_at from date_filter a join Users b on a.client_id = b.users_id where b.banned = "No"
),
trip_driver_ban as (
    select a.id, a.client_id, a.driver_id, a.status as status, a.request_at from trip_ban a join Users b on a.driver_id = b.users_id where b.banned = "No"
),
cancel_count as (
    select count(1) as cnt, request_at from (select * from trip_driver_ban where status="cancelled_by_driver" or status="cancelled_by_client") a group by request_at
),
total_count as (
    select count(1) as cnt, request_at from trip_driver_ban group by request_at
)
select a.request_at as Day, round(ifnull(b.cnt, 0) / a.cnt, 2) as 'Cancellation Rate' from total_count a left join cancel_count b on a.request_at = b.request_at