-- What is the name of the table that holds the items Northwind sells?
-- Products table has all the information about the products that Northwind sells.

-- What is the name of the table that holds the types/categories of the items Northwind sells?
-- 'Categories' table holds all the catgories with their IDs names, description and picture.

SELECT *
FROM Employees
-- Who is the Northwind employee whose name makes it look like she’s a bird? Include the answer as a comment underneath the SELECT statement
-- Peacock Margaret has a name of a bird.as

SELECT *
FROM Products
LIMIT 10
-- 77 in total but I can use the option to limit to 10n rows from the toolbar, right next to run options.
-- We can also limit the search with our 'LIMIT' function, and use it with a specific number that we wanna return.

SELECT *
FROM Categories
-- CAtegory ID for seafood is 8

SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM Orders
LIMIT 50