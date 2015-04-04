#!/usr/bin/env python
import os
import sys

#psycopg2 were not in sys path
sys.path.append("/usr/local/lib/python2.7/dist-packages")


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agence.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
