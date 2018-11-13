from deep_vision.models_helpers.AbstractModel import AbstractModel
from deep_vision.models_helpers.imageutilities import put_text


class Model(AbstractModel):
    def __init__(self):
        # initialize your model here
        # self.model = ...
        pass

    def predict(self, image):
        # get model predictions
        # preds = self.model.predict(image)
        # draw boxes, write text on the image, etc
        put_text(image, "preds")
        return image
