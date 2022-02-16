"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

from decouple import config
import dj_database_url

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


def get_env_variable(name, cast=str, default=""):
    try:
        if cast == bool:
            return os.environ[name].lower() in [
                "true",
                "1",
                "t",
                "y",
                "yes",
                "yeah",
                "yup",
                "certainly",
                "uh-huh",
            ]
        return cast(os.environ[name])
    # pylint: disable=W0702, bare-except
    except:
        return config(name, cast=cast, default=default)


BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

SECRET_KEY = get_env_variable("SECRET_KEY")
DEBUG = get_env_variable("DEBUG", cast=bool)
ENVIRONMENT = get_env_variable("ENVIRONMENT", default="development")

# LOGGING = {
#     'version': 1,
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         }
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#         }
#     },
#     'loggers': {
#         'django.db.backends': {
#             'level': 'DEBUG',
#             'handlers': ['console'],
#         }
#     }
# }

mailjet_api_key = get_env_variable("MAILJET_API_KEY")
mailjet_api_secret = get_env_variable("MAILJET_API_SECRET")

DEFAULT_FROM_EMAIL = "contact@apilos.beta.gouv.fr"

if mailjet_api_key != "":
    EMAIL_BACKEND = "django_mailjet.backends.MailjetBackend"
    MAILJET_API_KEY = mailjet_api_key
    MAILJET_API_SECRET = mailjet_api_secret
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

env_allowed_hosts = []
try:
    env_allowed_hosts = get_env_variable("ALLOWED_HOSTS").split(",")
except KeyError:
    pass

CONVERTAPI_SECRET = get_env_variable("CONVERTAPI_SECRET")

ALLOWED_HOSTS = ["localhost"] + env_allowed_hosts

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "bailleurs.apps.BailleursConfig",
    "conventions.apps.ConventionsConfig",
    "instructeurs.apps.InstructeursConfig",
    "programmes.apps.ProgrammesConfig",
    "apilos_settings.apps.ApilosSettingsConfig",
    "stats.apps.StatsConfig",
    "users.apps.UsersConfig",
    "upload.apps.UploadConfig",
    "comments.apps.CommentsConfig",
    "rest_framework",
    "drf_yasg",
    "django_filters",
    "django_cas_ng",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "csp.middleware.CSPMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": False,
            "context_processors": [
                "core.context_processor.get_environment",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


try:
    database_url = os.environ["DATABASE_URL"]
    default_settings = dj_database_url.config()
except KeyError:
    default_settings = {
        "ENGINE": "django.db.backends.postgresql",
        "USER": config("DB_USER"),
        "NAME": config("DB_NAME"),
        "HOST": config("DB_HOST"),
        "PASSWORD": config("DB_PASSWORD"),
        "PORT": config("DB_PORT", default="5432"),
        "TEST": {
            "NAME": config("DB_NAME") + "-test",
        },
        "ATOMIC_REQUESTS": True,
    }

DATABASES = {"default": default_settings}

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

LANGUAGE_CODE = "fr"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Static files
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, "staticfiles"))
STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# Why STAGING = FALSE ?
STAGING = False

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"
AUTHENTICATION_BACKENDS = [
    "users.backends.EmailBackend",
]

# Redirect to home URL after login
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Object storage with Scaleway
AWS_ACCESS_KEY_ID = get_env_variable("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = get_env_variable("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = get_env_variable("AWS_STORAGE_BUCKET_NAME")
AWS_DEFAULT_ACL = get_env_variable("AWS_DEFAULT_ACL")
AWS_S3_REGION_NAME = get_env_variable("AWS_S3_REGION_NAME")
AWS_S3_ENDPOINT_URL = get_env_variable("AWS_S3_ENDPOINT_URL")

if AWS_ACCESS_KEY_ID:
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
else:
    DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 6 * 60 * 60

# Security settings
if ENVIRONMENT != "development":
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "Strict"
SESSION_COOKIE_SAMESITE = "Lax"

# https://django-csp.readthedocs.io/en/latest/configuration.html
CSP_DEFAULT_SRC = "'none'"
CSP_SCRIPT_SRC = ("https://stats.data.gouv.fr/piwik.js", "'self'")
CSP_IMG_SRC = ("'self'", "data:")
CSP_OBJECT_SRC = "'none'"
CSP_FONT_SRC = "'self'", "data:"
CSP_CONNECT_SRC = ("'self'", "https://stats.data.gouv.fr/piwik.php")
CSP_STYLE_SRC = ("'self'", "https://code.highcharts.com/css/highcharts.css")
CSP_MANIFEST_SRC = "'self'"
CSP_INCLUDE_NONCE_IN = [
    "script-src",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
}
APILOS_PAGINATION_PER_PAGE = 20

SWAGGER_SETTINGS = {
    "DEFAULT_AUTO_SCHEMA_CLASS": "api.auto_schema.ReadWriteAutoSchema",
}

CERBERE_AUTH = get_env_variable("CERBERE_AUTH", cast=bool)

if CERBERE_AUTH:
    MIDDLEWARE = MIDDLEWARE + [
        "django_cas_ng.middleware.CASMiddleware",
    ]

    AUTHENTICATION_BACKENDS = [
        "users.backends.EmailBackend",
        "core.backends.CerbereCASBackend",
    ]  # custom backend CAS

    # CAS config
    CAS_SERVER_URL = (
        "https://authentification.din.developpement-durable.gouv.fr/cas/public"
    )
    CAS_VERSION = "CAS_2_SAML_1_0"
    CAS_USERNAME_ATTRIBUTE = "username"
    CAS_APPLY_ATTRIBUTES_TO_USER = True
    CAS_RENAME_ATTRIBUTES = {
        "UTILISATEUR.ID": "username",
        "UTILISATEUR.NOM": "last_name",
        "UTILISATEUR.PRENOM": "first_name",
        "UTILISATEUR.MEL": "email",
    }  # ,'UTILISATEUR.UNITE':'unite'

    LOGIN_URL = "/accounts/cerbere-login"

SENTRY_URL = get_env_variable("SENTRY_URL")

if SENTRY_URL:
    # opened issue on Sentry package : https://github.com/getsentry/sentry-python/issues/1081
    # it should be solved in a further release
    # pylint: disable=E0110
    sentry_sdk.init(
        dsn=SENTRY_URL,
        integrations=[DjangoIntegration()],
        environment=ENVIRONMENT,
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
    )
