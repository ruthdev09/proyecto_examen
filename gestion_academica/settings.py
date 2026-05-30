import os
from pathlib import Path
import dj_database_url  # Importante: pip install dj-database-url

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SEGURIDAD ---
# ¡ESTA ES LA LÍNEA QUE FALTABA! 
SECRET_KEY = 'django-insecure-yt$)f3$(#&sf160#g&l4&+hrb(j3c5od2rvevmj_vwa$bdjt^e'

# DEBUG es True para que puedas ver los errores mientras terminas el examen
DEBUG = True 

# Permitir todas las URLs para que funcione en Railway o cualquier hosting
ALLOWED_HOSTS = ['*']  # Vercel y cualquier dominio

CSRF_TRUSTED_ORIGINS = [
    'https://*.vercel.app',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

# Definición de Aplicaciones
INSTALLED_APPS = [
    'cloudinary_storage',  # Debe ir antes de staticfiles
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary',          # Librería de Cloudinary
    'django.contrib.staticfiles',
    'core',                # Tu aplicación principal
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Para servir CSS en la nube
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gestion_academica.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gestion_academica.wsgi.application'

# Configuración de Base de Datos — PostgreSQL en Neon
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://neondb_owner:npg_CIPxc5hu1vqQ@ep-little-silence-aqskh11v-pooler.c-8.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require',
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Validadores de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internacionalización (Configurado a español)
LANGUAGE_CODE = 'es-pe'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True

# Archivos Estáticos (CSS, JS)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configuración de Imágenes (Media)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# --- CONFIGURACIÓN DE CLOUDINARY ---
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dko2gdspm',
    'API_KEY': '764449157151482',
    'API_SECRET': '8WptNgfUdJjxXSlPSqgzCUhJfp8',
}

# Django 4.2+ usa STORAGES en lugar de DEFAULT_FILE_STORAGE / STATICFILES_STORAGE
STORAGES = {
    # Imágenes subidas por usuarios → Cloudinary (evita el filesystem read-only de Vercel)
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    # Archivos estáticos → Whitenoise (CSS, JS)
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Configuración de mensajes (Alertas)
from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {
    message_constants.DEBUG: 'secondary',
    message_constants.INFO: 'info',
    message_constants.SUCCESS: 'success',
    message_constants.WARNING: 'warning',
    message_constants.ERROR: 'error',
}

# Tipo de campo de ID por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'