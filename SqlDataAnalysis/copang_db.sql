USE copang_main;

select *, length(address)
from member;

select email, upper(email)
from member;

select email, lower(email)
from member;

select email, lpad(age, 10, '0')
from member;

select email, rpad(age, 10, '!')
from member;