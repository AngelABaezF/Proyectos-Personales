-- DML, Data Manipulation Language
-- INSERT, DELETE, UPDATE
-- insert into (, , , ) values('', '', '', ''),('', '', '', ''), ('', '', '', '');
-- Insertando en la tabla Branch
INSERT INTO branch VALUES('B005', '22 Reed Rd', 'London', 'SW1 3EH');
INSERT INTO branch(branchNo, street, city, postcode) VALUES('B007', '16 Argyll St', 'Aberdeen', 'AB2 3SU');
INSERT INTO branch VALUES
('B003', '163 Main St', 'Glasgow', 'G11 9QX'),
('B004', '32 Manse Rd', 'Bristol', 'BS99 1NZ'),
('B002', '56 Clover Dr', 'London', 'NW10 6EU');

INSERT INTO branch VALUES ('B009', '10 Xochi Rd', 'Xochitepec', '62790');
DELETE FROM Branch WHERE branchNo = 'B009';
UPDATE branch SET street = '10 Xochi St' WHERE branchNo = 'B009';

-- Insertando en la tabla Staff
INSERT INTO Staff VALUES
('SL21', 'John', 'White', 'Manager', 'M', '1945-10-01', 30000, 'B005'),
('SG37', 'Ann', 'Beech', 'Assistant', 'F', '1960-11-10', 12000, 'B003'),
('SG14', 'David', 'Ford', 'Supervisor', 'M', '1958-03-24', 18000, 'B003'),
('SA9', 'Mary', 'Howe', 'Assistant', 'F', '1970-02-19', 9000, 'B007'),
('SG5', 'Susan', 'Brand', 'Manager', 'F', '1940-06-03', 24000, 'B003'),
('SL41', 'Julie', 'Lee', 'Assistant', 'F', '1965-06-13', 9000, 'B005');

-- Insertando en la tabla PropertyForRent
INSERT INTO PropertyForRent VALUES
('PA14', '16 Holhead', 'Aberdeen', 'AB7 5SU', 'House', 6, 650, 'CO46', 'SA9', 'B007'),
('PL94', '6 Argyll St', 'London', 'NW2', 'Flat', 4, 400, 'CO87', 'SL41', 'B005'),
('PG4', '6 Lawrence St', 'Glasglow', 'G11 9QX', 'Flat', 3, 350, 'CO40', 'SA9', 'B003'),
('PG36', '2 Manor Rd', 'Glasglow', 'G32 4QX', 'Flat', 3, 375, 'CO93', 'SG37branch', 'B003'),
('PG21', '18 Dale Rd', 'Glasglow', 'G12', 'House', 5, 600, 'CO87', 'SG37', 'B003'),
('PG16', '5 Nova Dr', 'Glasglow', 'G12 9AX', 'Flat', 4, 450, 'CO93', 'SG14', 'B003');

-- Insertando en la tabla Client
INSERT INTO Client VALUES
('CR76', 'John', 'Kay', '0207-774-5632', 'Flat', 425, 'john.kay@gmail.com'),
('CR56', 'Aline', 'Stewart', '0141-848-1825', 'Flat', 350, 'astewart@hotmail.com'),
('CR74', 'Mike', 'Ritchie', '01475-392178', 'House', 750, 'mritchie01@yahoo.co.uk'),
('CR62', 'Mary', 'Tregaer', '01224-196720', 'Flat', 600, 'maryt@hotmail.com');

-- Insertando en la tabla PrivateOwner
INSERT INTO PrivateOwner VALUES
('CO46', 'Joe', 'Keogh', '2 Fergus Dr, Aberdeen AB2 7SX', '01224-861212', 'jkeogh@lhh.com', SHA2('1234','224')),
('CO87', 'Carol', 'Farrel', '6 Achray St, Glasglow G32 9DX', '0141-357-7419', 'cfarrel@gmail.com', SHA2('1234','224')),
('CO40', 'Tina', 'Murphy', '63 Well St, Glasglow G42', '0141-943-1728', 'tinam@hotmail.com', SHA2('1234','224')),
('CO93', 'Tony', 'Shaw', '12 Park Pl, Glasglow G4 0QR', '0142-225-7025', 'tony.shaw@ark.com', SHA2('1234','224'));

-- Insertando en la tabla Viewing
INSERT INTO Viewing VALUES
('CR56','PA14','2024-05-24','too small'),
('CR76','PG4','2013-04-20','too remote'),
('CR56','PG4','2013-05-26',''),
('CR62','PA14','2013-05-14','no dining room'),
('CR56','PG36','2013-04-28','');

-- Insertando en la tabla Registration
INSERT INTO Registration VALUES
('CR76','B005','SL41','2013-06-02'),
('CR56','B003','SG37','2012-04-11'),
('CR74','B003','SG37','2011-11-16'),
('CR62','B007','SA9','2012-03-07');

select * from Branch;
select * from Staff;
select * from PropertyForRent;
select * from Client;
select * from PrivateOwner;
select * from Viewing;
select * from Registration;