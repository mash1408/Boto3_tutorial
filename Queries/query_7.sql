USE classicmodels;
SELECT 
    *
FROM
    customers
WHERE
    customerNumber NOT IN (SELECT 
            customerNumber
        FROM
            orders);