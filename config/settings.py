import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Usa DEBUG=True en tu entorno local
DEBUG = os.environ.get('DJANGO_ENV') != 'production'

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-...')

ALLOWED_HOSTS = ['nick2l.pythonanywhere.com'] if not DEBUG else []

# --------------------------------------------------
# Selección de base de datos según entorno
if DEBUG:
    # Desarrollo local con SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    # Producción en PythonAnywhere con Postgres
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql',
            'NAME':     'plataforma_db',
            'USER':     'postgres',
            'PASSWORD': '1278',
            'HOST':     'localhost',
            'PORT':     '5432',
        }
    }
# --------------------------------------------------


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'



# Internationalization, validadores, etc. (igual que antes)…

# Static files (CSS, JS, imágenes)
STATIC_URL = '/static/'

# Directorio donde collectstatic copiará todos los archivos
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redirecciones tras login/logout
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
