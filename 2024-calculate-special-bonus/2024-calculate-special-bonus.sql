/* Write your T-SQL query statement below */
select employee_id, case
    when employee_id % 2 = 1 and name not like 'M%' then salary
    else 0
    end [bonus]
from employees
order by employee_id