USE classicmodels;
Select * from customers where customerName like "%Ltd" and creditLimit > 100000 or customerName like "%Ideas%";