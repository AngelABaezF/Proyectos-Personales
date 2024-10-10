-- Llenado de las tablas
insert into webpage values
('01', 'CSE412 Web', 'https://www.eas.asu.edu/~cse412/', '01','20'),
('02', 'CSE412 Web', 'gen_syllabus.html', '01','10'), 
('03', 'CSE412 Web', 'fall98/calendar.html', '01','18'),
('04', 'CSE412 Web', 'pub.html', '01','5'),
('05', 'CSE412 Web', 'winRDBI.html', '01','1'),
('06', 'CSE412 Web', 'projects.html', '01','20'),
('07', 'CSE412 Web', 'faqs.html', '01','1'),
('08', 'CSE412 Web', 'links.html', '01','10'),
('09', 'CSE412 Web', 'https://www.eas.asu.edu/~cse510/', '09','8'),
('10', 'CSE412 Web', 'gen_syllabus.html', '09','8'),
('11', 'CSE412 Web', 'fall98/calendar.html', '09','8'),
('12', 'CSE412 Web', 'notes.html', '09','8'),
('13', 'CSE412 Web', 'https://www.eas.asu.edu/~cse513', '13','21'),
('14', 'CSE412 Web', 'syllabus.html', '13','15'),
('15', 'CSE412 Web', 'class_notes.html', '13','11'),
('16', 'CSE412 Web', 'hypernews.html', '13','21');

insert graphic values
('01','background','gif','cse14/www/graphics/'),
('02','bar','gif','cse14/www/graphics/'),
('03','button 1','jpg','cse14/www/graphics/'),
('04','button 2','jpg','cse14/www/graphics/'),
('05','button 3','gif','cse14/www/graphics/'),
('06','ieeelogo','bmp','cse14/www/graphics/logos'),
('07','acmlogo','jpg','cse14/www/graphics/logos'),
('08','asulogo','gif','cse14/www/graphics/logos'),
('09','clouds','bmp','cse14/www/graphics/'),
('10','books','gif','cse14/www/graphics/'),
('11','lock','jpg','cse14/www/graphics/'),
('12','stone','bmp','cse14/www/graphics/');

insert courseware values 
('doc1','WinRDBI Setup','uh/ftp/class/cse412/winrdb/','D'),
('doc2','WinRDBI User Guide','uh/ftp/class/cse412/winrdb/','D'),
('exe1','WinRDBI Setup','uh/ftp/class/cse412/winrdb/','E'),
('mdb1','Company Database','uh/ftp/class/cse412/projects/','M'),
('not1','Class Notes Chapter 1','uh/ftp/class/cse412/notes/','N'),
('not2','Class Notes Chapter 2','uh/ftp/class/cse412/notes/','N'),
('pub1','WinRDBI Implementation','uh/ftp/class/cse412/winrdb/','P'),
('pub2','Company Theory','uh/ftp/class/cse412/projects/','P'),
('pub3','A Cp-operative Learning Approach','uh/ftp/class/cse412/pubs/','P');

insert into display values
('01','01'), ('06','01'), ('07','01'), ('01','02'),
('02','02'), ('06','02'), ('01','03'), ('07','03'), ('01','04'),
('04','06'),('04','07'), ('01','08'), ('03','08'), ('01','09'),
('03','09'), ('09','09'), ('08','11'), ('04','12');

insert into httpLink values
('02','01'), ('03','01'), ('01','02'), ('01','03'), ('01','04'), ('01','05'), 
('04','05'), ('06','05'), ('01','06'), ('01','07'), ('04','07'),  ('01','08'), 
('08','09'), ('11','09'), ('09','10'),  ('09','11'), ('09','12'), ('11','12'), 
('08','13'), ('14','13'), ('13','14'), ('13','15'),  ('14','15'), ('13','16');

insert into ftpLink values
('04','doc1'), ('05','doc2'), ('05','exe1'), ('06','mdb1'),
('04','not1'), ('06','not1'), ('12','not1'), ('15','not1'), ('08','not2'),
('15','not2'),('04','pub1'), ('05','pub1'), ('06','pub1'), ('12','pub1'),
('04','pub2'), ('05','pub2'), ('04','pub3'), ('05','pub3');

-- Visualizar las tablas existentes
show tables;

-- Visualizar los contenidos de cada tabla
select * from webpage;
select * from graphic;
select * from courseware;
select * from display;
select * from httpLink;
select * from ftpLink;