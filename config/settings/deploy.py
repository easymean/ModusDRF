from .base import *  # NOQA

DEBUG = False

ALLOWED_HOSTS = ["www.modus.com"]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "read_default_file": os.path.join(SECRET_DIR, "mysql.cnf"),  # NOQA
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",  # strict mode 설정 추가
        },
    }
}

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [  # NOQA
    "rest_framework.renderers.JSONRenderer",
]
