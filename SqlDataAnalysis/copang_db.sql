USE copang_main;

select email, concat(height, 'cm', ', ', weight, 'kg') as '키와 몸무게', weight / ((height / 100) * (height / 100)) as BMI,
(case
	when weight is null or height is null then '비만 여부 알 수 없음'
    when weight / ((height / 100) * (height / 100)) >= 25 then '과체중 또는 비만'
    when weight / ((height / 100) * (height / 100)) >= 18.5
		 and weight / ((height / 100) * (height / 100)) < 25
         then '정상'
	else '저체중'
end) as obesity_check
from member
order by obesity_check;