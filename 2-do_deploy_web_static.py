#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ["18.209.224.234", "52.23.213.75"]

def do_deploy(archive_path):
    """
    deployes web static 1
    """
    if exists(archive_path):
        f_name = archive_path.split("/")[-1]
        archive_no_ext = f_name.split(".")[0]
        r_release = "/data/web_static/releases"
        try:
            put(archive_path, '/tmp/')
            run('sudo mkdir -p {}/{}/'.format(r_release, archive_no_ext))
            run('sudo tar -xzf /tmp/{} -C {}/{}/'.format(f_name, r_release, archive_no_ext))
            run("sudo mv {}/{}/web_static/* {}/{}/".format(r_release, archive_no_ext, r_release, archive_no_ext))
            run ("sudo rm -r {}/{}/web_static".format(r_release, archive_no_ext))
            run('sudo rm /tmp/{}'.format(f_name))
            run('sudo rm -f /data/web_static/current')
            run('sudo ln -s {}/{}/data/web_static/current'.format(r_release, archive_no_ext))
            print('New version deployed!')
            return True
        except:
            return False
    else:
        return False
