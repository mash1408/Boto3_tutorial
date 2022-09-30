USE classicmodels;

SELECT 
            sum(amount) as total, customernumber
        FROM
            payments group by customernumber order by total desc limit 1;