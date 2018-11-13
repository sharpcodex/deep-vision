class FramesProcessor:
    def __init__(self, output_to):
        self.output_frame = output_to
        self.models = []

    def process_frame(self, frame):
        self.output_frame(frame)
