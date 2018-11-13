from pathlib import Path

import cv2

from deep_vision import config


class FramesRecorder:
    def __init__(self, output_to, source_type):
        self.output_frame = output_to
        self.source_type = source_type
        self.frame_writer = None

    def record_frame(self, frame):
        if config.SAVE_MEDIA:
            save_to_file = Path(config.SAVE_MEDIA_PATH).joinpath(config.SAVE_MEDIA_FILE)
            if 'Video' in self.source_type:
                if not self.frame_writer:
                    codecs = cv2.VideoWriter_fourcc(*'mp4v')
                    h = frame.shape[0]
                    w = frame.shape[1]
                    self.frame_writer = cv2.VideoWriter(str(save_to_file) + '.mp4', codecs, 20.0, (w, h))
                self.frame_writer.write(frame)
            else:
                cv2.imwrite(str(save_to_file) + '.jpg', frame)
        self.output_frame(frame)

    def release(self):
        if self.frame_writer:
            self.frame_writer.release()
            self.frame_writer = None
