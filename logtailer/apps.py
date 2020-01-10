import sys
from django.apps import AppConfig
from django.conf import settings
from django.db.utils import ProgrammingError


class LogtailerAppConfig(AppConfig):
    name = 'logtailer'

    def ready(self):
        from logtailer.models import LogFile

        if not ('makemigrations' in sys.argv or 'migrate' in sys.argv):
            try:
                # auto-register LogFiles from LOGTAILER_REGISTER_LOGFILES-setting if exists
                register_logfiles = settings.LOGTAILER_REGISTER_LOGFILES \
                    if hasattr(settings, 'LOGTAILER_REGISTER_LOGFILES') else []
                for (name, path) in register_logfiles.items():
                    LogFile.objects.get_or_create(name=name, defaults={'path': path})
            except ProgrammingError as e:
                print('django-logtailer: Error in auto-registering the LOGTAILER_REGISTER_LOGFILES,\n' +
                      'maybe you should run the migration first...\n' + str(e),
                      file=sys.stderr)