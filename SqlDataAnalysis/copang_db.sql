use copang_main;

# 서브쿼리 중첩
select i.id, i.name, avg(star) avg_star, count(*) count_star
from item as i left outer join review as r on r.item_id = i.id
     left outer join member as m on r.mem_id = m.id
where m.gender = 'f'
group by i.id, i.name
having count(*) >= 2
	   and avg_star = (select max(avg_star)
					   from (select i.id, i.name, avg(star) as avg_star, count(*) as count_star
							 from item as i left outer join review as r on r.item_id = i.id
								  left outer join member as m on r.mem_id = m.id
							 where m.gender = 'f'
                             group by i.id, i.name
                             having count(*) >= 2
                             order by avg(star) desc, count(*) desc) as final)
order by avg(star) desc, count(*) desc;