USE classicmodels;
SELECT 
    priceEach * quantityOrdered
FROM
    orderDetails
WHERE
    orderNumber IN (SELECT 
            orderNumber
        FROM
            orders
        WHERE
            status = 'shipped');