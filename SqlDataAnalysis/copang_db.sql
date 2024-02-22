use copang_main;

select i.name, i.id,
	   r.item_id, r.star, r.comment, r.mem_id,
       m.id, m.email
from item as i left outer join review as r on r.item_id = i.id
     left outer join member as m on r.mem_id = m.id;