# -*- coding: utf-8 -*-
# Django settings for openshift project.
import imp, os


# a setting to determine whether we are running on OpenShift
ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
if ON_OPENSHIFT:
    DEBUG = bool(os.environ.get('DEBUG', True))
    if DEBUG:
        print("WARNING: The DEBUG environment is set to True.")
else:
    DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

if ON_OPENSHIFT:
    # os.environ['OPENSHIFT_MYSQL_DB_*'] variables can be used with databases created
    # with rhc cartridge add (see /README in this git repo)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': '20thst',  # Or path to database file if using sqlite3.
            'USER': os.environ['OPENSHIFT_MYSQL_DB_USERNAME'],                      # Not used with sqlite3.
            'PASSWORD': os.environ['OPENSHIFT_MYSQL_DB_PASSWORD'],                  # Not used with sqlite3.
            'HOST': os.environ['OPENSHIFT_MYSQL_DB_HOST'],                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': os.environ['OPENSHIFT_MYSQL_DB_PORT'],                      # Set to empty string for default. Not used with sqlite3.
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'churchofchrist',  # Or path to database file if using sqlite3.
            'USER': 'root',                      # Not used with sqlite3.
            'PASSWORD': 'abc',                  # Not used with sqlite3.
            'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
        }
    }

CKEDITOR_UPLOAD_PATH = os.path.join(PROJECT_DIR, 'media/ckeditor/uploads')

LOGIN_URL = "/dashboard/dashboard_login"
LOGOUT_URL = "/dashboard/dashboard_logout"

# bible api configs
BIBLE_API_KEY="go2h8Hgrmbo6MJ5kbcFYTgYV3yCJEnFPgJSqjXWn"
BIBLE_API_ENDPOINT="https://bibles.org/v2"
BIBLE_API_VERSION="eng-KJVA"

#mailgun configs
MAIL_API_KEY="key-7ujhr-3mmt46gdq5b2a-m875olayixi1"
MAIL_API_ENDPOINT="https://api.mailgun.net/v2/20thst-churchofchrist.rhcloud.com/messages"
MAIL_CHURCH_DEFAULT_MAIL="20thstchurchofchrist@gmail.com"


FB_DEF_URL="https://www.facebook.com"

ALW_FILE_SIZE = (1*1024*1024) / 4

CKEDITOR_CONFIGS = {
    'default': {
        'width': "auto",
    },
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_DIR, '..', 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'staticfiles'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make a dictionary of default keys
default_keys = { 'SECRET_KEY': 'vm4rl5*ymb@2&d_(gc$gb-^twq9w(u69hi--%$5xrh!xk(t%hw' }

# Replace default keys with dynamic values if we are in OpenShift
use_keys = default_keys
if ON_OPENSHIFT:
    imp.find_module('openshiftlibs')
    import openshiftlibs
    use_keys = openshiftlibs.openshift_secure(default_keys)

# Make this unique, and don't share it with anybody.
SECRET_KEY = use_keys['SECRET_KEY']

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'openshift.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates'),
)


SUIT_CONFIG = {
    'ADMIN_NAME': '20th st. Church of Christ v1.0.1',
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,
    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-user',
    }
}

PAYPAL_RECEIVER_EMAIL = "neumerance-facilitator_api1.live.com"

MERCHANT_TEST_MODE = True    # Toggle for live transactions
MERCHANT_SETTINGS = {
    "pay_pal": {
        "WPP_USER" : "neumerance-facilitator_api1.live.com",
        "WPP_PASSWORD" : "1380877319",
        "WPP_SIGNATURE" : "ABdYc5g3.R75JP31XLvvpK7cuZQNAgqmRGJuvwXwabjnTLqscXXtIGiV"
    }
}

# Since merchant relies on django-paypal
# you have to additionally provide the
# below attributes
PAYPAL_TEST = MERCHANT_TEST_MODE
PAYPAL_WPP_USER = MERCHANT_SETTINGS["pay_pal"]["WPP_USER"]
PAYPAL_WPP_PASSWORD = MERCHANT_SETTINGS["pay_pal"]["WPP_PASSWORD"]
PAYPAL_WPP_SIGNATURE = MERCHANT_SETTINGS["pay_pal"]["WPP_SIGNATURE"]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'paypal.standard',
    'paypal.pro',
    'billing',
    'imagekit',
    'ckeditor',
    'south',
    'django_gravatar',
    'django.contrib.humanize',
    'endless_pagination',
    'suit',
    'django.contrib.admin',
    'django_tables2',
    'slider',
    'comment',
    'event',
    'ebible',
    'about',
    'contact',
    'news',
    'donate',
    'dashboard',
    'churchmember',
    'service',
    'gallery',
    'activetoken',
    'mailgun',
    'fellowship',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django_cleanup',
    'widget_tweaks',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
