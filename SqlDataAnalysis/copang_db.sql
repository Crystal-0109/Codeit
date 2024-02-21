USE copang_main;

select *
from member
order by sign_up_day desc
limit 10;

select *
from member
order by sign_up_day desc
limit 8, 2;