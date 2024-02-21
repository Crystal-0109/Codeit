USE copang_main;

select substring(address, 1, 2) as region, count(*)
from member
group by substring(address, 1, 2);

select substring(address, 1, 2) as region, gender, count(*)
from member
group by substring(address, 1, 2), gender
having region = '서울'
and gender = 'm';

select substring(address, 1, 2) as region, gender, count(*)
from member
group by substring(address, 1, 2), gender
having region is not null;

select substring(address, 1, 2) as region, gender, count(*)
from member
group by substring(address, 1, 2), gender
having region is not null
order by region asc, gender desc;