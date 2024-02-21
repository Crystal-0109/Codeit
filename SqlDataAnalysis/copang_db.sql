USE copang_main;

select avg(age)
from member;

select avg(age)
from member
where age between 5 and 100;

select *
from member
where address not like '%호';