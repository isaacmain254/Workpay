"""
Django settings for work_pay project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from django.contrib.messages import constants as messages
# Import dj-database-url at the beginning of the file.
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0at0nlz&q@g_i22zx4rwxml($hwrb58w8=ub!y2mw#oz5nozr='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['workPay.com', 'localhost', '127.0.0.1']
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]


# Application definition

INSTALLED_APPS = [
    "daphne",
    # my apps
    'marketplace',
    'account',
    'chat',


    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party apps
    "crispy_forms",
    "crispy_bootstrap5",
    "phonenumber_field",
    "debug_toolbar",
    'social_django',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'work_pay.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                # 'social_django.context_processors.login_redirect'
            ],
        },
    },
]

WSGI_APPLICATION = 'work_pay.wsgi.application'
# ASGI_APPLICATION = 'work_pay.asgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# Replace the SQLite DATABASES configuration with PostgreSQL:
DATABASES = {
    'default': dj_database_url.config(default='postgresql://client:maina254@localhost:5432/work_pay',  conn_max_age=600)}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
# Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication URL's configurations
LOGIN_REDIRECT_URL = 'login-success'

# Social auth redirect
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'login-success'

LOGIN_URL = 'login'

LOGOUT_URL = 'login'

# crispy-form config
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# email server configurations
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'elliotlinkon@gmail.com'
EMAIL_HOST_PASSWORD = 'lmyj tnhn kftq dkcs'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# media file configurations
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Phone Number Config
PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_REGION = "KE"

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"
# connecting bootstrap alert to messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# channels
ASGI_APPLICATION = 'work_pay.asgi.application'

# channel layer
CHANNEL_LAYERS = {
    "default": {
        # development only
        "BACKEND": "channels.layers.InMemoryChannelLayer",
        # production
        # "CONFIG": {
        #     "hosts": [("127.0.0.1", 6379)],
        # },
    },
}

# Google client ID
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '662747768788-2a16iep6g8g4bo9hta0euc5rpbrfn83h.apps.googleusercontent.com'
# Google client secret
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

# AUTHENTICATION BACKEND
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',

)

SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['role']

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'account.authentication.create_profile',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)
