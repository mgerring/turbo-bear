import settings, sys, os

MIDDLEWARE_CLASSES = settings.MIDDLEWARE_CLASSES + ['debug_toolbar.middleware.DebugToolbarMiddleware']
INSTALLED_APPS = settings.INSTALLED_APPS + ['debug_toolbar']

INTERNAL_IPS = ('127.0.0.1',)
USE_ETAGS = True

STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': 'db/cache'
    }
}