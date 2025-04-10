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
    estado VARCHAR(50) NOT NULL UNIQUE
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
