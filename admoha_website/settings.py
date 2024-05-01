from pathlib import Path
from django.core.management.utils import get_random_secret_key
import os
import sys
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

# # SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"


SECRET_KEY = 'django-insecure-c_r7@!mbotce@f^pv^4z%#3@(#5eayj#bufn216k&9$uoiv%kc'


ALLOWED_HOSTS = ["admoha.com",'www.admoha.com','.admoha.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
MY_APPS = [
    'blog',
    'ckeditor',
    'django.contrib.sites',
    'django.contrib.sitemaps',
]

INSTALLED_APPS += MY_APPS

SITE_ID = 1

CKEDITOR_CONFIGS = {
    'default':
        {
            'toolbar': 'full',
            'width': 'auto',
            'extraPlugins': ','.join([
                'codesnippet',
            ]),
        },
}
AUTHENTICATION_BACKENDS=[
    'django.contrib.auth.backends.ModelBackend',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'admoha_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.context_processors.display_user',
                'blog.context_processors.categories',
            ],
        },
    },
]

WSGI_APPLICATION = 'admoha_website.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.expanduser('~/db.sqlite3'),
    }
}




# if DEVELOPMENT_MODE is True:
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.sqlite3",
#             "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#         }
#     }
# elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
#     if os.getenv("DATABASE_URL", None) is None:
#         raise Exception("DATABASE_URL environment variable not defined")
#     DATABASES = {
#         "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
#     }
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE =  'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, imgs)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

MEDIA_ROOT= BASE_DIR / "media" 
MEDIA_URL="/media/"
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'iamadityacoder@gmail.com'
# EMAIL_HOST_PASSWORD = 'aditya=hero1'
# EMAIL_USE_TLS = True
