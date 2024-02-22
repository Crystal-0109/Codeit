use copang_main;

select i.id, i.name, avg(star)
from item as i left outer join review as r on r.item_id = i.id
     left outer join member as m on r.mem_id = m.id
where m.gender = 'f'
group by i.id, i.name
order by avg(star) desc;