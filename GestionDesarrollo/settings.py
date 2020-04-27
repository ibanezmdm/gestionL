"""
Django settings for GestionDesarrollo project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import yaml
import os

stream = open('config.yml', 'r')
settings = yaml.load(stream, yaml.SafeLoader)
# authorize_url = '{0}{1}'.format(settings['authority'], settings['authorize_endpoint'])
# token_url = '{0}{1}'.format(settings['authority'], settings['token_endpoint'])


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{}'.format(settings['SECRET_KEY'])

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(settings['DEBUG'])


# !! Aqui se registra la ip que formara parte del host de de la aplicacion
ALLOWED_HOSTS = ['{}'.format(settings['HOST'])]


# Application definition

INSTALLED_APPS = [
    'registration.apps.RegistrationConfig',
    'frontend.apps.FrontendConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'proveedores.apps.ProveedoresConfig',
    'colaboracion.apps.ColaboracionConfig',
    'tableros.apps.TablerosConfig',
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

ROOT_URLCONF = 'GestionDesarrollo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'GestionDesarrollo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': '{}'.format(settings['DATABASE_ENGINE']),
        'NAME': '{}'.format(settings['DATABASE_NAME']),
        'HOST': '{}'.format(settings['DATABASE_HOST']),
        'USER': '{}'.format(settings['DATABASE_USER']),
        'PASSWORD': '{}'.format(settings['DATABASE_PASSWORD']),
        'PORT': '{}'.format(settings['DATABASE_PORT']),
        'OPTIONS': {
            'driver': '{}'.format(settings['DATABASE_OPTION_DRIVER']),
            'isolation_level': '{}'.format(settings['DATABASE_OPTION_INSOLATION_LEVEL']),
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/


# Se cambia idioma la español
LANGUAGE_CODE = '{}'.format(settings['LANGUAGE_CODE'])

# Se agrega Zona horaria.
TIME_ZONE = '{}'.format(settings['TIME_ZONE'])

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')


# REGISTRATION CONFIG
LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'
