use copang_main;

# 평균, 최대, 최소 리뷰 개수
select avg(review_count), max(review_count), min(review_count)
from (select substring(address, 1, 2) as region,
			 count(*) as review_count
	  from review as r left outer join member as m
		   on r.mem_id  = m.id
	  group by substring(address, 1, 2)
	  having region is not null
	  and region != '안드') as review_count_summary;