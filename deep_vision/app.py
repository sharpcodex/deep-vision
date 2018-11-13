import os
import sys
import uuid
from pathlib import Path

from deep_vision import config
from deep_vision.app_helpers.app_logger import log

_excepthook = sys.excepthook


def exception_hooker(exception_type, value, traceback):
    print("Exiting, exception hooker:", exception_type, value, traceback)
    _excepthook(exception_type, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hooker

if __name__ == '__main__':
    config.APP_PATH = Path(os.getcwd())
    if not config.SAVE_MEDIA_PATH:
        config.SAVE_MEDIA_PATH = config.APP_PATH
    if not config.SAVE_MEDIA_FILE:
        config.SAVE_MEDIA_FILE = str(uuid.uuid4())[0:8]
    log('In __main__\n\tAPP_PATH : {0}\n\tSAVE_MEDIA_PATH : {1}'.format(config.APP_PATH, config.SAVE_MEDIA_PATH))

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
