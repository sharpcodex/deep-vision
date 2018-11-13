from PyQt5 import QtCore
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QInputDialog, QLineEdit

from deep_vision import config


class QWindowEventFilter(QtCore.QObject):
    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.ActivationChange:
            if self.parent().isActiveWindow():
                self.parent().on_window_activation()
            else:
                self.parent().on_window_deactivation()
        return QtCore.QObject.eventFilter(self, obj, event)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        path = config.APP_PATH / 'app_interface' / 'desktop'

        # Load Ui
        loadUi(str(path / 'main_window.ui'), self)
        self.installEventFilter(QWindowEventFilter(self))

        # Setup Window
        self.setWindowIcon(QIcon(str(path / 'favicon.png')))
        self.setWindowTitle(config.APP_NAME)
        self.displayerWidget.setScaledContents(True)

        # Events handlers
        self.exitAction.triggered.connect(self.on_exit_action_triggered)
        self.cameraTakeImageAction.triggered.connect(lambda x: self.select_camera_source('CameraImage'))
        self.cameraRecordVideoAction.triggered.connect(lambda x: self.select_camera_source('CameraVideo'))
        self.filesReadImageAction.triggered.connect(lambda x: self.select_file_source('FileImage'))
        self.filesReadVideoAction.triggered.connect(lambda x: self.select_file_source('FileVideo'))
        self.networkReadImageAction.triggered.connect(lambda x: self.select_network_source('NetworkImage'))
        self.networkReadVideoAction.triggered.connect(lambda x: self.select_network_source('NetworkVideo'))
        self.aboutAction.triggered.connect(self.on_about_action_triggered)

        # Shortcuts config
        self.exitAction.setShortcut('ESC')

        self.bar_log(config.APP_NAME)

    def select_camera_source(self, source_type):
        self.create_new_source(config.Camera_ID, source_type)

    def select_file_source(self, source_type):
        types = " ".join(config.IMAGES_TYPES) if 'Image' in source_type else " ".join(config.VIDEOS_TYPES)
        source_path, _ = QFileDialog.getOpenFileName(self, filter="Image files (" + types + ")")
        if source_path:
            self.create_new_source(source_path, source_type)

    def select_network_source(self, source_type):
        source_path, success = QInputDialog.getText(self, "Network Resource", "Url:", QLineEdit.Normal, "")
        if success and source_path != '':
            self.create_new_source(source_path, source_type)

    def create_new_source(self, source_path, source_type):
        pass

    def on_window_activation(self):
        pass

    def on_window_deactivation(self):
        pass

    def on_about_action_triggered(self):
        QMessageBox.about(self, config.ABOUT_TITLE, config.ABOUT_MESSAGE)

    def bar_log(self, msg):
        self.statusBar().showMessage(msg)

    @staticmethod
    def on_exit_action_triggered():
        QtCore.QCoreApplication.instance().quit()
