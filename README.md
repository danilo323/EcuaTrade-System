# 🇪🇨 EcuaTrade-System: Core Marketplace Backend

![Python](https://img.shields.io/badge/Language-Python%203.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Framework-Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Architecture](https://img.shields.io/badge/Architecture-MVT--Clean%20Code-FF6F00?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Desarrollo%20Activo-brightgreen?style=for-the-badge)

## 📌 SOBRE EL PROYECTO

**EcuaTrade-System** es una solución tecnológica integral diseñada para dinamizar el comercio en el mercado ecuatoriano. La plataforma actúa como un puente digital entre dos sectores estratégicos:
1. **TECNOLOGÍA DE CONSUMO:** Comercialización de periféricos de PC de alto rendimiento.
2. **SECTORES PRODUCTIVOS:** Intercambio de productos de los sistemas acuícolas, pesqueros, ganaderos y agrícolas.

Este sistema implementa validaciones rigurosas de identidad nacional y gestión de inventario profesional bajo el framework Django.

---

## 🛠️ ESPECIFICACIONES TÉCNICAS

### 🔐 MOTOR DE VALIDACIÓN DE IDENTIDAD
El sistema garantiza la integridad de los datos mediante validadores personalizados:
* **ALGORITMO DE CÉDULA:** Implementación del algoritmo de verificación del décimo dígito (Módulo 10) para asegurar identidades reales en Ecuador.
* **SANITIZACIÓN:** Limpieza de datos y formateo automático de texto.
* **INTEGRIDAD DE STOCK:** Validadores personalizados en el servidor para impedir precios o existencias negativas.

### 💾 PERSISTENCIA Y ADMINISTRACIÓN
* **Django ORM:** Gestión eficiente de base de datos SQLite.
* **Panel Administrativo:** Interfaz profesional para la gestión de productos y stock con logs de auditoría.

---

## 📂 ESTRUCTURA DEL PROYECTO (MVT Architecture)

```text
EcuaTrade-System/
├── ecuatrade_pro/       # Configuración central del proyecto (Settings, URLs)
├── inventario/          # App de gestión de productos
│   ├── models.py        # Definición de tablas de base de datos
│   ├── validators.py    # Lógica de validación personalizada
│   └── admin.py         # Configuración del panel de administración
├── src/                 # Legacy Core (Lógica original de validación)
├── .gitignore           # Filtro de archivos para el repositorio
├── manage.py            # Orquestador del Framework
└── requirements.txt     # Dependencias del sistema

```

### 1. Crear el entorno virtual
```bash
python -m venv .venv
```

### 2. Activar el entorno virtual
```bash
.venv\Scripts\activate
```


### 3. # Instalar Django y las librerías necesarias 
```bash
pip install -r requirements.txt
```


### 4. # Crear los archivos de migración
```bash
python manage.py makemigrations
```


### 5. Aplicar las migraciones a SQLite
```bash
python manage.py migrate
```

### 6. Iniciar el motor de Django
```bash
python manage.py runserver

```




