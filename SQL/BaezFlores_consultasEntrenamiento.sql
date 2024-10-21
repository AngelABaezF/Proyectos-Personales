use empleados;
show tables;
select * from employee;
select * from takes;
select * from technologyarea;
select * from trainingcourse;

-- Consultas:
-- ¿Qué cursos se ofrecen en el área de Bases de datos?
select cTittle  from trainingcourse where areaID="DB";
-- ¿Qué empleados han tomado un curso del área de Bases de datos?
select distinct e.eID, e.eFirst, e.eLast from employee e join takes t on e.eID = t.eID join trainingCourse c on t.cID = c.cID where c.areaID = "DB";
-- ¿Qué empleados no han tomado ningún curso?
select e.eID, e.eFirst, e.eLast from employee e where not exists (select 1 from takes t where e.eID = t.eID);
-- ¿Qué empleados han tomado un curso en más de un área tecnológica?
select e.eID, e.eFirst, e.eLast from employee e join takes t on e.eID = t.eID join trainingCourse c on t.cID = c.cID group by e.eID, e.eFirst, e.eLast having COUNT(distinct c.areaID) > 1;
-- ¿Qué empleados tienen el menor salario?
select eID, eFirst, eLast, eSalary from employee where eSalary = (select MIN(eSalary) from employee);
-- ¿Qué empleados tomaron todos los cursos del área de Bases de datos?
select e.eID, e.eFirst, e.eLast from employee e join takes t on e.eID = t.eID join trainingCourse c on t.cID = c.cID where c.areaID = "DB" group by e.eID, e.eFirst, e.eLast having COUNT(distinct c.cID) = (select COUNT(cID) from trainingCourse where areaID = "DB");
-- ¿Cuál es la cantidad de horas de curso tomadas por todos los empleados, separadas por área?
select a.aID, a.aTitle, sum(c.cHours) as TotalHours from takes t join trainingCourse c on t.cID = c.cID join technologyArea a on c.areaID = a.aID group by a.aID, a.aTitle;
-- ¿Qué empleados han tomado cursos después del 4 de diciembre del 2000?
select distinct e.eID, e.eFirst, e.eLast from employee e join takes t ON e.eID = t.eID where date(concat(t.tYear, "-", t.tMonth, "-", t.tDay)) > "2000-12-04";