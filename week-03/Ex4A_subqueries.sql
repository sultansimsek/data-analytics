 -- 1. What is the product name(s) of the most expensive products?
-- ∗ HINT: Find the max price in a subquery and then use that value to find products
-- useful starting point.)
SELECT ProductName, (
SELECT MAX(UnitPrice) FROM Products
) AS max_price
FROM Products;

-- 2. What is the product name(s) and categories of the least expensive products?
-- ∗ HINT: Find the min price in a subquery and then use that in your more complex
-- query that joins products with categories.
SELECT ProductName, CategoryName, (
SELECT MIN(UnitPrice) FROM Products
) AS min_price
FROM Products 
     JOIN Categories 
     ON Products.CategoryID = Categories.CategoryID;


-- 3. What is the order id, shipping name and shipping address of all orders shipped via "Federal Shipping"?
-- ∗ HINT: Find the shipper id of "Federal Shipping" in a subquery and then use that
-- value to find the orders that used that shipper.
-- ∗ You do not need "Federal Shipping" to display in the results.
SELECT OrderID, ShipName, ShipAddress 
FROM Orders
JOIN (SELECT ShipperID 
FROM Shippers
WHERE CompanyName = 'Federal Shipping') AS compname
ON Orders.ShipVia = compname.ShipperID;


-- 4. What are the order ids of the orders that included "Sasquatch Ale"? 
-- ∗ HINT: Find the product id of "Sasquatch Ale" in a subquery and then use that value
-- to find the matching orders from the `order details` table.
-- additional columns as you work on creating the query to better understand how the query is working.
SELECT `Order Details`.OrderID
FROM `Order Details`
WHERE `Order Details`.ProductID = (
    SELECT Products.ProductID
    FROM Products
    WHERE Products.ProductName = 'Sasquatch Ale'
);

-- 5. What is the name of the employee that sold order 10266?
SELECT Employees.LastName, Employees.FirstName 
FROM Employees 
WHERE Employees.EmployeeID = (
SELECT Orders.EmployeeID 
FROM Orders
WHERE OrderID = 10266
);

-- 6. What is the name of the customer that bought order 10266?
SELECT ContactName 
FROM  Customers
WHERE CustomerID = (SELECT Orders.CustomerID
FROM Orders 
WHERE OrderID = 10266);



