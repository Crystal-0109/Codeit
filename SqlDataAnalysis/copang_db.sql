use copang_main;

# 전체 상품의 평균 가격보다 높은 가격을 가진 상품 조회
select id, name, price,
	   (select avg(price) from item) as 'avg_price'
from item
where price > (select avg(price) from item);

# 가장 비싼 상품 조회
select id, name, price
from item
where price = (select max(price) from item);

# 최저가 상품 조회
select id, name, price
from item
where price = (select min(price) from item);