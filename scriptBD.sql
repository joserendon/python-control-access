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
    nombre VARCHAR(100) NOT NULL,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
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
CREATE TABLE auditorias (
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

DELIMITER $$

CREATE PROCEDURE proc_select_tipos_documento()
BEGIN
    SELECT id, nombre FROM tipos_documento ORDER BY id;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_insert_tipos_documento(
    IN p_tipo_documento VARCHAR(50),
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET Respuesta = 'Error al insertar el tipo de documento (posible duplicado)';
    END;

    INSERT INTO tipos_documento (nombre) VALUES (p_tipo_documento);
    SET Respuesta = 'Tipo de documento insertado correctamente';
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_update_tipos_documento(
    IN p_id INT,
    IN p_nuevo_tipo_documento VARCHAR(50),
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;

    SELECT COUNT(*) INTO v_existente FROM tipos_documento WHERE id = p_id;

    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        UPDATE tipos_documento SET nombre = p_nuevo_tipo_documento WHERE id = p_id;
        SET Respuesta = 'Tipo de documento actualizado correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_delete_tipos_documento(
    IN p_id INT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;

    SELECT COUNT(*) INTO v_existente FROM tipos_documento WHERE id = p_id;

    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        DELETE FROM tipos_documento WHERE id = p_id;
        SET Respuesta = 'Tipo de documento eliminado correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_select_usuarios()
BEGIN
    SELECT id, nombre, usuario, password, id_rol, id_estado FROM usuarios ORDER BY id;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_insert_usuarios(
    IN p_nombre VARCHAR(100),
    IN p_usuario VARCHAR(50),
    IN p_password VARCHAR(255),
    IN p_id_rol INT,
    IN p_id_estado INT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET Respuesta = 'Error al insertar el usuario (posible duplicado)';
    END;

    INSERT INTO usuarios (nombre, usuario, password, id_rol, id_estado)
    VALUES (p_nombre, p_usuario, p_password, p_id_rol, p_id_estado);
    SET Respuesta = 'Usuario insertado correctamente';
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_update_usuarios(
    IN p_id INT,
    IN p_nombre VARCHAR(100),
    IN p_usuario VARCHAR(50),
    IN p_password VARCHAR(255),
    IN p_id_rol INT,
    IN p_id_estado INT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;

    SELECT COUNT(*) INTO v_existente FROM usuarios WHERE id = p_id;

    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        UPDATE usuarios
        SET nombre = p_nombre,
            usuario = p_usuario,
            password = p_password,
            id_rol = p_id_rol,
            id_estado = p_id_estado
        WHERE id = p_id;
        SET Respuesta = 'Usuario actualizado correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_delete_usuarios(
    IN p_id INT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;

    SELECT COUNT(*) INTO v_existente FROM usuarios WHERE id = p_id;

    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        DELETE FROM usuarios WHERE id = p_id;
        SET Respuesta = 'Usuario eliminado correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_select_acciones()
BEGIN
    SELECT id, nombre FROM acciones ORDER BY id;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_insert_acciones(
    IN p_nombre VARCHAR(50),
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET Respuesta = 'Error al insertar la acción (posible duplicado)';
    END;

    INSERT INTO acciones (nombre) VALUES (p_nombre);
    SET Respuesta = 'Acción insertada correctamente';
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_update_acciones(
    IN p_id INT,
    IN p_nombre VARCHAR(50),
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;
    SELECT COUNT(*) INTO v_existente FROM acciones WHERE id = p_id;
    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        UPDATE acciones SET nombre = p_nombre WHERE id = p_id;
        SET Respuesta = 'Acción actualizada correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_delete_acciones(
    IN p_id INT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;
    SELECT COUNT(*) INTO v_existente FROM acciones WHERE id = p_id;
    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        DELETE FROM acciones WHERE id = p_id;
        SET Respuesta = 'Acción eliminada correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_select_auditorias()
BEGIN
    SELECT id, id_usuario, id_accion, descripcion, fecha_hora FROM auditorias ORDER BY id;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE proc_insert_auditorias(
    IN p_id_usuario INT,
    IN p_id_accion INT,
    IN p_descripcion TEXT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET Respuesta = 'Error al insertar la auditoria (posible duplicado)';
    END;

    INSERT INTO auditorias (id_usuario, id_accion, descripcion)
    VALUES (p_id_usuario, p_id_accion, p_descripcion);
    SET Respuesta = 'Auditoría insertada correctamente';
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_update_auditorias(
    IN p_id INT,
    IN p_id_usuario INT,
    IN p_id_accion INT,
    IN p_descripcion TEXT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;
    SELECT COUNT(*) INTO v_existente FROM auditorias WHERE id = p_id;
    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        UPDATE auditorias
        SET id_usuario = p_id_usuario,
            id_accion = p_id_accion,
            descripcion = p_descripcion
        WHERE id = p_id;
        SET Respuesta = 'Auditoría actualizada correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_delete_auditorias(
    IN p_id INT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;
    SELECT COUNT(*) INTO v_existente FROM auditorias WHERE id = p_id;
    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        DELETE FROM auditorias WHERE id = p_id;
        SET Respuesta = 'Auditoría eliminada correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_select_accesos()
BEGIN
    SELECT id, id_puerta_acceso, id_persona, id_area, id_motivo, id_tipo_acceso, fecha_hora FROM accesos ORDER BY id;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_insert_accesos(
    IN p_id_puerta_acceso INT,
    IN p_id_persona INT,
    IN p_id_area INT,
    IN p_id_motivo INT,
    IN p_id_tipo_acceso INT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET Respuesta = 'Error al insertar el acceso (Posible duplicado)';
    END;

    INSERT INTO accesos (id_puerta_acceso, id_persona, id_area, id_motivo, id_tipo_acceso)
    VALUES (p_id_puerta_acceso, p_id_persona, p_id_area, p_id_motivo, p_id_tipo_acceso);
    SET Respuesta = 'Acceso insertado correctamente';
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_update_accesos(
    IN p_id INT,
    IN p_id_puerta_acceso INT,
    IN p_id_persona INT,
    IN p_id_area INT,
    IN p_id_motivo INT,
    IN p_id_tipo_acceso INT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;
    SELECT COUNT(*) INTO v_existente FROM accesos WHERE id = p_id;
    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        UPDATE accesos
        SET id_puerta_acceso = p_id_puerta_acceso,
            id_persona = p_id_persona,
            id_area = p_id_area,
            id_motivo = p_id_motivo,
            id_tipo_acceso = p_id_tipo_acceso
        WHERE id = p_id;
        SET Respuesta = 'Acceso actualizado correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_delete_accesos(
    IN p_id INT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;
    SELECT COUNT(*) INTO v_existente FROM accesos WHERE id = p_id;
    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        DELETE FROM accesos WHERE id = p_id;
        SET Respuesta = 'Acceso eliminado correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_select_tipos_acceso()
BEGIN
    SELECT id, nombre FROM tipos_acceso ORDER BY id;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_insert_tipos_acceso(
    IN p_nombre VARCHAR(50),
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET Respuesta = 'Error al insertar el tipo de acceso (Posible duplicado)';
    END;

    INSERT INTO tipos_acceso (nombre) VALUES (p_nombre);
    SET Respuesta = 'Tipo de acceso insertado correctamente';
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_update_tipos_acceso(
    IN p_id INT,
    IN p_nombre VARCHAR(50),
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;
    SELECT COUNT(*) INTO v_existente FROM tipos_acceso WHERE id = p_id;
    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        UPDATE tipos_acceso SET nombre = p_nombre WHERE id = p_id;
        SET Respuesta = 'Tipo de acceso actualizado correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_delete_tipos_acceso(
    IN p_id INT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;
    SELECT COUNT(*) INTO v_existente FROM tipos_acceso WHERE id = p_id;
    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        DELETE FROM tipos_acceso WHERE id = p_id;
        SET Respuesta = 'Tipo de acceso eliminado correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_select_personas()
BEGIN
    SELECT id, id_tipo_documento, id_tipo_persona, documento, nombre_completo, telefono, id_empresa
    FROM personas ORDER BY id;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_insert_personas(
    IN p_id_tipo_documento INT,
    IN p_id_tipo_persona INT,
    IN p_documento VARCHAR(20),
    IN p_nombre_completo VARCHAR(100),
    IN p_telefono VARCHAR(20),
    IN p_id_empresa INT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET Respuesta = 'Error al insertar la persona (Posible duplicado)';
    END;

    INSERT INTO personas (id_tipo_documento, id_tipo_persona, documento, nombre_completo, telefono, id_empresa)
    VALUES (p_id_tipo_documento, p_id_tipo_persona, p_documento, p_nombre_completo, p_telefono, p_id_empresa);
    SET Respuesta = 'Persona insertada correctamente';
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_update_personas(
    IN p_id INT,
    IN p_id_tipo_documento INT,
    IN p_id_tipo_persona INT,
    IN p_documento VARCHAR(20),
    IN p_nombre_completo VARCHAR(100),
    IN p_telefono VARCHAR(20),
    IN p_id_empresa INT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;
    SELECT COUNT(*) INTO v_existente FROM personas WHERE id = p_id;
    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        UPDATE personas
        SET id_tipo_documento = p_id_tipo_documento,
            id_tipo_persona = p_id_tipo_persona,
            documento = p_documento,
            nombre_completo = p_nombre_completo,
            telefono = p_telefono,
            id_empresa = p_id_empresa
        WHERE id = p_id;
        SET Respuesta = 'Persona actualizada correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_delete_personas(
    IN p_id INT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;
    SELECT COUNT(*) INTO v_existente FROM personas WHERE id = p_id;
    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        DELETE FROM personas WHERE id = p_id;
        SET Respuesta = 'Persona eliminada correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_select_tipos_persona()
BEGIN
    SELECT id, nombre FROM tipos_persona ORDER BY id;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_insert_tipos_persona(
    IN p_nombre VARCHAR(50),
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET Respuesta = 'Error al insertar el tipo de persona (Posible duplicado) ';
    END;

    INSERT INTO tipos_persona (nombre) VALUES (p_nombre);
    SET Respuesta = 'Tipo de persona insertado correctamente';
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_update_tipos_persona(
    IN p_id INT,
    IN p_nombre VARCHAR(50),
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;
    SELECT COUNT(*) INTO v_existente FROM tipos_persona WHERE id = p_id;
    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        UPDATE tipos_persona SET nombre = p_nombre WHERE id = p_id;
        SET Respuesta = 'Tipo de persona actualizado correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_delete_tipos_persona(
    IN p_id INT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;
    SELECT COUNT(*) INTO v_existente FROM tipos_persona WHERE id = p_id;
    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        DELETE FROM tipos_persona WHERE id = p_id;
        SET Respuesta = 'Tipo de persona eliminado correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_select_puertas_acceso()
BEGIN
    SELECT id, nombre FROM puertas_acceso ORDER BY id;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_insert_puertas_acceso(
    IN p_nombre VARCHAR(50),
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET Respuesta = 'Error al insertar la puerta (Posible duplicado)';
    END;

    INSERT INTO puertas_acceso (nombre) VALUES (p_nombre);
    SET Respuesta = 'Puerta insertada correctamente';
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_update_puertas_acceso(
    IN p_id INT,
    IN p_nombre VARCHAR(50),
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;
    SELECT COUNT(*) INTO v_existente FROM puertas_acceso WHERE id = p_id;
    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        UPDATE puertas_acceso SET nombre = p_nombre WHERE id = p_id;
        SET Respuesta = 'Puerta actualizada correctamente';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_delete_puertas_acceso(
    IN p_id INT,
    OUT Respuesta VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;
    SELECT COUNT(*) INTO v_existente FROM puertas_acceso WHERE id = p_id;
    IF v_existente = 0 THEN
        SET Respuesta = 'ID no encontrado';
    ELSE
        DELETE FROM puertas_acceso WHERE id = p_id;
        SET Respuesta = 'Puerta eliminada correctamente';
    END IF;
END $$

DELIMITER ;