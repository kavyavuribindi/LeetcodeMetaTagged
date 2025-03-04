/* Write your T-SQL query statement below */
delete from person
where id in 
(select a.id from (
select id, row_number() over (partition by email order by id)  as rn
from person)a
where a.rn>1)
