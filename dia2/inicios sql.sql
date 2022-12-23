-- Asi se crea una base de datos
CREATE DATABASE IF NOT exists practicas;

use practicas;

-- ahora procedemos a crear nuetsra tabla
create table usuarios(
	id int auto_increment unique primary key,
    nombre text not null,
    dni char(8) unique
);
