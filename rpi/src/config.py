LOCALE = 'UTF-8'

#Android BT connection settings

RFCOMM_CHANNEL = 1
RPI_MAC_ADDR = 'b8:27:eb:5a:34:dc'
UUID = '48f2491c-350e-4c1c-b181-7e4a591cc311'
ANDROID_SOCKET_BUFFER_SIZE = 512

# Algorithm Wifi connection settings
# raspberryHotPotato: 192.168.3.1
WIFI_IP = '192.168.3.1'
WIFI_PORT = 8080
ALGORITHM_SOCKET_BUFFER_SIZE = 512

# Arduino USB connection settings
# SERIAL_PORT = '/dev/ttyACM0'
# Symbolic link to always point to the correct port that arduino is connected to
SERIAL_PORT = '/dev/ttyACM0'
BAUD_RATE = 115200

# Image Recognition Settings
STOPPING_IMAGE = 'stop_image_processing.jpg'

IMAGE_WIDTH = 640
IMAGE_HEIGHT = 360
IMAGE_FORMAT = 'bgr'

#from seniors
BASE_IP = 'tcp://192.168.3.'
PORT = ':5555'

IMAGE_PROCESSING_SERVER_URLS = 'tcp://192.168.3.13:5555'


