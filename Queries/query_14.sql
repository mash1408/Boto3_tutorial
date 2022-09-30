USE classicmodels;
SELECT
    productName,
    orderdetails.productCode,
    SUM(quantityOrdered)as q,
    SUM(quantityOrdered*priceEach) as sales
FROM
    orderdetails
        INNER JOIN
    orders ON orders.orderNumber = orderdetails.orderNumber
        INNER JOIN
    products ON products.productCode = orderdetails.productCode
-- WHERE
--       YEAR(shippedDate) = '2003'
GROUP BY orderdetails.productCode
ORDER BY q DESC