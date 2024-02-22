use copang_main;

# 뷰 생성
create view three_tables_joined as
select i.id, i.name, avg(star) as avg_star, count(*) as count_star
from item as i left outer join review as r on r.item_id = i.id
	 left outer join member as m on r.mem_id = m.id
where m.gender = 'f'
group by i.id, i.name
having count(*) >= 2
order by avg(star) desc, count(*) desc;

# 뷰 사용해서 별점의 평균값이 가장 높은 상품 조회
SELECT * 
FROM three_tables_joined
where avg_star = (select max(avg_star)
				  from three_tables_joined)
	  and count_star = (select max(count_star)
						from three_tables_joined);