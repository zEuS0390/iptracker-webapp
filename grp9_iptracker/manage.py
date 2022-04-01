#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

"""
### Team Members:
- Aras, Juanito
- Baltazar, Zeus James
- Crebello, Cynna Mae
- Moreno, Wenzel

### Major Requirements:
- Git (Local Version Control)
- GitHub (Remote Version Control)
- Python (Programming Language)
- Pipenv (Packaging Tool with Virtual Environment)
- Django (Python Web Framework)
- HTML/CSS/JS (Web Page Fundamentals)
- Bootstrap (CSS Framework)

### Honor Pledge
~ "We affirm that we will not give or receive 
~ any unauthorized help on this activity, and 
~ that all work will be our own. We will never 
~ give this material to anyone without our consent."
"""

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grp9_iptracker.settings')
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
