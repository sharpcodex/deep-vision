import os
import sys
from pathlib import Path

from deep_vision import config

_excepthook = sys.excepthook


def exception_hooker(exception_type, value, traceback):
    print("Exiting, exception hooker:", exception_type, value, traceback)
    _excepthook(exception_type, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hooker

if __name__ == '__main__':
    config.APP_PATH = Path(os.getcwd())

    if 'desktop' in config.APP_TYPE:
        from PyQt5.QtWidgets import QApplication
        from deep_vision.app_interface.desktop.main_window import MainWindow

        app = QApplication(sys.argv)
        main_window = MainWindow()
        main_window.show()
        app.exec_()

    try:
        sys.exit()
    except Exception as exp:
        print("Exiting, exception:", exp)
