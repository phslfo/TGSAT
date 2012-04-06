import os

# 'project' refers to the name of the module created with django-admin.py
ROOT_URLCONF = 'urls'
SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sites',
)

#ROOT_PATH = os.path.dirname(__file__)
#TEMPLATE_DIRS = (
#    # Put strings here, like "/home/html/django_templates" or
#    # "C:/www/django/templates".  Always use forward slashes, even on Windows.
#    # Don't forget to use absolute paths, not relative paths.
#    ROOT_PATH + '/templates',
#)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    
    #"E:/Workspace/capsdoc/src/project/templates"
    os.path.join(SETTINGS_PATH, 'templates')
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

# setup logger
#import logging
#PROJECT_DIR = os.path.dirname(__file__)
#logging.basicConfig(level=logging.DEBUG,
#     format='%(asctime)s %(levelname)s %(message)s',
#     filename=os.path.join(PROJECT_DIR, 'django.log'),
#     filemode='a+')