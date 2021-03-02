import requests
import json
import random

class hnu_clockin():
    def __init__(self, inform, AT_HOME):
        self.login_data = {
            "Code": inform.hnu["id"],
            "Password": inform.hnu["password"],
            "WechatUserinfoCode": None
        }
        self.login_path = "https://fangkong.hnu.edu.cn/api/v1/account/login"
        self.is_clockin_path = "https://fangkong.hnu.edu.cn/api/v1/clockinlog/isclockinloginfo"
        self.add_path = "https://fangkong.hnu.edu.cn/api/v1/clockinlog/add"
        self.headers = {
            "Referer": "https://fangkong.hnu.edu.cn/app/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }
        if AT_HOME == 1:
            self.add_data = {
                "Temperature": None,
                "RealProvince": inform.clockin_inform["省"],
                "RealCity": inform.clockin_inform["市"],
                "RealCounty": inform.clockin_inform["县"],
                "RealAddress": inform.clockin_inform["在家详细地址"],
                "IsUnusual": "0",
                "UnusualInfo": "",
                "IsTouch": "0",
                "IsInsulated": "0",
                "IsSuspected": "0",
                "IsDiagnosis": "0",
                "tripinfolist": [{
                    "aTripDate": "",
                    "FromAdr": "",
                    "ToAdr": "",
                    "Number": "",
                    "trippersoninfolist": []
                }],
                "toucherinfolist": [],
                "dailyinfo": {
                    "IsVia": "0",
                    "DateTrip": ""
                },
                "IsInCampus": "0",
                "IsViaHuBei": "0",
                "IsViaWuHan": "0",
                "InsulatedAddress": "",
                "TouchInfo": "",
                "IsNormalTemperature": "1",
                "Longitude": None,
                "Latitude": None
            }
        else:
            self.add_data = {
				"Longitude": None,
				"Latitude": None,
				"RealProvince": "湖南省",
				"RealCity": "长沙市",
				"RealCounty": "岳麓区",
				"RealAddress": inform.clockin_inform["在校详细地址"],
				"BackState": 1,
				"MorningTemp": "36." + str(random.randint(5,9)),
				"NightTemp": "36." + str(random.randint(5,9)),
				"tripinfolist": []
			}


    def load_vcode(self, token, vcode):
        self.login_data["Token"] = token
        self.login_data["VerCode"] = vcode

    def login(self):
        r = requests.post(self.login_path, data=self.login_data, headers= self.headers)
        cookies = r.cookies
        cookie = "; ".join([str(x)+"="+str(y) for x,y in cookies.items()])
        #请求头添加cookie
        self.headers["Cookie"] = cookie
        login_json = json.loads(r.text)
        msg = login_json["msg"]
        if msg == "成功":
            return True
        else:
            print(msg)
            return False

    def is_clockin(self):
        r = requests.get(self.is_clockin_path, headers= self.headers)
        j = json.loads(r.text)
        msg = j["msg"]
        if msg == "成功":
            return False
        else:
            return True

    def clockin(self):
        r = requests.post(self.add_path, json= self.add_data, headers= self.headers)
        j = json.loads(r.text)
        msg = j["msg"]
        if msg == "成功":
            return True
        else:
            return False
