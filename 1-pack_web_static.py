#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
""" prototype of the function """


from datetime import datetime
from fabric.api import *
import os


def do_pack():
    """Fabscript that generates a .tgz archive of contents of e web_static"""
    dt = datetime.now()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
