import cv2
import numpy as np
import urllib.request
from PyQt5 import QtCore


class ImageSource(QtCore.QObject):
    on_new_video_frame = QtCore.pyqtSignal(np.ndarray)

    def __init__(self, output_to, source_path, source_type, parent=None):
        super().__init__(parent)
        self.source_path = source_path
        self.source_type = source_type
        self.output_frame = output_to

    def start_reading(self):
        image = None
        if 'Camera' in self.source_type:
            camera = cv2.VideoCapture(0)
            _, image = camera.read()
            camera.release()
        elif 'File' in self.source_type:
            image = cv2.imread(self.source_path)
        elif 'Network' in self.source_type:
            with urllib.request.urlopen(self.source_path) as url:
                image = url.read()
            image = np.asarray(bytearray(image), dtype="uint8")
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        self.output_frame(image)
