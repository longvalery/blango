#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import platform



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blango.settings')
    print("platform.uname",platform.uname()) 
    ## DEV_MODE=(platform.system() =='Linux')
    #DEV_MODE=(platform.node() == 'salutecombine-stadiumbison')
    ##print(platform.release()[0:5])
    DEV_MODE=(platform.release()[0:5] == '5.4.0') # '5.4.0-1080-aws')  release='5.4.0-1078-aws'

    if DEV_MODE :
       os.environ.setdefault("DJANGO_CONFIGURATION", "Dev")
    else :
       os.environ.setdefault("DJANGO_CONFIGURATION", "Prod")    

    try:
        # from django.core.management import execute_from_command_line
        from configurations.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
