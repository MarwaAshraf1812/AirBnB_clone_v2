#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive
from the contents of the web_static folder of
"""

from fabric.api import *
from datetime import datetime
import os

@task
def do_pack():
    """
    generates a .tgz archive
    from the contents of the web_static folder
    """

    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_path))
    f_size = os.path.getsize(archived_path)
    f_str = ' versions/web_static_{}.tgz -> {}Bytes'.format(archived_path,f_size)
    print(f_str)
    if t_gzip_archive.succeeded:
        return archived_path
    else:
        return None
