# CafeBar

Sistema de gestión para cafeterías, desarrollado con Django y Django REST Framework.

## Funcionalidades
- Gestión de usuarios (clientes, administradores, meseros, baristas).
- CRUD para productos, órdenes, pagos, inventarios, reservas y proveedores.
- Gestión de menús dinámicos.
- API REST para interactuar con el sistema.
- Panel de administración para gestionar los datos.

## Requisitos
Antes de iniciar el proyecto, asegúrate de tener instalados los siguientes requisitos:
- **Python 3.12 o superior**: [Descargar Python](https://www.python.org/downloads/)
- **PostgreSQL**: [Descargar PostgreSQL](https://www.postgresql.org/download/)
- **Git**: [Descargar Git](https://git-scm.com/downloads)

## Instalación
Sigue estos pasos para configurar y ejecutar el proyecto:

### 1. Clonar el repositorio
Clona el repositorio desde GitHub:
```bash
git clone https://github.com/Felipe0206/CafeBar.git
cd CafeBar
```

### 2. Crear un entorno virtual
Crea y activa un entorno virtual para instalar las dependencias:
```bash
python -m venv venv
```
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```

### 3. Instalar las dependencias
Instala las dependencias necesarias desde el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos
Edita el archivo `CafeBar/settings.py` y configura las credenciales de tu base de datos PostgreSQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cafebar',  # Nombre de la base de datos
        'USER': 'postgres',  # Usuario de PostgreSQL
        'PASSWORD': 'TuContraseña',  # Contraseña del usuario
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Aplicar las migraciones
Ejecuta las migraciones para crear las tablas en la base de datos:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear un superusuario
Crea un superusuario para acceder al panel de administración:
```bash
python manage.py createsuperuser
```
Sigue las instrucciones para configurar un nombre de usuario, correo electrónico y contraseña.

### 7. Iniciar el servidor
Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```

Accede a:
- **Página de inicio**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Panel de administración**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Uso
- **API REST**: Interactúa con los endpoints de la API en [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/).
- **Panel de administración**: Gestiona los datos desde el panel de administración.

## Notas adicionales
- Si necesitas cambiar el puerto del servidor, usa:
  ```bash
  python manage.py runserver 8080
  ```
- Para desplegar el proyecto en producción, configura `DEBUG = False` en `settings.py` y usa un servidor web como Nginx o Apache.

## Licencia
Este proyecto está bajo la licencia MIT.
