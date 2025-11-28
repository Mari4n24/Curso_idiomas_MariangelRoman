# Proyecto Curso de Idiomas (Django)

    Este es mi proyecto de Django donde armé una plataforma para gestionar cursos de 
idiomas. Acá se pueden registrar usuarios, iniciar sesión y manejar cursos, profesores y alumnos. La idea es que sea simple, usable y que se pueda ver todo desde una interfaz limpia.

---

##  ¿Qué hace mi proyecto?

- Muestra un **inicio** y un **about**.
- Permite **registrar usuarios** y **loguearse**.
- Tiene CRUD completo de:
  - **Cursos**
  - **Profesores**
  - **Alumnos**
- Puedes:
  - Crear, editar, borrar y listar cursos  
  - Subir imágenes de los cursos  
  - Usar formularios personalizados  
  - Ver detalles individuales  
  - Buscar cursos desde un buscador básico  
- Algunas secciones solo se ven si el usuario está logueado (seguridad básica).

---

## Tecnologías que usé

- **Python 3**
- **Django 5**
- **HTML, CSS y Bootstrap**
- **SQLite** como base de datos  
- Archivos estáticos en `/static/`  
- Subida de imágenes en `/media/`

---

## Estructura general del proyecto

```
curso_idiomas/            # Configuración principal
curso/                    # CRUD de cursos, alumnos y profesores
inicio/                   # Página de inicio y about
usuarios/                 # Registro e inicio de sesión
media/                    # Imágenes de los cursos
static/                   # CSS, JS e imágenes estáticas
templates/                # HTML organizados por app
manage.py
requirements.txt
```

---

## Cómo correr el proyecto

### 1. Crear el entorno virtual
```bash
python -m venv .venv
```

Activarlo:

**Windows**
```bash
. .venv\Scripts\activate
```

**Linux/Mac**
```bash
source venv/bin/activate
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Migrar la base de datos
```bash
python manage.py migrate
```

### 4. Correr el servidor
```bash
python manage.py runserver
```

Abrís:  
    http://127.0.0.1:8000/

---

## Usuarios y autenticación

- Para crear cursos, profesores o alumnos necesitás estar logueado.
- Los formularios ya validan datos.
- Si querés entrar al admin:

```bash
python manage.py createsuperuser
```

---

## Cosas que hice y me parecieron importantes

- Organicé todas las vistas en plantillas separadas.
- Agregué imágenes reales de cursos dentro de `/media`.
- Personalicé el CSS para que no quede igual a la plantilla original.
- Mejoré el footer, el navbar y el estilo general.
- Dejé todo listo para que después pueda agregar más apps si quiero.

---

## Autora

    Proyecto desarrollado por **Mariangel Román**, como parte de mis prácticas de Django.  
Mi idea fue aprender bien cómo funcionan los CRUD, las rutas, los templates y el sistema de usuarios.