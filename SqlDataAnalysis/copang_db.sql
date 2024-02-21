USE copang_main;

select email, height, weight, weight / ((height / 100) * (height / 100))
from member;