USE copang_main;

select * 
from member
where gender != 'm';

select * 
from member
where gender <> 'm';

select * 
from member
where age in (20, 30);

select * 
from member
where email like 'c_____@%';