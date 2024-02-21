USE copang_main;

select substring(address, 1, 2) as region, count(*)
from member
group by substring(address, 1, 2);

select substring(address, 1, 2) as region, gender, count(*)
from member
group by substring(address, 1, 2), gender;