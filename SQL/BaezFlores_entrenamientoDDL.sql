-- Borrar base de datos
drop database empleados;

-- Creación de la base de datos
create database empleados;
use empleados;

-- Creación de las Tablas
CREATE TABLE employee(
eID INT,
eLast VARCHAR(7),
eFirst VARCHAR(8),
eTittle VARCHAR(50),
eSalary DOUBLE,
PRIMARY KEY(eID)
);

CREATE TABLE technologyArea(
aID VARCHAR(2),
aTitle VARCHAR(45),
aURL VARCHAR(45),
leadID INT,
PRIMARY KEY(aID),
CONSTRAINT fk_employee_technologyArea1
FOREIGN KEY(leadID) REFERENCES employee(eID)
);

CREATE TABLE trainingCourse(
cID VARCHAR(4),
cTittle VARCHAR(45),
cHours INT,
areaID VARCHAR(2),
PRIMARY KEY(cID),
CONSTRAINT fk_technologyArea_trainingCourse1
FOREIGN KEY(areaID) REFERENCES technologyArea(aID)
);

CREATE TABLE takes(
eID INT,
cID VARCHAR(4),
tYear INT,
tMonth INT,
tDay INT,
PRIMARY KEY(eID, cID),
CONSTRAINT fk_employee_takes1
FOREIGN KEY(eID) REFERENCES employee(eID),
CONSTRAINT fk_trainingCourse_takes1
FOREIGN KEY(cID) REFERENCES trainingCourse(cID)
);