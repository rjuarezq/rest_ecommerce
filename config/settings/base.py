from environ import Env, Path

ROOT_DIR = Path(__file__) - 3

env = Env(
    SECRET_KEY=(str, "DJANGO_SECRET_KEY"),
    DEBUG=(bool, False),
    CELERY_USER=(str, "guest"),
    CELERY_PASSWORD=(str, "guest"),
    CELERY_HOST=(str, "localhost"),
    CELERY_PORT=(int, 5672),
    CELERY_DATABASE=(str, "celery"),
    CELERY_BROKER_FAKE=(bool, False),
)

# GENERAL
# ------------------------------------------------------------------------------

# Take environment variables from .env file
env.read_env(ROOT_DIR(".env"))

# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

# Application definition

# Default apps
BASE_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework.authtoken",
]

LOCAL_APPS = [
    "product_app",
    "user_profile",
]

THIRD_APPS = [
    "rest_framework",
    "drf_yasg",
]

INSTALLED_APPS = BASE_APPS + THIRD_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
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


PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# specify the custom model as the default user model
# https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#authentication-backends:~:text=Finally%2C%20specify%20the,%27customauth.MyUser%27
AUTH_USER_MODEL = "user_profile.UserProfile"

# TIME TO EXPIRES A TOKEN
# https://stackoverflow.com/questions/14567586/how-to-set-token-expiration-time-in-django-rest-framework
TOKEN_EXPIRED_AFTER_SECONDS = 900  # 15 minutes

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "es-pe"

TIME_ZONE = "America/Lima"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# django-rest-framework
AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)
# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING_STREAMHANDLER = "logging.StreamHandler"

# CELERY
# ------------------------------------------------------------------------------
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#configuration
CELERY_USER = env("CELERY_USER")
CELERY_PASSWORD = env("CELERY_PASSWORD")
CELERY_HOST = env("CELERY_HOST")
CELERY_PORT = env("CELERY_PORT")
CELERY_DATABASE = env("CELERY_DATABASE")
CELERY_BROKER_URL = (
    f"pyamqp://{CELERY_USER}:{CELERY_PASSWORD}@{CELERY_HOST}:{CELERY_PORT}/{CELERY_DATABASE}"
)

# CELERY - EXTRA OPTIONS
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#configuration
CELERY_WORKER_SEND_TASK_EVENTS = True
CELERY_TASK_SEND_SENT_EVENT = True
