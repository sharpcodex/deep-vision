# deep vision
**deep vision** is an open source software, created to help fastai students in applying deep learning techniques to videos and images, by doing most of the 'programming' part, and let the students focus on the deep learning part.

## Key Features
* Get images and videos from Camera, Files and Network.
* Display images and videos on desktop or web(work in progress).
* save resulting images and videos to file.
* Very easy to configure
* Very easy to add you deep learning model

## Config file

Config Key|Default Value|Possible Values|Explanation
-------------|-------------|-------------|-------------
APP_NAME | 'Deep Vision' | any string | The application title (desktop and web).
ABOUT_TITLE | "Deep Vision" | any string | The about box title (desktop and web).
ABOUT_MESSAGE | "Created By : FastAI Student" | any string | The about box contents (desktop and web).
APP_TYPE | 'desktop' | desktop, web | Run the app as a desktop or a web application.
SHOW_MEDIA | True | True, False | Show images and videos on screen.
SAVE_MEDIA | True | True, False | Save images and videos to file.
SAVE_MEDIA_PATH | None | any string, None | Save images and videos to this folder, set to None to use application path.
SAVE_MEDIA_FILE | None | any string, None | Save images and videos to this file, set to None to use random file name.
SHOW_LOGS | False | True, False | Print applications logs to console.
CAMERA_ID | 0 | numbers | Target camera id, 0 for default camera
IMAGES_TYPES | ['*.jpg', '*.jpeg', '*.jpe', '*.png', '*.bmp'] | any image format supported by openCV| Open image dialog file types
VIDEOS_TYPES | ['*.mp4', '*.avi'] | any video format supported by openCV | Open video dialog file types
SCALE_IMAGES | True | True, False | Scale source image to fit container (desktop or web)

## How to use
* install the dependencies
```shell
$ conda install pyqt
$ conda install opencv
```
* modify the config file to whatever you want
* open model.py file and follow the comments to add your model
```python
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
```
* run the app



