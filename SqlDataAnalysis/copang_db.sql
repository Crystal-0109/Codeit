use copang_main;

# price 컬럼에서 최댓값을 구하는 서브쿼리
select id, name, price,
	   (select max(price) from item) as 'max_price'
from item;

# price 컬럼에서 평균을 구하는 서브쿼리
select id, name, price,
	   (select avg(price) from item) as 'avg_price'
from item;