import os

try:
    import requests
except:
    os.system("pip install requests")

try:
    import cv2
except:
    os.system("pip install opencv-python")

try:
    from aip import AipOcr
except:
    os.system("pip install baidu-aip")