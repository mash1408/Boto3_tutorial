USE classicmodels;
SELECT 
    *
FROM
    products
WHERE
    productCode IN (SELECT 
            productCode
        FROM
            orderDetails
        WHERE
            orderNumber IN (SELECT 
                    orderNumber
                FROM
                    orders
                WHERE
                    status = 'Shipped'));