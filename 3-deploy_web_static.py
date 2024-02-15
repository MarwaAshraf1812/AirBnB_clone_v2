#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""


from fabric.api import *
from datetime import datetime
import os
from fabric.api import put, run, env
from os.path import exists
env.hosts = ["18.209.224.234", "52.23.213.75"]


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

@task
def do_deploy(archive_path):
    """
    deployes web static 1
    """
    if exists(archive_path):
        f_name = archive_path.split("/")[-1]
        archive_ext = f_name.split(".")[0]
        r_release = "/data/web_static/releases"
        try:
            put(archive_path, '/tmp/')
            run('sudo mkdir -p {}/{}/'.format(r_release, archive_ext))
            run('sudo tar -xzf /tmp/{} -C {}/{}/'.format(f_name,
                                                         r_release,
                                                         archive_ext))
            run("sudo mv {}/{}/web_static/* {}/{}/".format(r_release,
                                                           archive_ext,
                                                           r_release,
                                                           archive_ext))
            run("sudo rm -r {}/{}/web_static".format(r_release, archive_ext))
            run('sudo rm /tmp/{}'.format(f_name))
            run('sudo rm -f /data/web_static/current')
            run('sudo ln -s {}/{} /data/web_static/current'.format(
                r_release, archive_ext))
            print('New version deployed!')
            return True
        except Exception as e:
                print(f"Error during deployment: {e}")
                return False

    else:
        return False

@task
def deploy():
    """
    creates and distributes an archive to the web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    else:
        return do_deploy(archive_path)
