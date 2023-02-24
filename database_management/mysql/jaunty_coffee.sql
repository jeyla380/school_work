-- Creating Tables
CREATE TABLE COFFEE_SHOP (
	shop_id INT,
    shop_name VARCHAR(50),
    city VARCHAR(50),
    state CHAR(2),
    
    PRIMARY KEY(shop_id)
);

CREATE TABLE EMPLOYEE (
  employee_id INT,
  first_name VARCHAR(30),
  last_name VARCHAR(30),
  hire_date DATE,
  job_title VARCHAR(30),
  shop_id INT,
  
  PRIMARY KEY(employee_id),
  FOREIGN KEY(shop_id) REFERENCES COFFEE_SHOP(shop_id)
 );

CREATE TABLE SUPPLIER (
	supplier_id INT,
    company_name VARCHAR(50),
    country VARCHAR(30),
    sales_contact_name VARCHAR(60),
    email VARCHAR(50) NOT NULL,
    
    PRIMARY KEY(supplier_id)
);
  
CREATE TABLE COFFEE (
	coffee_id INT,
    shop_id INT, 
    supplier_id INT, 
    coffee_name VARCHAR(30),
    price_per_pound NUMERIC(5, 2),
    
    PRIMARY KEY(coffee_id),
    FOREIGN KEY(shop_id) REFERENCES COFFEE_SHOP(shop_id),
    FOREIGN KEY(supplier_id) REFERENCES SUPPLIER(supplier_id)
);

-- Inserting data
INSERT INTO SUPPLIER(supplier_id, company_name, country, sales_contact_name, email)
VALUES
    (0, "Westrock Coffee Company, LLC", "United States", "Barrett's Coffee", "customerexpteam@westrockcoffee.com"),
    (1, "Collaborative Coffee Source", "Norway", "Epoch Coffee, Terrible Love, Civil Goat Coffee", "info@collaborativecoffeesource.com"),
    (2, "Melbourne Coffee Merchants", "Australia", "Houndstooth Coffee, Figure 8 Coffee Purveyors", "hello@melbournecoffeemerchants.com.au");

INSERT INTO COFFEE_SHOP(shop_id, shop_name, city, state)
VALUES
    (0, "Barrett's Coffee", "Austin", "TX"),
    (1, "Terrible Love", "Seattle", "WA"),
    (2, "Civil Goat Coffee", "Portland", "OR"),
    (3, "Epoch Coffee", "Atlanta", "GA"),
    (4, "Houndstooth Coffee", "Boise", "ID"),
    (5, "Figure 8 Coffee Purveyors", "Chicago", "IL");
    
INSERT INTO COFFEE(coffee_id, shop_id, supplier_id, coffee_name, price_per_pound)
VALUES
    (0, (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 1) ,(SELECT supplier_id FROM SUPPLIER WHERE supplier_id = 1), "Bakenke", 5.45),
    (1, (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 2), (SELECT supplier_id FROM SUPPLIER WHERE supplier_id = 1), "Nemba", 4.75),
    (2, (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 3), (SELECT supplier_id FROM SUPPLIER WHERE supplier_id = 1), "Halo Hartume", 4.60),
    (3, (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 0), (SELECT supplier_id FROM SUPPLIER WHERE supplier_id = 0), "Calahute", 5.15),
    (4, (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 4), (SELECT supplier_id FROM SUPPLIER WHERE supplier_id = 0), "La Providencia", 4.95),
    (5, (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 5), (SELECT supplier_id FROM SUPPLIER WHERE supplier_id = 2), "Nyarusiza", 5.30);
    
INSERT INTO EMPLOYEE(employee_id, first_name, last_name, hire_date, job_title, shop_id)
VALUES
    (0, "Jeffrey", "Bucher", "2015-06-23", "Assistant Store Manager", (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 0)),
    (1, "Evelyn", "Rourke", "2021-01-15", "Barista", (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 0)),
    (2, "Nick", "Mann", "2021-02-02", "Barista", (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 0)),
    (3, "Jack", "Hall", "2022-05-29", "Store Manager", (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 0)),
    (4, "Marie", "Cole", "2014-11-14", "Marketing Manager", (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 1)),
    (5, "Franklin", "Zuniga", "2016-04-25", "Assistant Store Manager", (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 1)),
    (6, "Charles", "Layne", "2020-05-11", "Barista", (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 1)),
    (7, "Michele", "Miller", "2020-12-15", "Barista", (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 1)),
    (8, "Howard", "Robinson", "2017-06-07", "Store Manager", (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 2)),
    (9, "Troy", "William", "2019-12-02", "Assistant Store Manager", (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 2)), 
    (10, "William", "Jackson", "2020-05-15", "Barista", (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 2)),
    (11, "Jamie", "Amos", "2022-04-25", "Social Media Manager", (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 3)),
    (12, "Maribel", "Pineda", "2022-05-05", "Store Manager", (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 3)),
    (13, "Trisha", "Marshall", "2022-08-12", "Barista", (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 3)),
    (14, "Kenneth", "Rockwood", "2018-04-16", "Marketing Manager", (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 4)),
    (15, "Amber", "Williams", "2019-12-05", "Barista", (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 4)),
    (16, "Mildred", "Vallo", "2018-10-06", "Assistant Store Manager", (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 5)),
    (17, "Yung", "Fuller", "2018-12-12", "Social Media Manager", (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 5)),
    (18, "Harriet", "Ayers", "2020-03-20", "Store Manager", (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 5)),
    (19, "Cathy", "Barrett", "2021-07-29", "Barista", (SELECT shop_id FROM COFFEE_SHOP WHERE shop_id = 5));

-- Create a view
CREATE VIEW EMPLOYEE_VIEW AS
SELECT employee_id, (CONCAT(first_name, " ", last_name)) AS employee_full_name, hire_date, job_title, shop_id FROM EMPLOYEE;

-- Create an index
CREATE INDEX index_coffee_name
ON COFFEE (coffee_name ASC);

EXPLAIN SELECT * FROM COFFEE
WHERE coffee_name = "Halo Hartume";

-- Create a SFW
SELECT employee_id, first_name, last_name, hire_date, job_title FROM EMPLOYEE
WHERE hire_date LIKE '2020%' ORDER BY last_name ASC;

-- Join EMPLOYEE, COFFEE, & COFFEE_SHOP tables
SELECT * FROM COFFEE_SHOP JOIN EMPLOYEE
ON COFFEE_SHOP.shop_id = EMPLOYEE.shop_id
JOIN COFFEE ON COFFEE_SHOP.shop_id = COFFEE.shop_id
LIMIT 7;
