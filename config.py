#PRI.GPIO    pin 4 in
ALIVE_DETECTOR_PIN = 18
GREEN_LED_PIN = 17 #16
YELLOW_LED_PIN = 27 #20
RED_LED_PIN = 22#21

# Threshold for the confidence of a recognized face before it's considered a
# positive match.  Confidence values below this threshold will be considered
# a positive match because the lower the confidence value, or distance, the
# more confident the algorithm is that the face was correctly detected.
# Start with a value of 3000, but you might need to tweak this value down if 
# you're getting too many false positives (incorrectly recognized faces), or up
# if too many false negatives (undetected faces).
POSITIVE_THRESHOLD = 85.0


STATE_PAUSE = 'pause'
STATE_SEARCH = 'search'
STATE_TRAIN = 'train'
STATE_DETECT = 'detect'
STATE_TR_CP = 'train complete'
STATE_NOFACE = 'no face saved'


COLOR_BLACK = (0,0,0)
COLOR_RED = (0,0,255)
COLOR_GREEN = (0,255,0)
COLOR_BLUE = (255,0,0)
COLOR_WHITE = (255,255,255)
# File to save and load face recognizer model.
TRAINING_FILE = 'training.xml'

# Directories which contain the positive and negative training image data.
POSITIVE_DIR = './training/positive'
NEGATIVE_DIR = './training/negative'
TRAIN_DIR = './train'

# Value for positive and negative labels passed to face recognition model.
# Can be any integer values, but must be unique from each other.
# You shouldn't have to change these values.
POSITIVE_LABEL = 1
NEGATIVE_LABEL = 2

FACE_NAME = 'gr'
NAME_FILE = 'name.csv'
TRAINED_FILE = 'traned.csv'
TIME_FILE = 'time.csv'
# Size (in pixels) to resize images for training and prediction.
# Don't change this unless you also change the size of the training images.
FACE_WIDTH  = 92
FACE_HEIGHT = 112

# Face detection cascade classifier configuration.
# You don't need to modify this unless you know what you're doing.
# See: http://docs.opencv.org/modules/objdetect/doc/cascade_classification.html
HAAR_FACES         = 'haarcascade_frontalface_alt.xml'
HAAR_SCALE_FACTOR  = 1.3
HAAR_MIN_NEIGHBORS = 4
HAAR_MIN_SIZE      = (30, 30)

WINDOW_MIN_SIZE        = (320,240)
WINDOW_MAX_SIZE        = (640,480)

# Filename to use when saving the most recently captured image for debugging.
DEBUG_IMAGE = 'capture.pgm'

def get_camera():	
	# Camera to use for capturing images.
	# Use this code for capturing from the Pi camera:
	import picam
	return picam.OpenCVCapture()
	# Use this code for capturing from a webcam:
	# import webcam
	# return webcam.OpenCVCapture(device_id=0)
