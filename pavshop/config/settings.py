"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from . import project_secrets


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kfb$#u9jo&gkpjai7i+l$y00gbu_-ro(sn)&3_@5f^fk4j!(ly'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INITIAL_APPS = [
    "jazzmin",
]

THIRD_PARTY_APPS = [
    "django_extensions",
    "werkzeug_debugger_runserver",
    "ckeditor",
    "phonenumber_field",
    "babel",
    'social_django',
]

MY_APPS = [
    "core.apps.CoreConfig",
    "account.apps.AccountConfig",
    "product.apps.ProductConfig",
    "blog.apps.BlogConfig",
]

INSTALLED_APPS = INITIAL_APPS + BASE_APPS + THIRD_PARTY_APPS + MY_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware'
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# # PostgreSQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'pavshop',
#         'USER': 'root',
#         'PASSWORD': 12345,
#         'HOST': 'localhost',
#         'PORT': 5432
#     }
# }


# Custom User model
AUTH_USER_MODEL = "account.User"


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Baku'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CKEditor configs
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        # 'height': 300,
        # 'width': '100%',
    },
}


# Jazzmin Settings
JAZZMIN_SETTINGS = {
    "site_title": "Pavshop Admin",
    "site_header": "Pavshop Admin",
    "site_brand": "Pavshop Admin Panel",
    "welcome_sign": "Welcome to Pavshop Admin panel",
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",

        # account APP
        "account.Country": "fas fa-globe",
        "account.City": "fas fa-city",
        "account.Address": "fas fa-map-marker-alt",
        "account.Position": "fas fa-briefcase",
        "account.User": "fas fa-user",

        # blog APP
        "blog.BlogCategory": "fas fa-folder",
        "blog.BlogTag": "fas fa-tag",
        "blog.Blog": "far fa-newspaper",
        "blog.BlogReview": "fas fa-comments",

        # core APP
        "core.Contact": "fas fa-envelope",
        "core.Newsletter": "fas fa-newspaper",

        # product APP
        "product.Color": "fas fa-palette",
        "product.Designer": "fas fa-pencil-ruler",
        "product.Brand": "fas fa-building",
        "product.Discount": "fas fa-percent",
        "product.ProductCategory": "fas fa-folder",
        "product.ProductTag": "fas fa-tag",
        "product.Product": "fas fa-cubes",
        "product.ProductVersion": "fas fa-cube",
        "product.ProductVersionImage": "fas fa-image",
        "product.ProductVersionReview": "fas fa-comments",
        "product.Wishlist": "fas fa-heart",
    },
}


# PasswordResetTokenGenerator token expiration time (6 hour)
PASSWORD_RESET_TIMEOUT = 6 * 60 * 60


# Account Activation
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'pavshop.project@gmail.com'
EMAIL_HOST_PASSWORD = 'vfvawfeqwoaaergj'
EMAIL_PORT = 587


# Social Login
AUTHENTICATION_BACKENDS = [
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_URL_NAMESPACE = 'social'
LOGIN_URL = 'login_view'
LOGIN_REDIRECT_URL = 'core:index_view'
LOGOUT_URL = 'logout_view'
SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'email',
]
# LOGOUT_REDIRECT_URL = 'login_view'

# Github OAuth2 key and secret configuration
SOCIAL_AUTH_GITHUB_KEY = project_secrets.github_key
SOCIAL_AUTH_GITHUB_SECRET = project_secrets.github_secret

# Google OAuth2 key and secret configuration
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = project_secrets.google_key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = project_secrets.google_secret

# Facebook OAuth2 key and secret configuration
SOCIAL_AUTH_FACEBOOK_KEY = project_secrets.facebook_key             # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = project_secrets.facebook_secret       # App Secret
