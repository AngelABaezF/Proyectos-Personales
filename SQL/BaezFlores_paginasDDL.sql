-- Tirar la base de datos
drop database paginasWeb;

-- Creación de la base de datos
create database paginasWeb;
use paginasWeb;

-- Crear tablas
CREATE TABLE webpage(
webID INT,
webTitle VARCHAR(45),
url TEXT,
base INT,
hits INT,
PRIMARY KEY(webID)
);

CREATE TABLE graphic(
gID INT,
gName VARCHAR(45),
gType VARCHAR(45),
gLocation TEXT,
PRIMARY KEY(gID)
);

CREATE TABLE courseware(
cid VARCHAR(4),
cDescription TEXT,
ftpLocation TEXT,
category VARCHAR(1),
PRIMARY KEY(cID)
);

CREATE TABLE display(
webID INT,
gID INT,
PRIMARY KEY(webID, gID),
CONSTRAINT fk_webpage_display
FOREIGN KEY(webID) REFERENCES webpage(webID),
CONSTRAINT fk_graphic_display
FOREIGN KEY(gID) REFERENCES graphic(gID)
);

CREATE TABLE httpLink(
sourceWebID INT,
targetWebID INT,
PRIMARY KEY(sourceWebID, targetWebID),
CONSTRAINT fk_webpage_httplink1
FOREIGN KEY(sourceWebID) REFERENCES webpage(webID),
CONSTRAINT fk_webpage_httplink2
FOREIGN KEY(targetWebID) REFERENCES webpage(webID)
);

CREATE TABLE ftpLink(
webID INT,
cID VARCHAR(4),
PRIMARY KEY(webID, cID),
CONSTRAINT fk_webpage_ftpLink
FOREIGN KEY(webID) REFERENCES webpage(webID),
CONSTRAINT fk_courseware_ftpLink
FOREIGN KEY(cID) REFERENCES courseware(cID)
);