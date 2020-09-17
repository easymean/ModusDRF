import os, datetime
import my_settings


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SERCRET_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")


# secret
SECRET_KEY = my_settings.SECRET_KEY

ALLOWED_HOSTS = ["127.0.0.1", ".pythonanywhere.com", "localhost"]


# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS = [
    "classes.apps.ClassesConfig",
    "places.apps.PlacesConfig",
    "users.apps.UsersConfig",
    "common.apps.CommonConfig",
    "somms.apps.SommsConfig",
    "hosts.apps.HostsConfig",
    "placeReservations.apps.PlacereservationsConfig",
    "placeReviews.apps.PlacereviewsConfig",
    "qnas.apps.QnasConfig",
]

THIRD_PARTY_APPS = [
    "rest_framework",
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

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
        "DIRS": [TEMPLATE_DIR],
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

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"

# Auth

AUTH_USER_MODEL = "users.User"

# Django Rest Framework

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "config.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
}

JWT_AUTH_COOKIE = "cookies"
JWT_EXPIRATION_DELTA = datetime.timedelta(hours=1)

EMAIL_BACKEND = my_settings.EMAIL["EMAIL_BACKEND"]
EMAIL_USE_TLS = my_settings.EMAIL["EMAIL_USE_TLS"]
EMAIL_PORT = my_settings.EMAIL["EMAIL_PORT"]
EMAIL_HOST = my_settings.EMAIL["EMAIL_HOST"]
EMAIL_HOST_USER = my_settings.EMAIL["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = my_settings.EMAIL["EMAIL_HOST_PASSWORD"]
DEFAULT_FROM_MAIL = my_settings.EMAIL["DEFAULT_FROM_MAIL"]
