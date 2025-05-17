# 🐍 Proyecto Django: Encuestas

Este es un pequeño proyecto desarrollado con **Django** como parte de un tutorial y aprendizaje personal.

Incluye:  
- Una app llamada `polls` para crear y votar en encuestas.  
- Personalización del panel de administración.  
- Uso de un entorno virtual (`entorno_chido`).

---

## 🚀 Cómo ejecutar el proyecto

Cloná el repositorio con:

git clone https://github.com/RonaldoUrnau/django_proyecto_tutorial
cd django_proyecto_tutorial

Creá un entorno virtual:

python -m venv entorno_chido

Activá el entorno virtual (en Windows):

.\entorno_chido\Scripts\activate

O en Linux/macOS:

source entorno_chido/bin/activate

Instalá las dependencias con:

pip install -r requirements.txt

Aplicá las migraciones y ejecutá el servidor:

python manage.py migrate  
python manage.py runserver

---

## 🗂️ Estructura del proyecto

proyecto/  
├── mysite/          # Configuración general del proyecto  
├── polls/           # App principal  
├── templates/       # Personalización del admin  
├── db.sqlite3       # Base de datos (SQLite)  
└── manage.py
