"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

import setting_secrets

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = setting_secrets.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = setting_secrets.DEBUG

if DEBUG:
    INTERNAL_IPS = ["127.0.0.1"]

ALLOWED_HOSTS = setting_secrets.ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fulfillmentapp',
    "debug_toolbar", 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware"
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
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


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = setting_secrets.DATABASES

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': (u'%(asctime)-s %(levelname)s [%(name)s]: %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'encoding': 'utf-8',
        },
    },
    'handlers': {
        'db': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/sql_logs.log',
            'formatter': 'default'
        },
        'requests': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/dj_requests.log',
            'formatter': 'default',
        },
        'bot': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/bot_logs.log',
            'formatter': 'default',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['db'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['requests'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'bot.events': {
            'handlers': ['bot'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

CACHES = setting_secrets.CACHES

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "/main/"
LOGOUT_REDIRECT_URL = "/"

# Токен telegram бота
TOKEN = setting_secrets.TOKEN
