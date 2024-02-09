USE masterPython 
CREATE TABLE IF NOT EXISTS usuarios(
    id tinyint auto_increment  PRIMARY KEY,
    nombre varchar(100),
    apellidos varchar(100),
    email varchar(50) not null,
    password varchar(255),
    fecha datetime default now(),
    active tinyint default 0,
    CONSTRAINT uq_email UNIQUE(email)
);

CREATE TABLE IF NOT EXISTS login(
id int auto_increment,
id_usuario tinyint not null,
fecha_login datetime default now(),
active tinyint default 0,
CONSTRAINT pk_login PRIMARY KEY(id),
CONSTRAINT fk_login_usuario FOREIGN KEY(id_usuario) REFERENCES usuarios(id)
);

CREATE TABLE IF NOT EXISTS notas(
id int auto_increment,
id_usuario tinyint not null,
titulo varchar(255) not null,
descripcion mediumtext,
fecha_login datetime default now(),
CONSTRAINT pk_notas PRIMARY KEY(id),
CONSTRAINT fk_nota_usuario FOREIGN KEY(id_usuario) REFERENCES usuarios(id)
);
