# 🇪🇨 EcuaTrade-System: Core Marketplace Backend

![Python](https://img.shields.io/badge/Language-Python%203.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Framework-Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Architecture](https://img.shields.io/badge/Architecture-Clean%20Code-FF6F00?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Desarrollo%20Activo-brightgreen?style=for-the-badge)

## 📌 SOBRE EL PROYECTO

**EcuaTrade-System** es una solución tecnológica integral diseñada para dinamizar el comercio en el mercado ecuatoriano. La plataforma actúa como un puente digital entre dos sectores estratégicos:
1. **TECNOLOGÍA DE CONSUMO:** Comercialización de periféricos de PC de alto rendimiento.
2. **SECTORES PRODUCTIVOS:** Intercambio de productos de los sistemas acuícolas, pesqueros, ganaderos y agrícolas.

Este repositorio contiene la **Lógica de Negocio (Back-End)**, implementando validaciones de identidad nacional y gestión de persistencia en memoria bajo el paradigma de **Programación Orientada a Objetos (POO)**.

---

## 🛠️ ESPECIFICACIONES TÉCNICAS

### 🔐 MOTOR DE VALIDACIÓN DE IDENTIDAD (ECUADOR)
El sistema garantiza la integridad de la base de datos mediante validadores personalizados:
* **ALGORITMO DE CÉDULA:** Implementación del algoritmo de verificación del décimo dígito (Módulo 10) para asegurar que cada usuario posee una identidad real en el territorio nacional.
* **SANITIZACIÓN DE DATOS:** Limpieza y formateo de cadenas de texto (Title Case) para nombres y apellidos, asegurando uniformidad estética y profesional.
* **INTEGRIDAD DE EMAIL:** Validación de sintaxis de correo electrónico para evitar registros erróneos.

### 💾 GESTIÓN DE PERSISTENCIA: MEMORY REPOSITORY
Se ha desarrollado una capa de persistencia temporal (`clsMemoryRepository`) que permite:
* **DETECCIÓN DE DUPLICADOS:** Algoritmo de búsqueda que bloquea registros con cédulas o correos electrónicos previamente existentes en el sistema.
* **PRUEBAS DE ALTA VELOCIDAD:** Almacenamiento eficiente en RAM para validación de flujo de usuario sin dependencia de motores de base de datos externos.

---

## 📂 ESTRUCTURA DEL DIRECTORIO

```text
EcuaTrade-System/
├── src/
│   ├── core/           # Validadores de cédula, correo y nombres.
│   ├── use_cases/      # Lógica del caso de uso "Registrar Usuario".
│   └── repository/     # Almacenamiento temporal (MemoryRepository).
├── tests/              # Pruebas unitarias de componentes.
└── test_register.py    # Punto de entrada principal para demostraciones.