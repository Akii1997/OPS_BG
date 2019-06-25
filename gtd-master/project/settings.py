# Django settings for gtd project.
import os
from django.contrib.messages import constants as message_constants


DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'lmrffsgfhrilklg-za7#57vi!zr)ps8)2anyona25###dl)s-#s=7=vn_'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Calcutta'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

LOGIN_URL = "/login"
LOGIN_REDIRECT_URL = 'home'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'
LOGIN_REDIRECT_URL = 'todo:lists'
LOGOUT_REDIRECT_URL = '/'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SECURITY_WARN_AFTER = 5
SESSION_SECURITY_EXPIRE_AFTER = 12

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'project.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'todo',
    'django_extensions',
    'project.apps.ProjectConfig',
)

# Static files and uploads

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'project', 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Uploaded media

# Without this, uploaded files > 4MB end up with perm 0600, unreadable by web server process
FILE_UPLOAD_PERMISSIONS = 0o644

# ######################
# Override in local.py :
# ######################

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'project', 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # Your stuff: custom template context processors go here
            ],
        },
    },
]


# Override CSS class for the ERROR tag level to match Bootstrap class name
MESSAGE_TAGS = {message_constants.ERROR: "danger"}

# Override in local.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'akash.kumar5@oyorooms.com'
EMAIL_HOST_PASSWORD = 'AkasHKumar@1'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'akash.kumar5@oyorooms.com'

# Todo-specific settings
TODO_STAFF_ONLY = False
TODO_DEFAULT_LIST_ID = None
TODO_DEFAULT_ASSIGNEE = None
TODO_PUBLIC_SUBMIT_REDIRECT = '/'
TODO_ALLOW_FILE_ATTACHMENTS = True
TODO_LIMIT_FILE_ATTACHMENTS = [".jpg", ".gif", ".png", ".csv", ".pdf"]

# TODO-specific settings
TODO_DEFAULT_LIST_SLUG = 'tickets'
ADMINS = (
    ('Akash', 'akash.kumar5@oyorooms.com'),
)
MANAGERS = ADMINS
