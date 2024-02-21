USE copang_main;

select gender, count(*), avg(height), min(weight)
from member
group by gender;