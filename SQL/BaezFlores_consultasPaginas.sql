use paginasWeb;
show tables;
select * from courseware;
select * from display;
select * from ftpink;
select * from graphic;
select * from httplink;
select * from webpage;

-- Consultas:
-- ¿Qué páginas contienen enlaces ftp a contenidos en la categoría N?
select w.webID, w.webTitle, c.cdescription from webpage w join ftpLink f on w.webID = f.webID join courseware c on f.cID = c.cID where c.category = "N";
-- ¿Qué páginas muestran imágenes (graphics) con el nombre 'asulogo'?
select w.webID, w.webTitle from webpage w join display d on w.webID = d.webID join graphic g on d.gID = g.gID where g.gName = "asulogo";
-- ¿Qué páginas no muestran imágenes (graphics)?
select w.webID, w.webTitle  from webpage w where w.webID not in (select d.webID from display d);
-- ¿Qué páginas usan imágenes jpg pero no gif?
select w.webID, w.webTitle from webpage w join display d on w.webID = d.webID join graphic g on d.gID = g.gID where g.gType = "jpg"and w.webID not in (select d.webID from display d join graphic g on d.gID = g.gID where g.gType = "gif");
-- ¿Qué páginas contienen solo un enlace http a otra página?
select w.webID, w.webTitle from webpage w join httpLink h on w.webID = h.sourceWebID group by w.webID, w.webTitle having count(h.targetWebID) = 1;
-- ¿Qué página tiene la mayor cantidad de visitas (hits)?
select webID, webTitle, hits from webpage order by hits desc limit 1;
-- ¿Qué páginas contienen enlaces ftp a contenidos en la categoría P?
select w.webID, w.webTitle, c.cdescription from webpage w join ftpLink f on w.webID = f.webID join courseware c on f.cID = c.cID where c.category = "P";