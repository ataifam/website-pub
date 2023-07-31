"""
Django settings for MyWebsite project.
sup
Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
import secrets
import django_on_heroku
import dj_database_url
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.environ.get('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['ataifou1projects']


# Application definition

INSTALLED_APPS = [
    'storages',
    'captcha',
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'main',
    'social',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'MyWebsite.urls'

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

WSGI_APPLICATION = 'MyWebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': str(os.environ.get('DATABASE_NAME')),
        'USER': str(os.environ.get('DATABASE_USER')),
        'PASSWORD': str(os.environ.get('DATABASE_PASS')),
        'HOST': str(os.environ.get('DATABASE_HOST')),
        'PORT': str(os.environ.get('DATABASE_PORT')),
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

RECAPTCHA_PUBLIC_KEY = str(os.environ.get('RECAPTCHA_PUBLIC_KEY'))
RECAPTCHA_PRIVATE_KEY = str(os.environ.get('RECAPTCHA_PRIVATE_KEY'))

AWS_ACCESS_KEY_ID = str(os.environ.get('S3_KEY'))
AWS_SECRET_ACCESS_KEY = str(os.environ.get('S3_SECRET'))
AWS_STORAGE_BUCKET_NAME = str(os.environ.get('BUCKET_NAME'))
AWS_S3_REGION_NAME = 'us-east-2'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATIC_URL = f"{AWS_S3_CUSTOM_DOMAIN}/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = f"{AWS_S3_CUSTOM_DOMAIN}/" + 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = str(os.environ.get('EMAIL_USER'))
EMAIL_HOST_PASSWORD = str(os.environ.get('EMAIL_PASS'))
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_SSL_REDIRECT = True

CSP_DEFAULT_SRC = ('none', )
CSP_CONNECT_SRC = ('none')
CSP_STYLE_SRC = ('self', 'https://cdn.jsdelivr.net/', AWS_S3_CUSTOM_DOMAIN)
CSP_SCRIPT_SRC = ('self', AWS_S3_CUSTOM_DOMAIN, 'https://cdn.jsdelivr.net/', 'https://www.google.com/recaptcha/api.js', 'https://www.gstatic.com/recaptcha/')
CSP_CHILD_SRC = ('https://www.google.com/recaptcha/',)
CSP_IMG_SRC = ('self', AWS_S3_CUSTOM_DOMAIN, 'data:')
CSP_FONT_SRC = ('self', AWS_S3_CUSTOM_DOMAIN, 'https://cdn.jsdelivr.net/')
CSP_INCLUDE_NONCE_IN = [
    'script-src',
]

CORS_ORIGIN_WHITELIST = [
'https://www.ataifou1projects.com',
]

django_on_heroku.settings(locals(), staticfiles=False)