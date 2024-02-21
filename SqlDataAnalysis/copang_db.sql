USE copang_main;

select substring(address, 1, 2) as region, gender, count(*)
from member
group by substring(address, 1, 2), gender
with rollup
having region is not null
order by region asc, gender desc;