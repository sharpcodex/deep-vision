from deep_vision.models_helpers.AbstractModel import AbstractModel
from deep_vision.models_helpers.imageutilities import put_text  # in future, this module will contain more helpers


class Model(AbstractModel):
    def __init__(self):
        # this code will be executed one time, when the user select a new image or video source.
        # initialize your model here
        # self.model = load_my_model()
        pass

    def predict(self, current_frame):
        # this code will be executed for every frame in the selected video,
        # or only one time if the selected source is an image(an image is a single frame).
        # Get your model predictions for the current frame
        # preds = self.model.predict(image)
        # Then, draw boxes, write text, or do what ever you want to the current frame,
        # you can use the built-in model helpers, like put_text().
        put_text(current_frame, "preds")
        # return the frame, and see it displayed or saved
        return current_frame
