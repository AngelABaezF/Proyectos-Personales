-- Crear Base de datos
CREATE database dreamhome;
USE dreamhome;
-- Crear tablas
CREATE TABLE Branch(
branchNo VARCHAR(4),
street VARCHAR(20),
city VARCHAR(20),
postcode VARCHAR(10),
primary key(branchNo)
);

CREATE TABLE Client(
clientNo VARCHAR(4),
fNAme VARCHAR(10),
lName VARCHAR(10),
telNo VARCHAR(15),
prefType VARCHAR(10),
maxRent DOUBLE,
eMail VARCHAR(256),
primary key(clientNo)
);

CREATE TABLE PrivateOwner(
ownerNo VARCHAR(4),
fName VARCHAR(10),
lName VARCHAR(10),
address VARCHAR(45),
telNo VARCHAR(15),
eMail VARCHAR(256),
password VARCHAR(56),
primary key(ownerNo)
);

create table Staff(
staffNo VARCHAR(4),
fName VARCHAR(10),
lName VARCHAR(10),
position VARCHAR(10),
sex VARCHAR(1),
BOD date,
salary double,
branchNo varchar(4),
primary key(staffNo),
constraint fk_branch_staff1 foreign key(branchNo) references Branch(branchNo)
);

create table PropertyForRent(
propertyNo varchar(4),
street VARCHAR(20),
city VARCHAR(20),
postcode VARCHAR(10),
type varchar(5),
rooms int,
rent double,
ownerNo VARCHAR(4),
staffNo VARCHAR(4),
branchNo varchar(4),
primary key(propertyNO),
constraint fk_privateowner_propertyforrent1 foreign key(ownerNo) references PrivateOwner(ownerNo),
constraint fk_staff_propertyforrent1 foreign key(staffNo) references Staff(staffNo),
constraint fk_branch_propertyforrent1 foreign key(branchNo) references Branch(branchNo)
);

create table Viewing(
clientNo varchar(4),
propertyNo varchar(4),
viewDate date,
comment text,
primary key(clientNo, propertyNo, viewDate),
constraint fk_client_viewing1 foreign key(clientNo) references Client(clientNo),
constraint fk_property_viewing1 foreign key(propertyNo) references PropertyForRent(propertyNO)
);

create table Registration(
clientNo varchar(4),
branchNo varchar(4),
staffNo varchar(4),
dateJoined date,
primary key(clientNo, branchNo, staffNo),
constraint fk_client_registration1 foreign key(clientNo) references Client(clientNo),
constraint fk_branch_registration1 foreign key(branchNo) references Branch(branchNo),
constraint fk_staff_registration1 foreign key(staffNo) references Staff(staffNo)
);

-- DROP, eliminar: DROP DATABASE nombre, drop table nombre,
drop database dreamhome;