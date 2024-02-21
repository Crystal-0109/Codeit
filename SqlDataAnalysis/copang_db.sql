USE copang_main;

select *
from member
order by height asc;

select *
from member
order by height desc;

select *
from member
where gender = 'm' and weight >= 70
order by height asc;

select sign_up_day, email
from member
order by year(sign_up_day) desc, email asc;