"""
Django settings for project project.
Generated by 'django-admin startproject' using Django 4.1.5.
For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import mimetypes
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ХХХ

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'NewsPortal',
    'debug_toolbar',
    'NewsPortal.apps.NewsportalConfig',
    'django_filters',
    'django.contrib.sites',
    'allauth',
    'allauth.socialaccount.providers.google',
    'allauth.account',
    'allauth.socialaccount',
    'django_apscheduler',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGIN_REDIRECT_URL = 'post_list'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

ACCOUNT_FORMS = {'signup': 'NewsPortal.forms.BasicSignupForm'}

EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 2525
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'Foma26199622@mail.ru'
EMAIL_HOST_PASSWORD = 'zu3sA5BMqakJnUvF5PEc'

DEFAULT_FROM_EMAIL = 'Foma26199622@mail.ru'

EMAIL_SUBJECT_PREFIX = 'Ошибка! '
SERVER_EMAIL = 'Foma26199622@mail.ru'

ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'ok'
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'ok'

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'TIMEOUT': 60,
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]

ADMINS = (
    ('admin', 'Foma26199622@mail.ru'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'console_debug': {
            'format': '%(name)-12s %(asctime)s %(levelname)-8s %(message)s'
        },
        'console_warning': {
            'format': '%(name)-12s %(asctime)s %(levelname)-8s %(pathname)s %(message)s'
        },
        'console_error': {
            'format': '%(name)-12s %(asctime)s %(levelname)-8s %(pathname)s %(exc_info)s %(message)s'
        },
        'file_info': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(module)s %(message)s'
        },
    },
    'filters': {
        'debug_false': {'()': 'django.utils.log.RequireDebugFalse'},
        'debug_true': {'()': 'django.utils.log.RequireDebugTrue'}
    },
    'handlers': {
        'console_debug': {
            'class': 'logging.StreamHandler',
            'formatter': 'console_debug',
            'filters': ['debug_true']
        },
        'console_warning': {
            'class': 'logging.StreamHandler',
            'formatter': 'console_warning',
            'filters': ['debug_true']
        },
        'console_error': {
            'class': 'logging.StreamHandler',
            'formatter': 'console_error',
            'filters': ['debug_true']
        },
        'file_general': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'file_info',
            'filename': 'general.log'
        },
        'file_errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'console_error',
            'filename': 'errors.log'
        },
        'file_security': {
            'class': 'logging.FileHandler',
            'formatter': 'file_info',
            'filename': 'security.log'
        },
        'email': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'console_error',
            'filters': ['debug_false']
        }
    },
    'loggers': {
        'django': {
            'level': 'DEBUG',
            'handlers': ['console_debug', 'console_warning', 'console_error', 'file_general'],
            'propagate': False
        },
        'django.request': {
            'level': 'ERROR',
            'handlers': ['file_errors', 'email']
        },
        'django.server': {
            'level': 'DEBUG',
            'handlers': ['file_errors', 'email']
        },
        'django.template': {
            'level': 'DEBUG',
            'handlers': ['file_errors']
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['file_errors']
        },
        'django.security': {
            'level': 'DEBUG',
            'handlers': ['file_security']
        },
    }
}

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]
