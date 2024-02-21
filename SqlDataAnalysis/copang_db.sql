USE copang_main;

select *
from member
where gender = 'm' and address like '서울%';

select *
from member
where gender = 'm' 
and address like '서울%'
and age between 25 and 29;

select *
from member
where month(sign_up_day) between 3 and 5
or month(sign_up_day) between 9 and 11;

select *
from member
where (gender = 'm' and height >= 180)
or (gender = 'f' and height >= 170);