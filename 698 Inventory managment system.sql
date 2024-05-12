-- Create the database and switch to it
CREATE DATABASE sp2024bis698g3s;
USE sp2024bis698g3s;

-- Vendor table
CREATE TABLE IF NOT EXISTS Vendor (
    VendorID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    VendorName VARCHAR(100),
    ContactPerson VARCHAR(100),
    Email VARCHAR(100),
    UNIQUE INDEX uq_vendor_email (Email)
);

-- Customer table
CREATE TABLE IF NOT EXISTS Customer (
    CustomerID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(100),
    Address VARCHAR(255),
    PhoneNumber VARCHAR(15),
    UNIQUE INDEX uq_customer_phone (PhoneNumber)
);

-- Product table
CREATE TABLE IF NOT EXISTS Product (
    ProductID INT NOT NULL PRIMARY KEY,
    Name VARCHAR(100),
    Description TEXT,
    Quantity INT DEFAULT 0,
    Price DECIMAL(10, 2),
    Category VARCHAR(50),
    VendorID INT,
    FOREIGN KEY (VendorID) REFERENCES Vendor(VendorID),
    UNIQUE INDEX uq_product_name (Name)
);

-- Order table
CREATE TABLE IF NOT EXISTS `Order` (
    OrderID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    DeliveryDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    TotalAmount DECIMAL(10, 2),
    Quantity INT, -- New column to be updated by trigger
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- Employee table
CREATE TABLE IF NOT EXISTS Employee (
    EmployeeID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(100),
    Role VARCHAR(100),
    PhoneNumber VARCHAR(15),
    Email VARCHAR(100),
    PasswordHash VARCHAR(255),
    UNIQUE INDEX uq_employee_phone (PhoneNumber),
    UNIQUE INDEX uq_employee_email (Email)
);

-- Floor_Manager table
CREATE TABLE IF NOT EXISTS Floor_Manager (
    FloorManagerID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(100),
    Role VARCHAR(100),
    EmployeeID INT,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- Inventory table
CREATE TABLE IF NOT EXISTS Inventory (
    InventoryID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Location VARCHAR(255),
    Capacity INT,
    ProductID INT,
    FloorManagerID INT,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
    FOREIGN KEY (FloorManagerID) REFERENCES Floor_Manager(FloorManagerID),
    UNIQUE INDEX uq_inventory_location (Location)
);

-- Floor_Manager_Order table for orders placed by floor managers to vendors
CREATE TABLE IF NOT EXISTS Floor_Manager_Order (
    FloorManagerOrderID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    FloorManagerID INT,
    VendorID INT,
    OrderDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    DeliveryDate DATE,
    TotalAmount DECIMAL(10, 2),
    FOREIGN KEY (FloorManagerID) REFERENCES Floor_Manager(FloorManagerID),
    FOREIGN KEY (VendorID) REFERENCES Vendor(VendorID)
);

-- Order_Product table for many-to-many relationship between Order and Product
CREATE TABLE IF NOT EXISTS Order_Product (
    OrderID INT,
    ProductID INT,
    Quantity INT,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
    #FOREIGN KEY (OrderID) REFERENCES `Order`(OrderID)
);

-- Trigger to update inventory when an order is placed
-- Trigger to update inventory when an order is placed

-- Update Employee table to change all managers to floor managers using a KEY column in WHERE clause
UPDATE Employee
SET Role = 'Floor Manager'
WHERE Role = 'Manager' AND EmployeeID > 0;
