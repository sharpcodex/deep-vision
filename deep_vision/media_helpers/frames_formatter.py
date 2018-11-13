from PyQt5 import QtGui


class FramesFormatter:
    def __init__(self, output_to, convert_to_qimage=True):
        self.output_frame = output_to
        self.convert_to_Qimage = convert_to_qimage

    def format_frame(self, frame):
        if self.convert_to_Qimage:
            frame = self.convert_to_qimage(frame)
        self.output_frame(frame)

    @staticmethod
    def convert_to_qimage(image):
        height, width, colors = image.shape
        bytes_per_line = 3 * width
        q_image = QtGui.QImage

        image = q_image(image.data,
                        width,
                        height,
                        bytes_per_line,
                        q_image.Format_RGB888)

        image = image.rgbSwapped()
        return image
