use copang_main;

select i.id,
	   i.name,
       s.item_id,
       s.inventory_count
from item as i inner join stock s
on i.id = s.item_id;