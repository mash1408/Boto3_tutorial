USE classicmodels;
SELECT 
    A.*
FROM
    customers A,
    customers B
WHERE
    A.CustomerNumber <> B.Customernumber
        AND A.City = B.City
        AND A.customerNumber IN (SELECT 
            customerNumber
        FROM
            orders
        WHERE
            orderNumber IN (SELECT 
                    a.orderNumber
                FROM
                    orderdetails a,
                    orderdetails b
                WHERE
                    a.orderNumber <> b.orderNumber
                        AND a.productCode = b.productCode));
