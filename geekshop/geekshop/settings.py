"""
Django settings for geekshop project.
Generated by 'django-admin startproject' using Django 3.2.11.
For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-&yrf9gq10(fpi=7@)!+_1%3e$@ed^7_$04qbb_l$ps+=utgro4"

DJANGO_PRODUCTION = bool(os.environ.get('DJANGO_PRODUCTION', False))
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not DJANGO_PRODUCTION

ALLOWED_HOSTS = ['127.0.0.1'] if DJANGO_PRODUCTION else []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "social_django",

    "mainapp",
    "authapp",
    "basketapp",
    "adminapp",
    "ordersapp",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
]

ROOT_URLCONF = "geekshop.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
                "mainapp.context_processors.menu_links",
            ],
        },
    },
]

WSGI_APPLICATION = "geekshop.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if DJANGO_PRODUCTION:
    DJANGO_DB_NAME = os.environ.get('DJANGO_DB_NAME')
    DJANGO_DB_USER = os.environ.get('DJANGO_DB_USER')
    DJANGO_DB_PASSWORD = os.environ.get('DJANGO_DB_PASSWORD')
    DJANGO_DB_HOST = os.environ.get('DJANGO_DB_HOST')
    DJANGO_DB_PORT = int(os.environ.get('DJANGO_DB_PORT', '0'))

    assert all([
         DJANGO_DB_NAME, 
        DJANGO_DB_USER,
        DJANGO_DB_PASSWORD,
        DJANGO_DB_HOST,
        DJANGO_DB_PORT,
    ])
    
    DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME":  DJANGO_DB_NAME,
        "USER": DJANGO_DB_USER,
        "PASSWORD":  DJANGO_DB_PASSWORD,
        "HOST": DJANGO_DB_HOST,
        "PORT": DJANGO_DB_PORT,
    }
}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


AUTH_USER_MODEL = "authapp.ShopUser"


LOGIN_URL = "auth:login"

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.github.GithubOAuth2',
)

SOCIAL_AUTH_GUTHUB_OAUTH2_SCOPE = ['user',]


SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'authapp.pipeline.get_user_location_and_bio',
)



with open("./credentials.json", "r") as credentials_file: 
    credentials = json.load(credentials_file)   
    SOCIAL_AUTH_GITHUB_KEY = credentials['GITHUB_KEY']
    SOCIAL_AUTH_GITHUB_SECRET = credentials['GITHUB_SECRET']

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'tmp/emails/'
DOMAIN_NAME = 'localhost'
