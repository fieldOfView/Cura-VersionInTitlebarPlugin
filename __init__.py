# Copyright (c) 2018 fieldOfView
# The VersionInTitlebarPlugin is released under the terms of the AGPLv3 or higher.

from . import VersionInTitlebarPlugin

def getMetaData():
    return {}

def register(app):
    return {"extension": VersionInTitlebarPlugin.VersionInTitlebarPlugin()}
