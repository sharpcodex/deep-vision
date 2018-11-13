import cv2
import numpy as np
from PyQt5 import QtCore


class QtVideoSource(QtCore.QObject):
    on_new_video_frame = QtCore.pyqtSignal(np.ndarray)

    def __init__(self, output_to, source_path, parent=None):
        super().__init__(parent)
        self.source = cv2.VideoCapture(source_path)
        self.timer = QtCore.QBasicTimer()
        self.on_new_video_frame.connect(output_to)

    def start_reading(self):
        self.timer.start(0, self)

    def release(self):
        self.timer.stop()
        if self.source:
            self.source.release()
        self.source = None

    def timerEvent(self, event):
        if event.timerId() != self.timer.timerId():
            return
        success, frame = self.source.read()
        if success:
            self.on_new_video_frame.emit(frame)
        else:
            self.timer.stop()
            self.release()
