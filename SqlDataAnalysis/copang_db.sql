use copang_main;

select i.id, i.name, avg(star) as avg_star
from item as i left outer join review as r
on r.item_id = i.id
group by i.id, i.name
having avg_star < 3.7273
order by avg_star desc;

# 별점 확인
select avg(star) from review;

# 서브쿼리
select i.id, i.name, avg(star) as avg_star
from item as i left outer join review as r
on r.item_id = i.id
group by i.id, i.name
having avg_star < (select avg(star) from review)
order by avg_star desc;