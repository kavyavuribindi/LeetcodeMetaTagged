/* Write your T-SQL query statement below */
-- delete from person
-- where id in 
-- (select a.id from (
-- select id, row_number() over (partition by email order by id)  as rn
-- from person)a
-- where a.rn>1)


-- delete from person
-- where
-- id not in(
-- select min(id) from person
-- group by email
-- )


-- with cte as (
--     select id, rank() over(partition by email order by id) as rnk
--     from person
-- )

-- delete from cte where rnk>1

with cte as (
    select id, row_number() over(partition by email order by id) as rn
    from person
)

delete from cte where rn>1