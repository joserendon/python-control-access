# Sistema de Control de Acceso a Empresa

Este proyecto implementa una base de datos relacional para el registro y control de accesos a instalaciones empresariales, incluyendo gestión de usuarios, visitantes, motivos de visita y auditoría de acciones.

## 🧱 Estructura General

La base de datos se llama: `control_acceso_empresa`.

Está diseñada para soportar:

- Registro de usuarios internos (empleados, guardias, administradores)
- Registro de visitantes externos y sus empresas
- Registro de accesos (entradas y salidas)
- Control de roles y estados de usuarios
- Auditoría de operaciones críticas

---

## 📁 Tablas Principales

### Usuarios y Seguridad

| Tabla             | Descripción                                 |
|------------------|---------------------------------------------|
| `usuarios`        | Información de usuarios del sistema         |
| `roles`           | Catálogo de roles (admin, guardia, etc.)    |
| `estados`         | Estado activo/inactivo de usuarios          |

### Catálogos

| Tabla              | Descripción                                  |
|-------------------|----------------------------------------------|
| `areas`            | Áreas físicas de la empresa (Recepción, etc.)|
| `motivos`          | Motivos por los cuales una persona visita    |
| `tipos_documento`  | Tipos de documentos de identidad              |
| `empresas`         | Empresas asociadas a visitantes externos     |
| `tipos_persona`    | Interno / Externo                             |
| `tipos_acceso`     | Entrada / Salida                              |
| `puertas_acceso`   | Entradas físicas (principal, carga, etc.)    |
| `acciones`         | Tipos de acciones para la auditoría          |

### Operativas

| Tabla         | Descripción                                     |
|--------------|-------------------------------------------------|
| `personas`    | Registro de personas (empleados y visitantes)   |
| `accesos`     | Registro de eventos de entrada/salida           |
| `auditoria`   | Registro de acciones del sistema (logs)         |

---

## 🔗 Relaciones Clave

- Un `usuario` tiene un `rol` y un `estado`
- Una `persona` puede ser **empleado** o **visitante**
- Una `persona` puede (opcionalmente) pertenecer a una `empresa`
- Un `acceso` asocia una persona, puerta, área, motivo y tipo de acceso
- Cada acción relevante se registra en `auditoria` con usuario y acción correspondiente

---

## ⚙️ Instalación

1. Asegúrate de tener MySQL instalado.
2. Ejecuta el script `create_database.sql` (o el contenido proporcionado) en tu gestor favorito (MySQL Workbench, DBeaver, CLI, etc.)

```bash
mysql -u root -p < create_database.sql
