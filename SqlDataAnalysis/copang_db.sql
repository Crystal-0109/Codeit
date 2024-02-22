use copang_main;

select item.id,
	   item.name,
       stock.item_id,
       stock.inventory_count
from item left outer join stock
on item.id = stock.item_id;

select i.id,
	   i.name,
       s.item_id,
       s.inventory_count
from item as i right outer join stock s
on i.id = s.item_id;