USE classicmodels;
SELECT 
    SUM(quantityOrdered) AS s,
    orderdetails.productcode,
    productName
FROM
    orderdetails
        INNER JOIN
    orders ON orders.orderNumber = orderdetails.orderNumber
        INNER JOIN
    products ON products.productCode = orderdetails.productCode
WHERE
    YEAR(shippedDate)='2003'
GROUP BY orderdetails.productcode
ORDER BY s DESC
LIMIT 5;