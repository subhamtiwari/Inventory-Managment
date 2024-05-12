-- Dummy data for Vendor table
INSERT INTO Vendor (VendorName, ContactPerson, Email) VALUES
('ABC Supplies', 'John Doe', 'john.doe@abcsupplies.com'),
('XYZ Distributors', 'Jane Smith', 'jane.smith@xyzdistributors.com'),
('Acme Corp', 'Bob Johnson', 'bob.johnson@acmecorp.com'),
('Omega Inc', 'Sarah Lee', 'sarah.lee@omegainc.com'),
('Delta Solutions', 'Michael Brown', 'michael.brown@deltasolutions.com'),
('Gamma Tech', 'Emily Davis', 'emily.davis@gammatech.com'),
('Epsilon Enterprises', 'David Wilson', 'david.wilson@epsilonenterprises.com'),
('Zeta Innovations', 'Jessica Taylor', 'jessica.taylor@zetainnovations.com'),
('Eta Distributors', 'William Anderson', 'william.anderson@etadistributors.com'),
('Theta Supplies', 'Olivia Martinez', 'olivia.martinez@thetasupplies.com'),
('Iota Systems', 'Alexander Hernandez', 'alexander.hernandez@iotasystems.com'),
('Kappa Solutions', 'Isabella Diaz', 'isabella.diaz@kappasolusions.com'),
('Lambda Tech', 'Daniel Reyes', 'daniel.reyes@lambdatech.com'),
('Mu Enterprises', 'Sophia Morales', 'sophia.morales@muenterprises.com'),
('Nu Distributors', 'Jacob Gutierrez', 'jacob.gutierrez@nudistributors.com'),
('Xi Innovations', 'Mia Ramirez', 'mia.ramirez@xiinnovations.com'),
('Omicron Supplies', 'Ethan Flores', 'ethan.flores@omicronsupplies.com'),
('Pi Solutions', 'Isabella Castillo', 'isabella.castillo@pisolutions.com'),
('Rho Tech', 'Liam Jimenez', 'liam.jimenez@rhotech.com'),
('Sigma Enterprises', 'Emma Vargas', 'emma.vargas@sigmaenterprises.com');

-- Dummy data for Customer table
INSERT INTO Customer (FullName, Address, PhoneNumber) VALUES
('Customer A', '123 Main St, Anytown USA', '555-1234'),
('Customer B', '456 Oak Rd, Somewhere City', '555-5678'),
('Customer C', '789 Maple Ave, Elsewhere Town', '555-9012'),
('Customer D', '321 Elm St, Somewhere Else', '555-2468'),
('Customer E', '654 Pine Rd, Another Town', '555-7890'),
('Customer F', '987 Birch Ln, Somewhere Else', '555-3456'),
('Customer G', '159 Willow Dr, Anytown', '555-8902'),
('Customer H', '753 Maple Blvd, Somewhere City', '555-4567'),
('Customer I', '357 Oak Ave, Elsewhere Town', '555-2109'),
('Customer J', '951 Elm Ct, Another Town', '555-6789'),
('Customer K', '753 Pine St, Anytown USA', '555-0123'),
('Customer L', '159 Birch Rd, Somewhere City', '555-8766'),
('Customer M', '357 Willow Ln, Elsewhere Town', '555-4322'),
('Customer N', '951 Maple Dr, Another Town', '555-9877'),
('Customer O', '753 Oak Ave, Anytown', '555-5433'),
('Customer P', '159 Elm St, Somewhere City', '555-1099'),
('Customer Q', '357 Pine Rd, Elsewhere Town', '555-7655'),
('Customer R', '951 Birch Blvd, Another Town', '555-3211'),
('Customer S', '753 Willow Ct, Anytown USA', '555-9088'),
('Customer T', '159 Maple Ln, Somewhere City', '555-6544');

-- Dummy data for Product table
INSERT INTO Product (ProductID, Name, Description, Quantity, Price, Category, VendorID) VALUES
(1, 'Widget A', 'A high-quality widget', 50, 9.99, 'Electronics', 1),
(2, 'Gadget X', 'A useful gadget', 25, 19.99, 'Electronics', 2),
(3, 'Gizmo Z', 'An innovative gizmo', 75, 14.99, 'Tools', 3),
(4, 'Doohickey B', 'A versatile doohickey', 40, 12.99, 'Hardware', 1),
(5, 'Thingamajig Y', 'A handy thingamajig', 30, 16.99, 'Tools', 2),
(6, 'Whatchamacallit C', 'An interesting whatchamacallit', 60, 11.99, 'Electronics', 3),
(7, 'Doodad D', 'A practical doodad', 45, 14.99, 'Hardware', 1),
(8, 'Whatsit E', 'A cool whatsit', 35, 18.99, 'Tools', 2),
(9, 'Thingummy F', 'An amazing thingummy', 55, 13.99, 'Electronics', 3),
(10, 'Dohickey G', 'A handy dohickey', 20, 15.99, 'Hardware', 1),
(11, 'Whatnot H', 'A versatile whatnot', 65, 17.99, 'Tools', 2),
(12, 'Doodlebug I', 'An interesting doodlebug', 40, 12.99, 'Electronics', 3),
(13, 'Thingamabob J', 'A practical thingamabob', 30, 16.99, 'Hardware', 1),
(14, 'Whatchamajigger K', 'A cool whatchamajigger', 50, 14.99, 'Tools', 2),
(15, 'Doodad L', 'An amazing doodad', 25, 19.99, 'Electronics', 3),
(16, 'Whatsit M', 'A handy whatsit', 45, 13.99, 'Hardware', 1),
(17, 'Thingummy N', 'A versatile thingummy', 35, 17.99, 'Tools', 2),
(18, 'Dohickey O', 'An interesting dohickey', 60, 11.99, 'Electronics', 3),
(19, 'Whatnot P', 'A practical whatnot', 20, 15.99, 'Hardware', 1),
(20, 'Doodlebug Q', 'A cool doodlebug', 55, 13.99, 'Tools', 2);


-- Dummy data for Order table
INSERT INTO `Order` (CustomerID, OrderDate, DeliveryDate, TotalAmount) VALUES
(1, '2024-04-15 10:30:00', '2024-04-20', 49.95),
(2, '2024-04-18 14:45:00', '2024-04-22', 99.50),
(3, '2024-04-21 09:00:00', '2024-04-25', 74.75),
(4, '2024-04-22 16:20:00', '2024-04-27', 129.99),
(5, '2024-04-23 11:40:00', '2024-04-28', 89.75),
(6, '2024-04-24 13:55:00', '2024-04-29', 159.50),
(7, '2024-04-25 08:15:00', '2024-05-01', 79.99),
(8, '2024-04-26 15:05:00', '2024-05-02', 199.75),
(9, '2024-04-27 12:30:00', '2024-05-03', 119.50),
(10, '2024-04-28 10:00:00', '2024-05-04', 139.99),
(11, '2024-04-29 14:25:00', '2024-05-05', 99.75),
(12, '2024-04-30 09:35:00', '2024-05-06', 149.50),
(13, '2024-05-01 16:10:00', '2024-05-07', 89.99),
(14, '2024-05-02 11:50:00', '2024-05-08', 179.75),
(15, '2024-05-03 13:20:00', '2024-05-09', 129.50),
(16, '2024-05-04 08:45:00', '2024-05-10', 159.99),
(17, '2024-05-05 15:00:00', '2024-05-11', 109.75),
(18, '2024-05-06 10:40:00', '2024-05-12', 189.50),
(19, '2024-05-07 14:15:00', '2024-05-13', 99.99),
(20, '2024-05-08 12:00:00', '2024-05-14', 169.75);

-- Dummy data for Employee table
INSERT INTO Employee (FullName, Role, PhoneNumber, Email, PasswordHash) VALUES
('John Doe', 'Manager', '555-1235', '1', '1'),
('Jane Smith', 'Supervisor', '555-5679', 'jane.smith@company.com', 'password_hash2'),
('Bob Johnson', 'Team Lead', '555-9013', 'bob.johnson@company.com', 'password_hash3'),
('Sarah Lee', 'Coordinator', '555-2469', 'sarah.lee@company.com', 'password_hash4'),
('Michael Brown', 'Specialist', '555-7891', 'michael.brown@company.com', 'password_hash5'),
('Emily Davis', 'Analyst', '555-3457', 'emily.davis@company.com', 'password_hash6'),
('David Wilson', 'Technician', '555-8902', 'david.wilson@company.com', 'password_hash7'),
('Jessica Taylor', 'Associate', '555-4568', 'jessica.taylor@company.com', 'password_hash8'),
('William Anderson', 'Consultant', '555-2110', 'william.anderson@company.com', 'password_hash9'),
('Olivia Martinez', 'Advisor', '555-6790', 'olivia.martinez@company.com', 'password_hash10'),
('Alexander Hernandez', 'Specialist', '555-0124', 'alexander.hernandez@company.com', 'password_hash11'),
('Isabella Diaz', 'Coordinator', '555-8767', 'isabella.diaz@company.com', 'password_hash12'),
('Daniel Reyes', 'Technician', '555-4322', 'daniel.reyes@company.com', 'password_hash13'),
('Sophia Morales', 'Analyst', '555-9877', 'sophia.morales@company.com', 'password_hash14'),
('Jacob Gutierrez', 'Associate', '555-5433', 'jacob.gutierrez@company.com', 'password_hash15'),
('Mia Ramirez', 'Consultant', '555-1099', 'mia.ramirez@company.com', 'password_hash16'),
('Ethan Flores', 'Advisor', '555-7655', 'ethan.flores@company.com', 'password_hash17'),
('Isabella Castillo', 'Specialist', '555-3211', 'isabella.castillo@company.com', 'password_hash18'),
('Liam Jimenez', 'Coordinator', '555-9088', 'liam.jimenez@company.com', 'password_hash19'),
('Emma Vargas', 'Analyst', '555-6544', 'emma.vargas@company.com', 'password_hash20');

-- Dummy data for Floor_Manager table
INSERT INTO Floor_Manager (FullName, Role, EmployeeID) VALUES
('John Doe', 'Floor Manager', 1),
('Jane Smith', 'Floor Manager', 2),
('Bob Johnson', 'Floor Manager', 3),
('Sarah Lee', 'Floor Manager', 4),
('Michael Brown', 'Floor Manager', 5);

-- Dummy data for Inventory table
INSERT INTO Inventory (Location, Capacity, ProductID, FloorManagerID) VALUES
('Warehouse A', 500, 1, 1),
('Warehouse B', 300, 2, 2),
('Retail Store', 100, 3, 3),
('Distribution Center', 800, 4, 4),
('Satellite Warehouse', 400, 5, 5),
('Regional Hub', 600, 6, 1),
('Local Depot', 200, 7, 2),
('Main Facility', 1000, 8, 3),
('Offsite Storage', 300, 9, 4),
('Central Warehouse', 700, 10, 5);

-- Dummy data for Floor_Manager_Order table
INSERT INTO Floor_Manager_Order (FloorManagerID, VendorID, OrderDate, DeliveryDate, TotalAmount) VALUES
(1, 1, '2024-04-25 12:00:00', '2024-04-30', 300.25),
(2, 2, '2024-04-27 15:30:00', '2024-05-02', 400.50),
(3, 3, '2024-04-29 09:45:00', '2024-05-04', 250.75),
(4, 1, '2024-05-01 14:20:00', '2024-05-06', 375.99),
(5, 2, '2024-05-03 11:10:00', '2024-05-08', 325.50);

-- Dummy data for Order_Product table
INSERT INTO Order_Product (OrderID, ProductID, Quantity) VALUES
(1, 1, 5),
(2, 2, 3),
(3, 3, 4),
(4, 4, 2),
(5, 5, 6),
(6, 6, 3),
(7, 7, 4),
(8, 8, 2),
(9, 9, 5),
(10, 10, 3);
