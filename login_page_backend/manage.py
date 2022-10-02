#!/usr/bin/env python

# How to run this as a website:
# make your current directory C:\Users\...\incskill-website\login_page_backend
# Run the following command: py -3 manage.py runserver
# Copy and paste the link created in your terminal


# Django's command-line utility for administrative tasks.
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'login_page_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
