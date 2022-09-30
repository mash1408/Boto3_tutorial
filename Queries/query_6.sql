USE classicmodels;
SELECT 
    *
FROM
    products
WHERE
    productCode = (SELECT 
            productCode
        FROM
            orderDetails
        GROUP BY productCode
        ORDER BY COUNT(orderNumber) DESC
        LIMIT 1);