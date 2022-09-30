USE classicmodels;
select * from
(SELECT 
    Year(orderYear) AS year,productLine, quantityOrdered * priceEach AS sales
FROM
    products
        INNER JOIN
    orderdetails ON products.productCode = orderdetails.productCode
        INNER JOIN
    orders ON orders.orderNumber = orderdetails.orderNumber) t1 
left JOIN
(SELECT 
    productLine, SUM(quantityOrdered * priceEach) AS salesSummarized
FROM
    products
        INNER JOIN
    orderdetails ON products.productCode = orderdetails.productCode
        INNER JOIN
    orders ON orders.orderNumber = orderdetails.orderNumber
GROUP BY productLine) t2
ON t1.productLine = t2.productLine ;
 
 
 
 