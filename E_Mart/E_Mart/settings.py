"""
Django settings for E_Mart project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x#1c03n(&5_1p*68)6_w26@(342u^f0if4ym#!6lh&5sx1@37o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
AUTH_USER_MODEL='Home_Module.User'
AUTHENTICATION_BACKENDS=(
    'django.contrib.auth.backends.AllowAllUsersModelBackend',
    'Home_Module.Backend.BackendSetting'
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #for creating rest api's
     'rest_framework',
     #to ensure only authorize domains can access our Api's
    'corsheaders',

    #to use Allauth library
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #providers i.e google,facebook
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    

    #local apps
    'Home_Module',
]
#only White List domains can access our Api's
CORS_ALLOWED_ORIGINS = [
 
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    #manully added
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'E_Mart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'E_Mart.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
LOGIN_REDIRECT_URL = "/"

SITE_ID=1

STATIC_URL = '/static/'
MEDIA_URL='/Images/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]
MEDIA_ROOT=os.path.join(BASE_DIR,'Home_Module/static/Images')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'emart1354@gmail.com' 
EMAIL_HOST_PASSWORD = 'mcsf19@emart'
EMAIL_USE_SSL=False



DEFAULT_FROM_EMAIL = os.environ.get('emart1354@gmail.com')

