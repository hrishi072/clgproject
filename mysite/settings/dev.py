from .common import *

# database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'social',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}"""

# email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# django-cors-headers settings
CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
)