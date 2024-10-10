-- Creación de la base de datos
create database paginasWeb;
use paginasWeb;

-- Tabla para almacenar las páginas web
create table webpage (
    webID int primary key,
    webTitle varchar(255) not null,
    url text,
    base int,
    hits int
);

-- Tabla para almacenar gráficos
create table graphic (
    gID int primary key,
    gName varchar(255) not null,
    gType varchar(5),
    gLocation text
);

-- Tabla para almacenar cursos
create table courseware (
    cID varchar(10) primary key,
    cDescription text,
    ftpLocation text,
    category varchar(1)
);

-- Tabla de relación entre páginas web y gráficos (muchos a muchos)
create table display (
    webID int,
    gID int,
    primary key (webID, gID),
    foreign key (webID) references webpage(webID),
    foreign key (gID) references graphic(gID)
);

-- Tabla de relación para enlaces HTTP entre páginas web
create table httpLink (
    sourceWebID int,
    targetWebID int,
    primary key (sourceWebID, targetWebID),
    foreign key (sourceWebID) references webpage(webID),
    foreign key (targetWebID) references webpage(webID)
);

-- Tabla de relación para enlaces FTP entre páginas web y cursos
create table ftpLink (
    webID int,
    cID varchar(10),
    primary key (webID, cID),
    foreign key (webID) references webpage(webID),
    foreign key (cID) references courseware(cID)
);