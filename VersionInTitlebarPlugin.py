# Copyright (c) 2018 fieldOfView
# The VersionInTitlebarPlugin is released under the terms of the AGPLv3 or higher.

from UM.Extension import Extension
from cura.CuraApplication import CuraApplication

class VersionInTitlebarPlugin(Extension):
    def __init__(self):
        super().__init__()

        self._application = CuraApplication.getInstance()

        self._print_information = None
        self._main_window = None

        self._version_string = self._application.getVersion()
        self._application.engineCreatedSignal.connect(self._engineCreated)

        self._application_name = ""

    def _engineCreated(self):
        try:
            engine = self._application._qml_engine
        except AttributeError:
            engine = self._application._engine
        self._main_window = engine.rootObjects()[0]

        try:
            self._application_name = self._application.getApplicationDisplayName()
        except AttributeError:
            self._application_name = self._main_window.title()

        self._print_information = self._application.getPrintInformation()
        self._print_information.jobNameChanged.connect(self._updateWindowTitle)

        self._updateWindowTitle()

    def _updateWindowTitle(self):
        # set window title
        self._main_window.setTitle("%s - %s %s" % (self._print_information.jobName, self._application_name, self._version_string))

