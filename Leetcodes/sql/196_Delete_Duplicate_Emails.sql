-- 중복된 email을 다 날리지만 이번 문제는 출력이 아니라 실제로 중복 된 이메일을 delete 문을 사용하여 삭제를 해야한다
-- 따라서 cte를 사용하여 중복된 email을 찾았으며, 그걸 이용하여 삭제 되어야 할 id를 찾았고,
-- 그 id를 이용하여 delete 구문을 사용하였다.

with dist_email as (
    select min(id) as id, email from Person group by email
),
delete_item as (
    select a.id as id from Person a join dist_email b
    on a.email = b.email
    where a.id <> b.id
)
delete from Person where id in (select id from delete_item)