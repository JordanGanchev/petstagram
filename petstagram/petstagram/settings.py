from operator import truediv
from pathlib import Path

from django.conf.global_settings import MEDIA_ROOT

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-l6m4w+o*!jhna5!1)^%#vg9vl@e8j=1^f5tb+q&-8&4fy4o**e"

DEBUG = True

ALLOWED_HOSTS = [
    # 'localhost',
    # '127.0.0.1',
    # '192.168.x.x',
    # 'example.com',
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "petstagram.accounts",
    "petstagram.common",
    "petstagram.pets",
    "petstagram.photos",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "petstagram.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = "petstagram.wsgi.application"


DATABASES = {
    "sqlite3": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'petstagram',
        'USER': 'postgres',
        'PASSWORD': '123sql',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }

}

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



LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True



STATIC_URL = "static/"

STATICFILES_DIRS = (
    BASE_DIR / 'staticfiles',
)

MEDIA_ROOT = BASE_DIR / 'mediafiles'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# UserModel = get_user_model()
