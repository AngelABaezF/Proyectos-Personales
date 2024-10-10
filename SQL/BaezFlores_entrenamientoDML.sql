-- Llenado de las tablas
insert into employee values 
('111','Last111','First111','Database Administrator','751119'),
('222','Last222','First222','Softwere Engineer','51722'), ('321','Last321','First321','Database Administrator','68321'),
('333','Last333','First333','Sr Softwere Engineer','60333'), ('345','Last345','First345','Sr Softwere Engineer','59345'),
('369','Last369','First369','Softwere Engineer','36369'), ('444','Last444','First444','Softwere Engineer','44444'),
('456','Last456','First456','Softwere Engineer','45456'), ('555','Last555','First555','Sr Softwere Engineer','55555'),
('654','Last654','First654','Coach','60654'), ('666','Last666','First666','Coach','66666'), ('678','Last678','First678','Coach','67678'),
('693','Last693','First693','Coach','69693'), ('777','Last777','First777','Database Administrator','77777'),
('789','Last789','First789','Database Administrator','78789'), ('888','Last888','First888','Database Administrator','88888'),
('963','Last963','First963','Manager','98963'), ('987','Last987','First987','Manager','99987'), ('999','Last999','First999','Manager','100999');

insert into trainingCourse values
('DB01','Micrsoft Access','8','D6'),
('DB02','Query Languajes','16','D6'),
('DB03','Database Modeling','8','D6'),
('DB04','Transactions','8','D6'),
('JA01','Introduction to Java','8','JA'),
('JA02','JavaBeans','16','JA'),
('JA03','Enterprise JavaBeans','32','JA'),
('JA04','JDBC','8','JA'),
('SE01','Patterns','16','SE'),
('SE02','Validations & Verifications','32','SE'),
('SE03','Softwere Components','40','SE'),
('WW01','Dynamic HTML','8','WW'),
('WW02','XML','16','WW'),
('WW03','XSLT','24','WW');

insert into technologyArea values
('DB','Database','https://www.company.intranet/technology/db','321'),
('JA','Java','https://www.company.intranet/technology/java','333'),
('SE','Softwere Engineering','https://www.company.intranet/technology/softwere-engineering','345'),
('WW','Web','https://www.company.intranet/technology/web','369');

insert into takes values
(321, 'JA01', 2000, 7, 24),
(333, 'JA04', 2000, 7, 27),
(333, 'SE01', 2000, 6, 1),
(345, 'SE02', 2000, 6, 2),
(345, 'WW01', 2000, 8, 1),
(369, 'JA04', 2000, 7, 27),
(369, 'WW01', 2000, 8, 1),
(369, 'WW02', 2000, 8, 2),
(369, 'WW03', 2000, 8, 3),
(444, 'DB01', 2000, 8, 15),
(444, 'DB02', 2000, 9, 15),
(456, 'JA01', 2001, 1, 15),
(456, 'WW01', 2000, 3, 1),
(555, 'DB03', 2000, 9, 22),
(666, 'JA01', 2000, 1, 1),
(678, 'JA01', 2000, 1, 1),
(678, 'JA02', 2000, 1, 2),
(693, 'JA01', 2000, 7, 24),
(693, 'JA02', 2000, 1, 2),
(693, 'JA03', 2000, 12, 12),
(777, 'DB01', 2000, 5, 1),
(777, 'DB02', 2000, 9, 15),
(777, 'DB03', 2000, 9, 22),
(777, 'DB04', 2000, 9, 29),
(789, 'WW01', 2001, 3, 1),
(888, 'DB01', 2000, 5, 1),
(888, 'JA01', 2000, 7, 24),
(888, 'SE01', 2000, 8, 1),
(888, 'WW01', 2000, 7, 24),
(999, 'SE01', 2000, 6, 1);

-- Visualizar las tablas existentes
show tables;

-- Visualizar los contenidos de cada tabla
select * from employee;
select * from trainingCourse;
select * from technologyArea;
select * from takes;