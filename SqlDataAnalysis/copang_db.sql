USE copang_main;

select *
from member
where address is null;

select *
from member
where address is not null;

select *
from member
where address is null
or weight is null
or address is null;

select coalesce(height, '####'), coalesce(weight, '---'), coalesce(address, '@@@')
from member;