# Django-Logtailer
Fork from: https://github.com/fireantology/django-logtailer  
Original Author:  Mauro Rocco <mauro.rocco@toforge.com>


## Fixes
Integrate fixes from:
* Django 2 model-fix: https://github.com/dima-kov/django-logtailer/commit/14f2da106937f03067e6e5ae95bfa34648968e09
* Python 3.6 view-fix: https://github.com/cpankajr/django-logtailer/commit/931d4a19f69d692a8ea325a4a29275e4025d3d3a


## Extensions
Add an auto-registering for logfiles in the setting `LOGTAILER_REGISTER_LOGFILES`.  
Just add the following to your `settings.py`:
```
LOGTAILER_REGISTER_LOGFILES = {
    'Django-Log': LOGS_DIR.path('django.log'),
    'Schedule-Log': LOGS_DIR.path('scheduled_job.log')
}
```
Where `LOGS_DIR` is an `environ.Path()` pointing to your log-directory. You can you use any other path-building mechanism, it has to result in an absolute path to the log-file.    
The logfile-entries are only added to the LogFile-Model/Admin when they doesn't exist already with the same name (e.g. 'Django-Log')  


## Source
Author: Thomas Häny <dev@haeny.de>  
Version: 1.1.2  
Repo: https://github.com/thaeny-dev/django-logtailer  
Dependencies: Django (>=2)  
Requires: Python 3.6+  

##Changelog
1.1.2   move auto-register-code to apps.py, avoid running code during migrations, bugfixing  
1.1.1   Add auto-registering for LOGTAILER_REGISTER_LOGFILES    
1.1.0   Fork from fireantology/django-logtailer and integrate fixes (Django2-models, Python3.6-views)
