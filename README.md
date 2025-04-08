# 🛡️ Sistema de Control de Acceso Empresarial

Este proyecto implementa una base de datos relacional en MySQL para el control de entradas y salidas de visitantes en una empresa. Incluye la validación de datos clave como documento, área visitada y motivo de la visita, con trazabilidad en tiempo real.

---

## 📦 Características

- Registro de visitantes con documento único.
- Registro de entradas y salidas con marca de tiempo.
- Catálogo de áreas internas de la empresa.
- Catálogo de motivos de visita.
- Relaciones bien definidas entre entidades.
- Preparado para integración con aplicaciones web o móviles.

---

## 🧱 Estructura de la Base de Datos

- `visitantes`: Personas que ingresan a la empresa.
- `areas`: Lugares dentro de la empresa que pueden ser visitados.
- `motivos`: Razones estandarizadas por las cuales se permite el ingreso.
- `accesos`: Registro de cada entrada o salida.

---

## 🗄️ Modelo Relacional

```plaintext
visitantes ---< accesos >--- areas
                         |
                         v
                      motivos
