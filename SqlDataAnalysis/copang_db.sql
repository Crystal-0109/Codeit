USE copang_main;

select *
from member
where year(birthday) = '1992';

select *
from member
where month(sign_up_day) in (6, 7, 8);

select *
from member
where dayofmonth(sign_up_day) between 15 and 31;

select email, sign_up_day, curdate(), datediff(sign_up_day, curdate())
from member;

select email, sign_up_day, datediff(sign_up_day, birthday) / 365
from member;

select email, sign_up_day, date_add(sign_up_day, interval 300 day)
from member;

select email, sign_up_day, date_sub(sign_up_day, interval 250 day)
from member;

select email, sign_up_day, from_unixtime(unix_timestamp(sign_up_day))
from member;
