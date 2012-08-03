import importlib
import os

def append_app_settings(settings):
    for app in settings['INSTALLED_APPS']:
        settings['LOGGING']['handlers'][app] = {
            'level' : 'INFO' if not settings['DEBUG'] else 'DEBUG',
            'class' : 'logging.FileHandler',
            'formatter' : 'simple',
            'filename' : os.path.join(settings['LOGGING_BASE_DIR'], "{app}.log".format(app=app))
        }

        try:
            app_settings = importlib.import_module(app + '.app_settings')

            # add app specific loggers
            if hasattr(app_settings, "APP_LOGGING"):
                for name, logger in app_settings.APP_LOGGING.items():
                    settings['LOGGING']['loggers'][name] = logger

            # add app specific regular tasks
            if hasattr(app_settings, "APP_CELERYBEAT_SCHEDULE"):
                for name, task in app_settings.APP_CELERYBEAT_SCHEDULE.items():
                    settings['CELERYBEAT_SCHEDULE'][name] = task
        except ImportError:
            pass

