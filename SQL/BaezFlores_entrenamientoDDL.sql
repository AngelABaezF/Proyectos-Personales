-- Borrar base de datos
drop database entrenamientoEmpleados;

-- Creación de la base de datos
create database entrenamientoEmpleados;
use entrenamientoEmpleados;

-- Creación de las Tablas
create table employee (
    eID int primary key,
    eLast varchar(8),
    eFirst varchar(8),
    eTitle text,
    eSalary int
);

create table trainingCourse (
	cID varchar(5) primary key,
    cTitle text,
    cHours int,
    areaID varchar(2)
);

create table technologyArea (
	aID varchar(2) primary key,
    aTitle text,
    aUrl text,
    leadID int
);

create table takes (
    eID int,
    cID varchar(5),
    tYear year,
    tMonth int,
    tDay int,
    primary key (eID, cID),
    foreign key (eID) references employee(eID),
    foreign key (cID) references trainingCourse(cID)
);