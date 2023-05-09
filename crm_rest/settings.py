"""
Django settings for crm_rest project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=a)jb1mrwei44@6n!vwb0ni^-n=q%-7g(^8bpcofb$s#@mvz5q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'drf_yasg',
    'corsheaders',
    'rest_framework_simplejwt.token_blacklist',
    'rest_framework',
    'Auth',
    'App',
    'Client',
    'Coming',
    'Personal',
    'Agreement',
    'Cashbox',
]

REST_FRAMEWORK = { 
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5), # Время жизни access-токена
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=15), # Время жизни refresh-токена
    'ROTATE_REFRESH_TOKENS': True, # При каждом обновлении access-токена создается новый refresh-токен
    'BLACKLIST_AFTER_ROTATION': True, # Добавляет использованный refresh-токен в blacklist
    'UPDATE_LAST_LOGIN': False, # Не обновляет поле last_login при создании токена
    'ALGORITHM': 'HS256', # Алгоритм шифрования
    'SIGNING_KEY': SECRET_KEY, # Секретный ключ
    'VERIFYING_KEY': None, # Публичный ключ, используется при декодировании токена
    'AUTH_HEADER_TYPES': ('Bearer',), # Тип заголовка авторизации
    'USER_ID_FIELD': 'id', # Название поля идентификатора пользователя в токене
    'USER_ID_CLAIM': 'user_id', # Название поля идентификатора пользователя в пайлоуде токена
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',), # Классы для создания токенов
    'TOKEN_TYPE_CLAIM': 'token_type', # Название поля типа токена в пайлоуде токена
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'crm_rest.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    # 'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'crm_rest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'crm',
#         'USER': 'crmuser',
#         'PASSWORD': 'crmuserpass',
#         'HOST': 'db',
#         'PORT': '3306',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crm',
        'USER': 'crmuser',
        'PASSWORD': 'crmuserpass',
        'HOST': '45.81.224.229',
        'PORT': '90',
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

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
