-- WAQ to list product id, name, unit price of every product, sort ascending in price
SELECT ProductID, ProductName, UnitPrice 
FROM Products
ORDER BY UnitPrice ASC 
-- WAQ showing products with at least 100 units on hand, from highest to lowest
SELECT ProductID, ProductName, UnitsInStock
FROM Products
WHERE UnitsInStock >= 100 
ORDER BY UnitsInStock DESC

-- WAQ showing products with at least 100 units on hand, from highest to lowest, if two  or more have same price, list in product name alphabetically
SELECT ProductID, ProductName, UnitsInStock
FROM Products
WHERE UnitsInStock >= 100 
ORDER BY UnitsInStock DESC, ProductName ASC

-- WAQ of total number of distinct customers who placed an order by customer id, use alias to label the count as CustomerCount, order the list by CustomerCount largest to smallest
SELECT CustomerID, COUNT(OrderID) AS CustomerCount 
FROM Orders
GROUP BY CustomerID 
Order by CustomerCount DESC

-- WAQ showing the products less than 25 units on hand, but 1 or more units of them in order, sort by quantity, high to low, then by product name
SELECT ProductName, UnitsInStock, UnitsOnOrder, QuantityPerUnit
FROM Products
WHERE UnitsInStock < 25 AND UnitsOnOrder > 1
ORDER BY QuantityPerUnit DESC, ProductName

-- WAQ to list each job title, along with how many employees hold each job title
SELECT DISTINCT Title, COUNT(EmployeeID) AS employedppl
FROM Employees
GROUP BY Title
ORDER BY employedppl 

-- WAQ showing the employees who have a monthly salary  that is betweeen 2000 and 2500, sort them by job title
SELECT EmployeeID, LastName, FirstName, Title, Salary
FROM Employees
WHERE Salary BETWEEN 2000 AND 2500
ORDER BY Title
