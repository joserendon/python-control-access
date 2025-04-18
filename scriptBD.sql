-- Crear base de datos
CREATE DATABASE IF NOT EXISTS control_acceso_empresa;
USE control_acceso_empresa;

-- Tabla de roles de usuario
CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- Tabla de estados
CREATE TABLE estados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- Tabla de usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    id_rol INT NOT NULL,
    id_estado INT NOT NULL,
    FOREIGN KEY (id_rol) REFERENCES roles(id),
    FOREIGN KEY (id_estado) REFERENCES estados(id)
);

-- Tabla de áreas de la empresa
CREATE TABLE areas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

-- Tabla de motivos de visita
CREATE TABLE motivos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

-- Tabla de tipos de documento
CREATE TABLE tipos_documento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- Tabla de empresas
CREATE TABLE empresas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- Tabla de tipos de persona
CREATE TABLE tipos_persona (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- Tabla de personas
CREATE TABLE personas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_tipo_documento INT NOT NULL,
    id_tipo_persona INT NOT NULL,
    documento VARCHAR(20) NOT NULL UNIQUE,
    nombre_completo VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    id_empresa INT,
    FOREIGN KEY (id_tipo_documento) REFERENCES tipos_documento(id),
    FOREIGN KEY (id_tipo_persona) REFERENCES tipos_persona(id),
    FOREIGN KEY (id_empresa) REFERENCES empresas(id)
);

-- Tabla de tipos de acceso (entradas y salidas, etc.)
CREATE TABLE tipos_acceso (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- Tabla de puertas de acceso
CREATE TABLE puertas_acceso (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- Tabla de accesos (registro de entradas y salidas)
CREATE TABLE accesos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_puerta_acceso INT NOT NULL,
    id_persona INT NOT NULL,
    id_area INT NOT NULL,
    id_motivo INT NOT NULL,
    id_tipo_acceso INT NOT NULL,
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_puerta_acceso) REFERENCES puertas_acceso(id),
    FOREIGN KEY (id_persona) REFERENCES personas(id),
    FOREIGN KEY (id_area) REFERENCES areas(id),
    FOREIGN KEY (id_motivo) REFERENCES motivos(id),
    FOREIGN KEY (id_tipo_acceso) REFERENCES tipos_acceso(id)
);

-- Tabla de acciones de auditoría
CREATE TABLE acciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- Tabla de auditoría
CREATE TABLE auditoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_accion INT NOT NULL,
    descripcion TEXT,
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_accion) REFERENCES acciones(id)
);


DELIMITER $$

CREATE PROCEDURE proc_select_estados()
BEGIN
    SELECT id, nombre FROM estados ORDER BY id;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_insert_estados(
    IN p_estado VARCHAR(50),
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET Respuesta = 'Error al insertar el estado (posible duplicado)';
    END;

    INSERT INTO estados (nombre) VALUES (p_estado);
    SET Respuesta = 'Estado insertado correctamente';
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_update_estados(
    IN p_id INT,
    IN p_nuevo_estado VARCHAR(50),
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;

    SELECT COUNT(*) INTO v_existente FROM estados WHERE id = p_id;

    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        UPDATE estados SET nombre = p_nuevo_estado WHERE id = p_id;
        SET Respuesta = 'Estado actualizado correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_delete_estados(
    IN p_id INT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;

    SELECT COUNT(*) INTO v_existente FROM estados WHERE id = p_id;

    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        DELETE FROM estados WHERE id = p_id;
        SET Respuesta = 'Estado eliminado correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_select_areas()
BEGIN
    SELECT id, nombre FROM areas ORDER BY id;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_insert_areas(
    IN p_area VARCHAR(100),
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET Respuesta = 'Error al insertar el área (posible duplicado)';
    END;

    INSERT INTO areas (nombre) VALUES (p_area);
    SET Respuesta = 'Área insertada correctamente';
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_update_areas(
    IN p_id INT,
    IN p_nueva_area VARCHAR(100),
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;

    SELECT COUNT(*) INTO v_existente FROM areas WHERE id = p_id;

    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        UPDATE areas SET nombre = p_nueva_area WHERE id = p_id;
        SET Respuesta = 'Área actualizada correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_delete_areas(
    IN p_id INT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;

    SELECT COUNT(*) INTO v_existente FROM areas WHERE id = p_id;

    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        DELETE FROM areas WHERE id = p_id;
        SET Respuesta = 'Área eliminada correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_select_empresas()
BEGIN
    SELECT id, nombre FROM empresas ORDER BY id;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_insert_empresas(
    IN p_empresa VARCHAR(50),
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET Respuesta = 'Error al insertar la empresa (posible duplicado)';
    END;

    INSERT INTO empresas (nombre) VALUES (p_empresa);
    SET Respuesta = 'Empresa insertada correctamente';
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_update_empresas(
    IN p_id INT,
    IN p_nueva_empresa VARCHAR(50),
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;

    SELECT COUNT(*) INTO v_existente FROM empresas WHERE id = p_id;

    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        UPDATE empresas SET nombre = p_nueva_empresa WHERE id = p_id;
        SET Respuesta = 'Empresa actualizada correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_delete_empresas(
    IN p_id INT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;

    SELECT COUNT(*) INTO v_existente FROM empresas WHERE id = p_id;

    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        DELETE FROM empresas WHERE id = p_id;
        SET Respuesta = 'Empresa eliminada correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_select_motivos()
BEGIN
    SELECT id, nombre FROM motivos ORDER BY id;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_insert_motivos(
    IN p_motivo VARCHAR(100),
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET Respuesta = 'Error al insertar el motivo (posible duplicado)';
    END;

    INSERT INTO motivos (nombre) VALUES (p_motivo);
    SET Respuesta = 'Motivo insertado correctamente';
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_update_motivos(
    IN p_id INT,
    IN p_nuevo_motivo VARCHAR(100),
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;

    SELECT COUNT(*) INTO v_existente FROM motivos WHERE id = p_id;

    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        UPDATE motivos SET nombre = p_nuevo_motivo WHERE id = p_id;
        SET Respuesta = 'Motivo actualizado correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_delete_motivos(
    IN p_id INT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;

    SELECT COUNT(*) INTO v_existente FROM motivos WHERE id = p_id;

    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        DELETE FROM motivos WHERE id = p_id;
        SET Respuesta = 'Motivo eliminado correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_select_roles()
BEGIN
    SELECT id, nombre FROM roles ORDER BY id;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_insert_roles(
    IN p_rol VARCHAR(50),
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET Respuesta = 'Error al insertar el rol (posible duplicado)';
    END;

    INSERT INTO roles (nombre) VALUES (p_rol);
    SET Respuesta = 'Rol insertado correctamente';
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_update_roles(
    IN p_id INT,
    IN p_nuevo_rol VARCHAR(50),
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;

    SELECT COUNT(*) INTO v_existente FROM roles WHERE id = p_id;

    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        UPDATE roles SET nombre = p_nuevo_rol WHERE id = p_id;
        SET Respuesta = 'Rol actualizado correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_delete_roles(
    IN p_id INT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;

    SELECT COUNT(*) INTO v_existente FROM roles WHERE id = p_id;

    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        DELETE FROM roles WHERE id = p_id;
        SET Respuesta = 'Rol eliminado correctamente';
    END IF;
END $$

DELIMITER ;
