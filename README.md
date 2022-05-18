# Shopify Data Science Challenge 2022
### By: Satrajit Chatterjee

<br>

## Question 1

### Provided data: 

- Number of sneaker shops: **100**
- Initial average order value (AOV): **$3145.13**

<br>

#### (A) Think about what could be going wrong with our calculation. Think about a better way to evaluate this data.

The data description confirms the fact that AOV is 3145.13. We can also note that the 75% percentile is at 390 but the max order amount is 704000. This means that there are obvious outliers that are causing the overall mean to be inflated. Similarly, there are orders where the total number of items are at 2000, which is much higher than the 75% percentile of 3 items. Visualizing this data gives us a better sense of the outlying entries in the dataset.

The box plots for `order_amount` confirm that there are outliers, where the graph has a much smaller range with `showfliers` set to `False`. Calculating the highest and lowest 5% percentiles, we can filter down the data to a much more reasonable range, in this case, between 122 and 640. Similarly, the box plots for `total_items` confirm that there are outliers as well, where we can filter down the data to a range between 1 and 4. 

Individual Order Value, or IOV, is a new attribute introduced to the data, which represents the order amount over the total number of items that are part of an order. The middle 90% quantile of IOV ranges bewteen 112 and 195. This contributes to the factors when creating a reliable data filter. This is better visualized in the Python Jupyter Notebook. 

<br>

#### (B) What metric would you report for this dataset?

Based on the outliers detection, it is clear that there are two major sets at play here. While there are some general outliers that must be filtered out for accurate calculations, there is some data with order amounts over 200000 that are large enough in number to be its own category, possibly for large businesses. The other general data falls in a second category for regular businesses. The current filtering process can be used to categorize the data into two main sections, the first one representing 0.34% of the orders, for large businesses, and the second one representing 85.42% of the orders, for regular businesses. The mean of the order amounts for each of the categories represents its respective AOV. 

<br>

#### (C) What is its value?

The description of the new data categories can now provide us with the correct AOVs. For each of the descriptions, the **means** define the AOVs. The AOVs for each of the categories are:
- *Regular businesses*: \$293.50
- *Large businesses*: \$704000.00

<br>
<br>

## Question 2

#### (a) How many orders were shipped by Speedy Express in total?

```sql
SELECT COUNT(*) as total FROM Orders o
INNER JOIN Shippers s ON o.ShipperID = s.ShipperID
WHERE ShipperName = 'Speedy Express';
```

*This returns the result:* 

| total |
| :--- |
| 54 |

**54** orders were shipped by Speedy Express in total.

---

#### (b) What is the last name of the employee with the most orders?

```sql
SELECT LastName from Orders o
INNER JOIN Employees e ON e.EmployeeID = o.EmployeeID
GROUP BY o.EmployeeID
ORDER BY count(DISTINCT OrderID) DESC
LIMIT 1;
```

*This returns the result:* 

| LastName |
| :--- |
| Peacock |

**Peacock** is the lastname of the employee with the most orders. 
If we add the count to the queried columns we get the total order count of **40**.

```sql
count(DISTINCT OrderID) as total -- added to previous query line 1
```

| LastName | total |
| :--- | :--- |
| Peacock | 40 |

---

#### (c) What product was ordered the most by customers in Germany?

Assuming that "most ordered product" refers to the total quantity of the product ordered, 

```sql
SELECT ProductName as product from OrderDetails od
INNER JOIN Products p ON p.ProductID = od.ProductID
INNER JOIN Orders o ON o.OrderID = od.OrderID
INNER JOIN Customers c ON c.CustomerID = o.CustomerID
WHERE c.Country = 'Germany'
GROUP BY od.ProductID
ORDER BY SUM(od.Quantity) DESC
LIMIT 1;
```

*This returns the result:* 

| product |
| :--- |
| Boston Crab Meat |

**Boston Crab Meat** is the most ordered product.
If we add the count to the queried columns we get the total order count of **160** orders.

```sql
SUM(od.Quantity) as total -- added to previous query line 1
```

| product | total |
| :--- | :--- |
| Peacock | 160 |

---