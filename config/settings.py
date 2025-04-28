import os
from pathlib import Path

# 1. Rutas base
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Variables de entorno para seguridad
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-fallback-key-para-dev'  # SOLO desarrollo; en prod carga desde env
)

DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

# ALLOWED_HOSTS desde entorno, separado por comas
hosts = os.environ.get('DJANGO_ALLOWED_HOSTS', '')
ALLOWED_HOSTS = hosts.split(',') if hosts else []

# 3. Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',   # tu app principal
]

# 4. Middleware
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

# 5. Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],           # si tienes templates globales, agrégalos aquí
        'APP_DIRS': True,     # busca en core/templates/...
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

# 6. Base de datos PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB',     'plataforma_db'),
        'USER': os.environ.get('POSTGRES_USER',   'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASS','1278'),
        'HOST': os.environ.get('POSTGRES_HOST',   'localhost'),
        'PORT': os.environ.get('POSTGRES_PORT',   '5432'),
    }
}

# 7. Validadores de contraseña
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# 8. Internacionalización
LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'UTC'
USE_I18N      = True
USE_TZ        = True

# 9. Archivos estáticos
STATIC_URL  = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# 10. Campo clave por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 11. Redirecciones post-login/logout
LOGIN_REDIRECT_URL  = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
