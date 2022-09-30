USE classicmodels;
SELECT 
    distinct a.firstName AS employeeName,
    c.contactFirstName AS customerName
FROM
    employees a,
    customers c
WHERE
    a.firstName = c.contactFirstName order by c.contactFirstName; 