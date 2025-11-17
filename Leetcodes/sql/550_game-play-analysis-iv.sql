-- Activity
-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | player_id    | int     |
-- | device_id    | int     |
-- | event_date   | date    |
-- | games_played | int     |
-- +--------------+---------+
-- 첫번째로 로그인 하고, 그 직후 다음날에 한번 더 로그인 한 player 수를 찾고 이를 전체 player 수로 나누어라

with accept_players as (
    select player_id, min(event_date) as event_date from Activity group by player_id
)
select round(b.cnt / count(distinct(orig.player_id)), 2) as fraction from Activity orig, (select count(a.player_id) as cnt from Activity a inner join accept_players b on a.player_id = b.player_id and a.event_date = date_add(b.event_date, interval 1 day)) b