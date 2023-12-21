"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import sys
from contextlib import suppress
from datetime import timedelta
from pathlib import Path
from typing import cast

import decouple
import dj_database_url
import sentry_sdk
from decouple import Config, RepositoryEnv
from django.core.exceptions import PermissionDenied
from sentry_sdk.integrations.django import DjangoIntegration

BASE_DIR = Path(__file__).resolve().parent.parent
TESTING = (len(sys.argv) > 1 and sys.argv[1] == "test") or ("pytest" in sys.modules)

if TESTING:
    config = Config(
        RepositoryEnv(
            BASE_DIR
            / cast(str, decouple.config("TEST_DOT_ENV_FILE", default=".env.test"))
        )
    )
else:
    config = decouple.config


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
    except Exception:
        return config(name, cast=cast, default=default)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

SECRET_KEY = get_env_variable("SECRET_KEY")
DEBUG = get_env_variable("DEBUG", cast=bool)
ENVIRONMENT = get_env_variable("ENVIRONMENT", default="development")
CRON_ENABLED = get_env_variable("CRON_ENABLED", default=False, cast=bool)

LOGLEVEL = get_env_variable("LOGLEVEL", default="error").upper()

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        }
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": LOGLEVEL,
        },
    },
    "formatters": {
        "default": {
            # exact format is not important, this is the minimum information
            "format": "[%(asctime)s] %(name)-12s] %(levelname)-8s : %(message)s",
        },
    },
}

SENDINBLUE_API_KEY = get_env_variable("SENDINBLUE_API_KEY")
APPLICATION_DOMAIN_URL = get_env_variable("APPLICATION_DOMAIN_URL")

MAX_EMAIL_ATTACHED_FILES_SIZE = 10 * 1024 * 1024  # 10MB

if SENDINBLUE_API_KEY:
    ANYMAIL = {
        "SENDINBLUE_API_KEY": SENDINBLUE_API_KEY,
    }
    EMAIL_BACKEND = "anymail.backends.sendinblue.EmailBackend"
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DEFAULT_FROM_EMAIL = get_env_variable(
    "DEFAULT_FROM_EMAIL", default="ne-pas-repondre@apilos.beta.gouv.fr"
)

env_allowed_hosts = []
try:
    env_allowed_hosts = get_env_variable("ALLOWED_HOSTS").split(",")
except KeyError:
    pass

# Convert API
CONVERTAPI_SECRET = get_env_variable("CONVERTAPI_SECRET")
# INSEE API
INSEE_API_KEY = get_env_variable("INSEE_API_KEY")
INSEE_API_SECRET = get_env_variable("INSEE_API_SECRET")

ALLOWED_HOSTS = ["localhost"] + env_allowed_hosts


INSTALLED_APPS = [
    "admin.apps.ApilosAdminConfig",
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
    "siap.apps.SiapConfig",
    "users.apps.UsersConfig",
    "upload.apps.UploadConfig",
    "comments.apps.CommentsConfig",
    "rest_framework",
    "drf_spectacular",
    "django_cas_ng",
    "django.contrib.admindocs",
    "explorer",
    "ecoloweb",
    "anymail",
    "simple_history",
    "hijack",
    "hijack.contrib.admin",
    "django_celery_results",
]

if ENVIRONMENT == "development":
    INSTALLED_APPS.extend(
        [
            "django_extensions",
            "django_browser_reload",
            "debug_toolbar",
        ]
    )
    SHELL_PLUS_PRINT_SQL = get_env_variable(
        "SHELL_PLUS_PRINT_SQL", default=True, cast=bool
    )
    SHELL_PLUS = get_env_variable("SHELL_PLUS", default="ptpython")


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "csp.middleware.CSPMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
    "hijack.middleware.HijackUserMiddleware",
]


if not TESTING:
    MIDDLEWARE = MIDDLEWARE + [
        "whitenoise.middleware.WhiteNoiseMiddleware",
    ]

if "django_browser_reload" in INSTALLED_APPS:
    MIDDLEWARE.extend(
        [
            "django_browser_reload.middleware.BrowserReloadMiddleware",
        ]
    )
if "debug_toolbar" in INSTALLED_APPS:
    MIDDLEWARE.extend(
        [
            "debug_toolbar.middleware.DebugToolbarMiddleware",
        ]
    )
    with suppress(ModuleNotFoundError):
        from debug_toolbar.settings import CONFIG_DEFAULTS

        DEBUG_TOOLBAR_CONFIG = {
            "SHOW_TOOLBAR_CALLBACK": "operator.truth",
            "HIDE_IN_STACKTRACES": CONFIG_DEFAULTS["HIDE_IN_STACKTRACES"]
            + ("sentry_sdk",),
        }

ROOT_URLCONF = "core.urls"

HIJACK_PERMISSION_CHECK = "hijack.permissions.superusers_and_staff"

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
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

WSGI_APPLICATION = "core.wsgi.application"

try:
    # dj_database_url is used in scalingo environment to interpret the
    # connection configuration to the DB from a single URL with all path
    # and credentials
    DATABASE_URL = config("DATABASE_URL")
    default_settings = dj_database_url.parse(DATABASE_URL)
except decouple.UndefinedValueError:
    default_settings = {
        "ENGINE": "django.db.backends.postgresql",
        "USER": get_env_variable("DB_USER"),
        "NAME": get_env_variable("DB_NAME"),
        "HOST": get_env_variable("DB_HOST"),
        "PASSWORD": get_env_variable("DB_PASSWORD"),
        "PORT": get_env_variable("DB_PORT", default="5432"),
        "TEST": {
            "NAME": get_env_variable("DB_NAME") + "-test",
        },
        "ATOMIC_REQUESTS": True,
    }

# EXPLORER settings
# from https://django-sql-explorer.readthedocs.io/en/latest/install.html
# The readonly access is configured with fake access when DB_READONLY env
# variable is not set.
DB_READONLY = config("DB_READONLY")
readonly_settings = dj_database_url.parse(DB_READONLY)

DATABASES = {"default": default_settings, "readonly": readonly_settings}

if get_env_variable("ECOLO_DATABASE_URL") != "":
    DATABASES["ecoloweb"] = dj_database_url.parse(
        get_env_variable("ECOLO_DATABASE_URL")
    )

EXPLORER_CONNECTIONS = {"Default": "readonly"}
EXPLORER_DEFAULT_CONNECTION = "readonly"

CONN_HEALTH_CHECKS = True
CONN_MAX_AGE = None

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
STATICFILES_DIRS = [
    BASE_DIR / "static",
    ("dsfr", BASE_DIR / "node_modules" / "@gouvfr" / "dsfr" / "dist"),
    ("virtual-select", BASE_DIR / "node_modules" / "virtual-select-plugin" / "dist"),
    ("turbo", BASE_DIR / "node_modules" / "@hotwired" / "turbo" / "dist"),
]

# Why STAGING = FALSE ?
STAGING = False

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

AUTHENTICATION_BACKENDS = [
    "core.backends.EmailBackend",
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
AWS_ECOLOWEB_BUCKET_NAME = get_env_variable("AWS_ECOLOWEB_BUCKET_NAME")

if AWS_ACCESS_KEY_ID:  # pragma: no cover
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
# Crisp configuration: https://docs.crisp.chat/guides/others/whitelisting-our-systems/crisp-domain-names/
CSP_DEFAULT_SRC = "'none'"
CSP_SCRIPT_SRC = (
    "https://stats.data.gouv.fr/piwik.js",
    "'self'",
    "'sha256-zaYxlJmjbzgo2YczX5XHFlvamZUNy264d7XlOOUwMME='",
    "'sha256-928U3JmFf9xytJJBtEU5V1FVGcqsTfwaVnI2vmHmamA='",
    "'sha256-lkrKw/baCFdnI+tB9T+0yFMewpXSk9yct2ZbWEGPDhY='",
    # Convention > récapitilatif > manage type I and type II options
    "'sha256-J71e5kr85q2XGRl+qwOA/tpMsXmKDjeTnvlzBhBsz/0='",
    "'sha256-h7boyH6dI/JQnsm6Iw1sAtEbdb/+638kREPj4sfWmMs='",  # ???
    # Convention > Récapitulatif > Comment type1and2
    "'sha256-7uHmVaAHWxl0RElSoWED7kK+9kRSQ+E6SQ3aBK1prkU='",
    # Swagger UI
    "https://cdn.jsdelivr.net/npm/swagger-ui-dist@latest/swagger-ui-bundle.js",
    "https://cdn.jsdelivr.net/npm/swagger-ui-dist@latest/swagger-ui-standalone-preset.js",
    # Crisp
    "https://client.crisp.chat",
    "https://settings.crisp.chat",
)
CSP_IMG_SRC = (
    "'self'",
    "data:",
    "https://cdn.jsdelivr.net/npm/swagger-ui-dist@latest/favicon-32x32.png",
    # Crisp
    "https://client.crisp.chat",
    "https://image.crisp.chat",
    "https://storage.crisp.chat",
)
CSP_OBJECT_SRC = "'none'"

X_FRAME_OPTIONS = "SAMEORIGIN"
CSP_FRAME_SRC = (
    "'self'",
    "https://www.dailymotion.com/embed/video/x8fkp4y",
    "https://www.dailymotion.com/embed/video/x8frr91",
    # Crisp
    "https://game.crisp.chat",
    # Metabase
    "https://metabase.apilos.beta.gouv.fr/public/dashboard/b91cd727-95e2-44c7-b8ae-0cf4a235abfb",
)

CSP_MEDIA_SRC = (
    # Crisp
    "https://client.crisp.chat"
)
CSP_FONT_SRC = (
    "'self'",
    "data:",
    # Crisp
    "https://client.crisp.chat",
)
CSP_CONNECT_SRC = (
    "'self'",
    "https://stats.data.gouv.fr/piwik.php",
    # Crisp
    "https://client.crisp.chat",
    "https://storage.crisp.chat",
    "wss://client.relay.crisp.chat",
    "wss://stream.relay.crisp.chat",
)
CSP_STYLE_SRC = (
    "'self'",
    "https://code.highcharts.com/css/highcharts.css",
    "https://cdn.jsdelivr.net/npm/swagger-ui-dist@latest/swagger-ui.css",
    "'unsafe-inline'",
    # Crisp
    "https://client.crisp.chat",
)
CSP_MANIFEST_SRC = "'self'"
CSP_INCLUDE_NONCE_IN = [
    "script-src",
]
CSP_EXCLUDE_URL_PREFIXES = ("/explorer",)

# Disable whitenoise for test
STATICFILES_STORAGE = (
    "django.contrib.staticfiles.storage.StaticFilesStorage"
    if TESTING
    else "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "siap.siap_authentication.SIAPJWTAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ALGORITHM": get_env_variable("JWT_ALGORITHM", default="HS256"),
    "SIGNING_KEY": get_env_variable("JWT_SIGN_KEY", default=None),
    "USER_ID_CLAIM": "user-login",
    "USER_ID_FIELD": "cerbere_login",
}

SIAP_CLIENT_JWT_SIGN_KEY = get_env_variable("SIAP_CLIENT_JWT_SIGN_KEY", default=None)
SIAP_CLIENT_ALGORITHM = get_env_variable("SIAP_CLIENT_ALGORITHM", default="HS256")
SIAP_CLIENT_HOST = get_env_variable("SIAP_CLIENT_HOST", default=None)
SIAP_CLIENT_PATH = get_env_variable("SIAP_CLIENT_PATH", default=None)

SPECTACULAR_SETTINGS = {
    "TITLE": "API APiLos",
    "DESCRIPTION": "Documentation de l'API APiLos consommée par SIAP",
    "VERSION": "0.0.1",
    "SERVE_INCLUDE_SCHEMA": False,
    "TAGS": [{"name": "config-resource", "description": "Config Resource"}],
    "DISABLE_ERRORS_AND_WARNINGS": False,
    # OTHER SETTINGS
}

APILOS_PAGINATION_PER_PAGE = 20
APILOS_MAX_DROPDOWN_COUNT = get_env_variable(
    "APILOS_MAX_DROPDOWN_COUNT", cast=int, default=20
)

# to do : deprecate drf_yasg
SWAGGER_SETTINGS = {
    "DEFAULT_AUTO_SCHEMA_CLASS": "api.auto_schema.ReadWriteAutoSchema",
}

CERBERE_AUTH = get_env_variable("CERBERE_AUTH")
USE_MOCKED_SIAP_CLIENT = get_env_variable("USE_MOCKED_SIAP_CLIENT", cast=bool)
NO_SIAP_MENU = get_env_variable("NO_SIAP_MENU", cast=bool)

if CERBERE_AUTH:
    MIDDLEWARE = MIDDLEWARE + [
        "django_cas_ng.middleware.CASMiddleware",
        "siap.custom_middleware.CerbereSessionMiddleware",
    ]

    AUTHENTICATION_BACKENDS = AUTHENTICATION_BACKENDS + [
        "core.backends.CerbereCASBackend",
    ]  # custom backend CAS

    # CAS config
    CAS_SERVER_URL = CERBERE_AUTH
    CAS_VERSION = "CAS_2_SAML_1_0"
    CAS_USERNAME_ATTRIBUTE = "username"
    CAS_APPLY_ATTRIBUTES_TO_USER = True
    CAS_RENAME_ATTRIBUTES = {
        "UTILISATEUR.ID": "username",
        "UTILISATEUR.LOGIN": "cerbere_login",
        "UTILISATEUR.NOM": "last_name",
        "UTILISATEUR.PRENOM": "first_name",
        "UTILISATEUR.MEL": "email",
    }
    CAS_LOGIN_MSG = None
    CAS_LOGGED_MSG = None

    LOGIN_URL = "/accounts/cerbere-login"

# Django defender (doc https://github.com/jazzband/django-defender#customizing-django-defender)
REDIS_URL = get_env_variable("REDIS_URL")
if REDIS_URL and not CERBERE_AUTH and not TESTING:
    INSTALLED_APPS += ["defender"]
    MIDDLEWARE += ["defender.middleware.FailedLoginMiddleware"]

    DEFENDER_LOGIN_FAILURE_LIMIT = 5
    DEFENDER_BEHIND_REVERSE_PROXY = get_env_variable(
        "DEFENDER_BEHIND_REVERSE_PROXY", cast=bool, default=False
    )
    DEFENDER_REDIS_URL = REDIS_URL
    DEFENDER_COOLOFF_TIME = 6 * 60 * 60


# Sentry

SENTRY_URL = get_env_variable("SENTRY_URL")

if SENTRY_URL:  # pragma: no cover
    # opened issue on Sentry package : https://github.com/getsentry/sentry-python/issues/1081
    # it should be solved in a further release
    sentry_sdk.init(
        dsn=SENTRY_URL,
        integrations=[DjangoIntegration()],
        environment=ENVIRONMENT,
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=0.05,
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
        ignore_errors=[PermissionDenied],
    )

# Crisp
CRISP_WEBSITE_ID = get_env_variable("CRISP_WEBSITE_ID")

# Celery (see https://docs.celeryq.dev/en/stable/userguide/configuration.html#configuration)
CELERY_TIMEZONE = "Europe/Paris"
# CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 60 * 60
CELERY_BROKER_URL = get_env_variable("REDIS_URL")
CELERY_RESULT_BACKEND = "django-db"
CELERY_SEND_EVENTS = True
CELERY_ACKS_LATE = True
CELERY_WORKER_MAX_TASKS_PER_CHILD = 5000

# limit reach when an operation has 167 logements
DATA_UPLOAD_MAX_NUMBER_FIELDS = int(
    get_env_variable("DATA_UPLOAD_MAX_NUMBER_FIELDS", default="100000")
)

# ClamAV configuration
CLAMAV_SERVICE_URL = get_env_variable("CLAMAV_SERVICE_URL", default=None)
CLAMAV_SERVICE_USER = get_env_variable("CLAMAV_SERVICE_USER")
CLAMAV_SERVICE_PASSWORD = get_env_variable("CLAMAV_SERVICE_PASSWORD")
