USE copang_main;

select email, height as 키, weight as 몸무게, weight / ((height / 100) * (height / 100)) as BMI
from member;