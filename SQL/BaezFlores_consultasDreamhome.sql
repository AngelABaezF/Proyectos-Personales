-- Consultas de DreamHome
use dreamhome;

-- SELECT campos FROM tabla WHERE condiciones

-- Conidciones (delante del WHERE o HAVING)

-- Condicionales de comparacion
-- = < > != <= >= <>
-- AND, OR, NOT

-- RANGO
-- salary >= 3000 AND salary <= 5000
-- salary BETWEEN 3000 AND 5000

-- PATRON
-- Todos los empleados cuyo apellido termine en o
-- % cualquier cantidad de caracteres
-- _ un solo caracter
-- ? un solo caracter opcional (va o no va)alter
-- fName LIKE '%o'		Todos los que terminan en o
-- fName LIKE 'A%'		Todos los que empeizan en a
-- fName LIKE ''	Todos los que tienen 4 letras
-- fName LIKE '_a'
-- fName LIKE 'Alejandre?'
-- fName LIKE '%on%'

-- NULA
-- NO hacer esto comment = NULL
-- Siempre te va a dar NULL
-- La forma correcta es comment IS NULL

-- PERTENENCIA
-- month = 'March' OR month = 'August' OR montg = 'December'
-- month IN ('March', 'August', 'December')

-- GROUP BY campos HAVING condiciones ORDER BY campos
-- OPERADORES ESCALARES (Funciones, afecta un valor o registro a la vez)
-- sha2,, length, upper, lower, substring, 

--  FUNCIONES DE AGREGACION/AGREGADO
-- cout, sum, avg, mas, min

-- CONSULTA MULTITABLA
-- 
-- JOIN
-- SUBCONSULTAS

select * from Staff where branch = 'B005';
select fName, lName from Staff where branch = 'B005';
select * from propertyforrent where city = 'Glasgow';
select * from propertyforrent where rent > 400 AND rent < 600;
select * from viewing where comment is null;
select distinct type from propertyforrent;
select count(city) from branch;
select count(*) from branch where city = 'London';
select avg(salary) from staff where branchNO = 'B003';
select max(rent) from propertyforrent;
select count(*) from branch, staff where Branch.branchNo = Staff.branchNO and city = 'Glasgow';
select count(*) from branch join staff on Branch.branchNo = Staff.staffNo where city = 'Glasgow';
select fName, lName, street from Staff join PropertyForRent on Staff.staffNo = PropertyForRent.staffNo;
select count(properyNo) from viewing v join client c on v.clientNo = c.clientNo where fName= 'John' and lName = 'Kay';
select count(properyNo) from propertyforrent p join branch b on p.staffNo = b.staffNo where b.city = 'Aberdeen';
select fName, lName from registration r join client c on r.clientNo = c.clientNo where month(dateJoined) = 11;
select street from propertyforrent pr join viewing v on pr.propertyNo = v.propertyNo where comment is null;
select max(rent) from propertyforrent;
select * from propertyforrent where rent = (select max(rent) from propertyforrent);
select propertyNo from viewing where comment is null;
select ownerNo from propertyforrent where propertyNo in(select propertyNo from viewing where comment is null);
select fName, lName from privateowner where ownerNo in  (select ownerNo from propertyforrent where propertyNo in(select propertyNo from viewing where comment is null));

-- Consultas de la tarea
-- ¿Qué páginas contienen enlaces ftp a contenidos en la categoría N?
-- ¿Qué páginas muestran imágenes (graphics) con el nombre 'asulogo'?
-- ¿Qué páginas no muestran imágenes (graphics)?
-- ¿Qué páginas usan imágenes jpg pero no gif?
-- ¿Qué páginas contienen solo un enlace http a otra página?
-- ¿Qué página tiene la mayor cantidad de visitas (hits)?
-- ¿Qué páginas contienen enlaces ftp a contenidos en la categoría P?