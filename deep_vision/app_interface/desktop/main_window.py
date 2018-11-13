from PyQt5 import QtCore, QtGui
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QInputDialog, QLineEdit

from deep_vision import config
from deep_vision.app_helpers.app_logger import log
from deep_vision.media_helpers.frames_formatter import FramesFormatter
from deep_vision.media_helpers.frames_processor import FramesProcessor
from deep_vision.media_helpers.frames_recorder import FramesRecorder
from deep_vision.media_helpers.image_source import ImageSource
from deep_vision.media_helpers.qt_video_source import QtVideoSource


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

        # class init
        super(MainWindow, self).__init__(parent)
        path = config.APP_PATH / 'app_interface' / 'resources'
        self.formatter = None
        self.recorder = None
        self.processor = None
        self.source = None
        self.source_path = ""
        self.source_type = ""
        self.options = {}

        # Load Ui
        loadUi(str(path / 'main_window.ui'), self)
        self.installEventFilter(QWindowEventFilter(self))

        # Setup App Window
        self.setWindowIcon(QIcon(str(path / 'favicon.png')))
        self.setWindowTitle(config.APP_NAME)
        self.displayerWidget.setScaledContents(config.SCALE_IMAGES)

        # Window Events handlers
        self.exitAction.triggered.connect(self.on_exit_action_triggered)
        self.cameraTakeImageAction.triggered.connect(lambda: self.select_camera_source('CameraImage'))
        self.cameraRecordVideoAction.triggered.connect(lambda: self.select_camera_source('CameraVideo'))
        self.filesReadImageAction.triggered.connect(lambda: self.select_file_source('FileImage'))
        self.filesReadVideoAction.triggered.connect(lambda: self.select_file_source('FileVideo'))
        self.networkReadImageAction.triggered.connect(lambda: self.select_network_source('NetworkImage'))
        self.networkReadVideoAction.triggered.connect(lambda: self.select_network_source('NetworkVideo'))
        self.aboutAction.triggered.connect(self.on_about_action_triggered)

        # Shortcuts config
        self.exitAction.setShortcut('ESC')
        self.cameraTakeImageAction.setShortcut('Ctrl+I')
        self.cameraRecordVideoAction.setShortcut('Ctrl+V')
        self.filesReadImageAction.setShortcut('shift+I')
        self.filesReadVideoAction.setShortcut('shift+V')
        self.networkReadImageAction.setShortcut('alt+I')
        self.networkReadVideoAction.setShortcut('alt+V')

        self.bar_log(config.APP_NAME)

    def create_new_source(self, source_path, source_type):
        log('In create_new_source\n\tsource_path : {0}\n\tsource_type : {1}'.format(source_path, source_type))

        self.release_media()
        self.source_path = source_path
        self.source_type = source_type

        self.formatter = FramesFormatter(output_to=self.update_displayer_widget, convert_to_qimage=True)

        self.recorder = FramesRecorder(output_to=self.formatter.format_frame, source_type=self.source_type)

        self.processor = FramesProcessor(output_to=self.recorder.record_frame)

        if 'Video' in self.source_type:
            self.source = QtVideoSource(output_to=self.processor.process_frame, source_path=self.source_path)
        else:
            self.source = ImageSource(output_to=self.processor.process_frame, source_path=self.source_path,
                                      source_type=self.source_type)
        self.source.start_reading()

    def release_media(self):
        if 'Video' in self.source_type:
            self.source.release()
            self.recorder.release()

    def update_displayer_widget(self, frame):
        if config.SHOW_MEDIA:
            self.displayerWidget.setPixmap(QtGui.QPixmap.fromImage(frame))
            self.displayerWidget.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        else:
            self.displayerWidget.setText('Video Processing is running on background')

    def select_camera_source(self, source_type):
        self.create_new_source(config.CAMERA_ID, source_type)

    def select_file_source(self, source_type):
        types = " ".join(config.IMAGES_TYPES) if 'Image' in source_type else " ".join(config.VIDEOS_TYPES)
        source_path, _ = QFileDialog.getOpenFileName(self, filter='Image files ("{0}")'.format(types))
        if source_path:
            self.create_new_source(source_path, source_type)

    def select_network_source(self, source_type):
        source_path, success = QInputDialog.getText(self, "Network Resource", "Url:", QLineEdit.Normal, "")
        if success and source_path != '':
            self.create_new_source(source_path, source_type)

    def on_window_activation(self):
        pass

    def on_window_deactivation(self):
        pass

    def on_about_action_triggered(self):
        QMessageBox.about(self, config.ABOUT_TITLE, config.ABOUT_MESSAGE)

    def on_exit_action_triggered(self):
        self.release_media()
        QtCore.QCoreApplication.instance().quit()

    def bar_log(self, msg):
        self.statusBar().showMessage(msg)
