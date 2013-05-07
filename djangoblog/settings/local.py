from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts

# DISQUS_API_KEY = '4QPXB0KLZpJSW58asYblShy92ANAuogEYpAYzfOPr7dcYRY1cuizkl1dSouCzH1v'
# DISQUS_WEBSITE_SHORTNAME = 'ashier.com'

ALLOWED_HOSTS = ['*']

# Make this unique, and don't share it with anybody.
SECRET_KEY = '00d2ppwoqyn1m4!@!cbhnf4x%ovttuwkgzv9k4vlk(xy^xev%&'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'djangoblog',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',                      # Set to empty string for default.
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    #'django.contrib.admindocs',
    # 'disqus',
    'tinymce',
    'south',
    'autoslug',
    'tastypie',
    'model_utils',
    'blog',
    'api_v1',
)
