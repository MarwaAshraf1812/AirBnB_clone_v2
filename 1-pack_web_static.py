#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive
from the contents of the web_static folder.
"""

from fabric.api import *
from datetime import datetime
import os


@task
def do_pack():
    """
    Generates a .tgz archive
    from the contents of the web_static folder.
    """

    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_path))
    f_size = os.path.getsize(archived_path)
    f_str = 'web_static packed: versions/web_static_{}.tgz -> {}Bytes'
    file_str = f_str.format(date, f_size)
    print(file_str)
    if t_gzip_archive.succeeded:
        return archived_path
    else:
        return None
