"""
Django settings for report_trade_sanctions_breach project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import environ

from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env()

# TODO: replace os.environ[""] with env("") throughout?
# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ["SECRET_KEY"]
SECRET_KEY = env("SECRET_KEY")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

VCAP_SERVICES = env.json('VCAP_SERVICES', default={})

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "crispy_forms_gds",
    "report_breach_web_service",
    "django_chunk_upload_handlers",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = ("bootstrap", "bootstrap3", "bootstrap4", "uni_form", "gds")
CRISPY_TEMPLATE_PACK = "gds"

# File storage
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

CLAM_AV_USERNAME = env("CLAM_AV_USERNAME", default=None)
CLAM_AV_PASSWORD = env("CLAM_AV_PASSWORD", default=None)
CLAM_AV_DOMAIN = env("CLAM_AV_DOMAIN", default=None)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "report_trade_sanctions_breach.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "report_trade_sanctions_breach.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "breach_prototype",
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASSWORD"],
        "HOST": "localhost",
        "PORT": "",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

FILE_UPLOAD_HANDLERS = (
    "django_chunk_upload_handlers.clam_av.ClamAVFileUploadHandler",
    "django_chunk_upload_handlers.s3.S3FileUploadHandler",
)  # Order is important

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
WEB_SERVICE_STATIC_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../report_breach_web_service", "static")
)
# used by djangos manage.py collectstatic command which copies the static files into the
# top level project directory
# more info: https://docs.djangoproject.com/en/4.2/ref/contrib/staticfiles/
# The copied folder has been added to .gitignore
# This may need to be revisited when we are deploying to a cloud env
STATICFILES_DIRS = (WEB_SERVICE_STATIC_DIR,)  # /PS-IGNORE

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
