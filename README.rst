ga_app - App portal for geoanalytics
####################################

Introduction
============

This application contains some necessary hacks and simiar stuff for Geoanalytics as a whole.  Most 
everything here could be enabled in a specific app, but since GA consists of many modules, many
of which have common assumptions about system setup, this app exists for that.  It will also 
eventually become the portal app.  If you are running any GA apps, you should install this app, as
any or all of them may require it in the future.  As of right now, the only app that requires it is
ga_bigboard, but more will follow

Special instructions
====================

One thing that ga_app does for you is magic logging, creating app-by-app logs and importing regularly
scheduled Celery tasks on an app by app basis.  To achieve this, create an :file:`app_settings` file
in your django app, and add a LOGGING attribute to the module like this::

   APP_LOGGING = {
       'ga_bigboard.views' : {
            'handlers': ['ga_bigboard'],
            'level': 'INFO',
            'propagate': True,
        }
   }

where the handler is simply the app label in INSTALLED_APPS.  Then at the end of your project's main
settings.py file, add the following lines::

   LOGGING_BASE_DIR = '<base directory for all your logs>'
   from ga_app import utils
   utils.append_app_settings(globals())

this trick means that you **must** not import django.conf.settings in your app_settings file. 
