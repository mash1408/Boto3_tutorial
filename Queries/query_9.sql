USE classicmodels;
SELECT 
            SUM(quantityOrdered) AS sum, status,productCode
        FROM
            orderdetails
                INNER JOIN
            orders ON orderdetails.orderNumber = orders.orderNumber
        GROUP BY status
        HAVING sum > 500;