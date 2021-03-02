import json

class read_inform():
    def __init__(self):
        self.__path = "config/inform.json"
        self.hnu = self.api = self.clockin_inform = {}
        self.load_json()

    def load_json(self):
        with open(self.__path, "r", encoding="utf-8") as f:
            inform = json.load(f)
            self.hnu = inform["hnu_account"]
            self.api = inform["baidu_ai_account"]
            self.clockin_inform = inform["clockin_inform"]
