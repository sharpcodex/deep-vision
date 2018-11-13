# feel free to change these settings
APP_NAME = 'Deep Vision'  # any string:	The application title (desktop and web).
ABOUT_TITLE = "Deep Vision"  # any string: The about box title (desktop and web).
ABOUT_MESSAGE = "Created By : FastAI Student"  # any string: The about box contents (desktop and web).
APP_TYPE = 'desktop'  # desktop, web: Run the app as a desktop or a web application.
SHOW_MEDIA = True  # True, False: Show images and videos on screen.
SAVE_MEDIA = False  # True, False: Save images and videos to file.
SAVE_MEDIA_PATH = None  # any string, None: Save images and videos to this folder, set to None to use application path.
SAVE_MEDIA_FILE = None  # any string, None: Save images and videos to this file, set to None to use random file name.
# Mostly you will not want to change these settings
SHOW_LOGS = False  # True, False: Print applications logs to console.
CAMERA_ID = 0  # numbers: Target camera id, 0 for default camera
IMAGES_TYPES = ['*.jpg', '*.jpeg', '*.jpe', '*.png',
                '*.bmp']  # any image format supported by openCV: Open image dialog file types
VIDEOS_TYPES = ['*.mp4', '*.avi']  # any video format supported by openCV: Open video dialog file types
SCALE_IMAGES = True  # True, False: Scale source image to fit container (desktop or web)

# don't change these settings
APP_PATH = './'
