USE classicmodels;
select count(*) as count,lastname from employees group by lastname order by lastName;