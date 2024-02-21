USE copang_main;

select *
from member
where age >= 27;

select *
from member
where age between 30 and 39;

select *
from member
where age not between 30 and 39;

select *
from member
where sign_up_day > '2019-01-01';

select *
from member
where sign_up_day between '2018-01-01' and '2018-12-31';