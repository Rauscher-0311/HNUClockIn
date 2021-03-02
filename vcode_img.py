import requests
import json
import cv2

class vcode_img:
    def __init__(self):
        self.headers = {
            "Host": "fangkong.hnu.edu.cn",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }
        self.token_url = "https://fangkong.hnu.edu.cn/api/v1/account/getimgvcode"
        self.vcode_img_url = "https://fangkong.hnu.edu.cn/imagevcode?token="

    def get_token(self):
        token = ""
        token_r = requests.get(self.token_url, headers= self.headers)
        token_json = json.loads(token_r.text)
        token = token_json["data"]["Token"]
        # print(token)
        return token

    def get_img_byte(self, token):
        url = self.vcode_img_url + token

        cap = cv2.VideoCapture(url)
        assert cap.isOpened()
        ret,img = cap.read()
        # print(img)
        # cv2.imshow("image",img)
        # cv2.waitKey()

        _, img = cv2.imencode(".jpg", img)
        return img.tostring()
