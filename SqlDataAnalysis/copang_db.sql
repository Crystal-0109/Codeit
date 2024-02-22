use copang_main;

# 리뷰가 최소 3개 이상 달린 상품들의 정보 조회
select *
from item
where id in (select item_id
			 from review
             group by item_id
             having count(*) >= 3);