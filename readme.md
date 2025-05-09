# 🧠 Gestor de Tareas - API RESTful con Django & DRF

Esta es una API RESTful para la gestión de tareas, construida con Django y Django REST Framework.

---

## 🚀 Características

- Operaciones CRUD completas sobre tareas
- Serialización automática con Django REST Framework
- Estructura profesional para producción
- Fácil de extender con autenticación, archivos y más

---

## 📦 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/gestor-tareas.git
   cd gestor-tareas

2.- Crea y activa un entorno virtual:
    python -m venv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # Linux/macOS

3.-Instala dependencias:
    pip install -r requirements.txt 

4.-Realiza migraciones:
    python manage.py migrate

5.-Ejecuta el servidor:
    python manage.py runserver

📬Endpoints principales
Método	Endpoint	Descripción
GET	/api/tareas/	Listar todas las tareas
POST	/api/tareas/	Crear una nueva tarea
GET	/api/tareas/{id}/	Ver detalles de una tarea
PUT	/api/tareas/{id}/	Actualizar una tarea
DELETE	/api/tareas/{id}/	Eliminar una tarea


📄 Licencia
Este proyecto está bajo la licencia MIT. Libre para usar, modificar y compartir.