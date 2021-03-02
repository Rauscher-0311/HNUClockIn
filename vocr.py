from aip import AipOcr

class vocr:
    def __init__(self, inform):
        self.app_id = inform.api["app_id"]
        self.api_key = inform.api["api_key"]
        self.secret_key = inform.api["secret_key"]

    def vcode(self, img):
        client = AipOcr(self.app_id, self.api_key, self.secret_key)
        return client.basicGeneral(img)["words_result"][0]["words"]