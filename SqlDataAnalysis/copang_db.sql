USE copang_main;

select distinct(gender)
from member;

select distinct(address)
from member;

select distinct(substring(address, 1, 2))
from member;