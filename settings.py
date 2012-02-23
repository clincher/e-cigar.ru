# -*- coding: utf-8 -*-
# Django settings for ecigar project.
import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'database.sqlite',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1

APPEND_SLASH = False

RATING_RANGE = 5

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
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'
TINYMCE_JS_URL = os.path.join(STATIC_ROOT, "tiny_mce/tiny_mce.js")
TINYMCE_JS_ROOT = os.path.join(MEDIA_ROOT, "tiny_mce")
# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
#ADMIN_MEDIA_PREFIX = '/static/admin/'
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
# Additional locations of static files

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'templates/static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'apps.myshop.context_processors.manufacturers',
    'apps.myshop.context_processors.cigarettes',
    'apps.myshop.context_processors.most_popular_product',
    'apps.myshop.context_processors.most_discount_product',
    'apps.myshop.context_processors.rating_range',
    'apps.myshop.context_processors.delivery_in_moscow_backend',
    'apps.feedback.context_processors.feedback_form'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

SHOP_SHIPPING_BACKENDS = [
#    'apps.myshop.shipping.backends.pickup.PickupShipping',
    'apps.myshop.shipping.backends.delivery_in_moscow.DeliveryInMoscowShipping',
]
SHOP_PAYMENT_BACKENDS = [
    'apps.myshop.payments.backends.pay_with_cash.PayWithCashBackend'
]
SHOP_CART_MODIFIERS = [
    'shop_simplevariations.cart_modifier.ProductOptionsModifier',
    'apps.myshop.modifiers.cigarette_quantity.CigaretteQuantityRebateModifier'
]

#dict of depend rebate from total cigarettes quantity
REBATE_PERCENTAGES = {3: 5}


SHOP_ADDRESS_MODEL = 'apps.myshop.address.models.Address'

INSTALLED_APPS = [
    # django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.flatpages',
    'django.contrib.staticfiles',
    # django-shop apps
    'sorl.thumbnail',
    'polymorphic',
    'shop',
    'shop_simplevariations',
    # useful 3rd party apps
    'south',
    'sitetree',
    'djangoratings',
    'tinymce',
    'captcha',

    # Our own apps
    'apps.common',
    'apps.myshop',
    'apps.myshop.address',
    'apps.articles',
    'apps.banners',
    'apps.callback',
    'apps.feedback',
]

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

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
DEBUG = True
from local_settings import *
TEMPLATE_DEBUG = DEBUG

if DEBUG:
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
    #    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )
    MIDDLEWARE_CLASSES = (('debug_toolbar.middleware.DebugToolbarMiddleware',)
                                                        + MIDDLEWARE_CLASSES)
    INTERNAL_IPS = ('127.0.0.1',)
    DEBUG_TOOLBAR_CONFIG = dict(
        INTERCEPT_REDIRECTS = False
    )
    INSTALLED_APPS += ['debug_toolbar', 'django_extensions']
    
    STATICFILES_DIRS += (os.path.join(PROJECT_DIR, 'media'),)
else:
    FILES_URL = 'http://files.e-cigar.ru'
    MEDIA_URL = FILES_URL + MEDIA_URL
#    STATIC_URL = FILES_URL + STATIC_URL
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),)