"""
Django settings for schoolsys project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

from decouple import config
from dj_database_url import parse as dburl

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.vercel.app']


# Time and Date Config
USE_L10N = False
DATE_INPUT_FORMATS = ('%d-%m-%Y', '%d/%m/%Y', '%d/%m/%y')
DATETIME_INPUT_FORMATS = ('%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M', '%d/%m/%Y',)


TIME_ZONE = 'America/Sao_Paulo'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrapform',
    'datepickerwidget',
    'debug_toolbar',
    'cpffield',
    'localflavor',
    'student',
    'exam',
    'crispy_forms',
    'calendar_app',
    'dashboard',
    # Third-Party Apps
    'rest_framework',
    'rest_framework.authtoken',  # <-- Here
    # Local Apps (Your project's apps)
    'core',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # <-- And here
    ],
    # 'DATE_INPUT_FORMATS': ['%d-%m-%Y', '%d/%m/%Y', '%d/%m/%y', '%d %b %Y', ],
    # 'DATETIME_INPUT_FORMATS': ['%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M', '%d/%m/%Y']
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'schoolsys.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'schoolsys.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
# 'default': {
#  'ENGINE': 'django.db.backends.sqlite3',
# 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
# #}#
# }


default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {'default': config(
    'DATABASE_URL', default=default_dburl, cast=dburl), }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'student.Student'

CRYPTOGRAPHY_KEY = None
CRYPTOGRAPHY_SALT = 'django-cryptography'

SIGNING_BACKEND = 'django_cryptography.core.signing.TimestampSigner'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Obs: Deve ser retirado caso aqui haja codigos de setando date and tz

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'


LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'home'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'schoolsystem.django@gmail.com'
EMAIL_HOST_PASSWORD = 'qwerty!@#'
