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
        ORDER BY SUM(QuantityOrdered) DESC
        LIMIT 1);