"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

import dj_database_url
import environ
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

env = environ.Env(
    DEBUG=(bool, False),
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
BASE_DIR = ROOT_DIR

SECRET_KEY = env.str("DJANGO_SECRET_KEY")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

OUR_APPS = ["report_a_breach", "healthcheck"]

THIRD_PARTY_APPS = [
    "crispy_forms",
    "crispy_forms_gds",
    "django_chunk_upload_handlers",
    "simple_history",
    "storages",
]

INSTALLED_APPS = DJANGO_APPS + OUR_APPS + THIRD_PARTY_APPS

CRISPY_ALLOWED_TEMPLATE_PACKS = ("bootstrap", "bootstrap3", "bootstrap4", "uni_form", "gds")
CRISPY_TEMPLATE_PACK = "gds"

# AWS
AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID", default=None)
AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY", default=None)
AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME", default=None)
AWS_ENDPOINT_URL = env.str("AWS_ENDPOINT_URL", default=None)
AWS_S3_ENDPOINT_URL = f"http://{AWS_ENDPOINT_URL}"
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_ENDPOINT_URL}"
AWS_LOCATION = "static/"
AWS_REGION = env.str("AWS_REGION", default="eu-west-2")

# We want to use HTTP for local development and HTTPS for production
AWS_S3_URL_PROTOCOL = env.str("AWS_S3_URL_PROTOCOL", default="https:")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
# where static files are collected after running collectstatic:

if env.bool("USE_S3_STATIC_FILES", default=True):
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    STATIC_URL = f"{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}"
else:
    STATIC_URL = "static/"
    STATIC_ROOT = ROOT_DIR / "static"
    STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(ROOT_DIR, "media")

FILE_UPLOAD_HANDLERS = (
    "django_chunk_upload_handlers.clam_av.ClamAVFileUploadHandler",
    "django_chunk_upload_handlers.s3.S3FileUploadHandler",
)  # Order is important

# File storage
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

CLAM_AV_USERNAME = env.str("CLAM_AV_USERNAME", default=None)
CLAM_AV_PASSWORD = env.str("CLAM_AV_PASSWORD", default=None)
CLAM_AV_DOMAIN = env.str("CLAM_AV_DOMAIN", default=None)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
]

ROOT_URLCONF = "config.urls"

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

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
_VCAP_SERVICES = env.json("VCAP_SERVICES", default={})

if "postgres" in _VCAP_SERVICES:
    DATABASES = {
        "default": {
            **dj_database_url.parse(
                _VCAP_SERVICES["postgres"][0]["credentials"]["uri"],
                engine="postgresql",
                conn_max_age=0,
            ),
            "ENGINE": "django.db.backends.postgresql",
        }
    }
else:
    default_database = env.db()
    DATABASES = {"default": default_database}

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

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# COMPANIES HOUSE API
COMPANIES_HOUSE_API_KEY = env.str("COMPANIES_HOUSE_API_KEY", default="")

# GOV NOTIFY
GOV_NOTIFY_API_KEY = env.str("GOV_NOTIFY_API_KEY")
EMAIL_VERIFY_CODE_TEMPLATE_ID = env.str("GOVUK_NOTIFY_TEMPLATE_EMAIL_VERIFICATION")
RESTRICT_SENDING = env.bool("RESTRICT_SENDING", default=True)  # if True, only send to whitelisted domains

# SENTRY
SENTRY_DSN = env.str("SENTRY_DSN", default="")
SENTRY_ENVIRONMENT = env.str("SENTRY_ENVIRONMENT", default="")
if SENTRY_DSN and SENTRY_ENVIRONMENT:
    sentry_sdk.init(
        dsn=env.str("SENTRY_DSN", default=""),
        environment=env.str("SENTRY_ENVIRONMENT", default=""),
        integrations=[DjangoIntegration()],
        traces_sample_rate=0,
    )
