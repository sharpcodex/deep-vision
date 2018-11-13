from deep_vision.model import Model


class FramesProcessor:
    def __init__(self, output_to):
        self.output_frame = output_to
        self.model = Model()

    def process_frame(self, frame):
        self.output_frame(self.model.predict(frame))
