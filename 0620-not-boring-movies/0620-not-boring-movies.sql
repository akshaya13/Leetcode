/* Write your T-SQL query statement below */
select id, movie, description, rating
from cinema
where not description = 'boring' and id % 2 = 1
order by rating desc