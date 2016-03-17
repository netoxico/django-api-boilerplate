#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    environment = os.environ.get('PROJECT_ENV', 'development')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{project_name}}.settings.%s" % environment)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
