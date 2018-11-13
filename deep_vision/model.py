from deep_vision.models_helpers.AbstractModel import AbstractModel
from deep_vision.models_helpers.imageutilities import put_text  # in future, this module will contain more helpers


class Model(AbstractModel):
    def __init__(self):
        # this code will execute one time, when the user select a new media source.
        # initialize your model here
        # self.model = load_my_model()
        pass

    def predict(self, current_frame):
        # this code will be executed for every frame in videos,
        # or only one time for images(an image is a single frame).
        # So, get your model predictions for the current frame
        # preds = self.model.predict(image)
        # Then, draw boxes, write text(you can use put_text), or do what ever you want to the current frame
        put_text(current_frame, "preds")
        # return the frame, and see it displayed or saved
        return current_frame
