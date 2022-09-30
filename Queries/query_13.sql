USE classicmodels;
SELECT * from products where productCode in 
(select productCode from orderdetails where orderNumber in 
(select ordernumber where "2003"in 
(select year(shippedDate) from orders )))
  and productCode in  (SELECT 
            productCode
        FROM
            orderDetails
        GROUP BY productCode
        ORDER BY SUM(QuantityOrdered) DESC
        LIMIT 5);