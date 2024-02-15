#!/usr/bin/python3
"""
Clean all archives based on the number of
arguements passed
"""

from fabric.api import *
from fabric.context_managers import cd, lcd
import os
from datetime import datetime


env.hosts = ["18.209.224.234", "52.23.213.75"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


@task
def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc."""

    number = int(number)
    if number == 0:
        number = 2
    else:
        number += 1

    with lcd('versions'):
        local('ls -1t | tail -n +{} | xargs -I {{}} rm -f {{}}'.format(number))
    with cd('/data/web_static/releases'):
        run('ls -t | tail -n +{} | xargs rm -rf'.format(number))
