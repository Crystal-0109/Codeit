use copang_main;

select old.id as old_id,
	   old.name as old_name,
       new.id as new_id,
       new.name as new_name
from item as old left outer join item_new as new
on old.id = new.id;

select old.id as old_id,
	   old.name as old_name,
       new.id as new_id,
       new.name as new_name
from item as old right outer join item_new as new
on old.id = new.id;

select old.id as old_id,
	   old.name as old_name,
       new.id as new_id,
       new.name as new_name
from item as old inner join item_new as new
on old.id = new.id;

select * from item
union
select * from item_new;