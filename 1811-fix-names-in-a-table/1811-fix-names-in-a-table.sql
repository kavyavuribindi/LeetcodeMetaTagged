/* Write your T-SQL query statement below */

select user_id,
CONCAT(upper(left(name,1)),lower(right(name,len(name)-1))) AS name
from Users
order by user_id