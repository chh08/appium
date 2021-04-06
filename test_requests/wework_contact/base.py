import requests


class Base:
    def __init__(self):
        # 实例化
        self.s = requests.Session()
        # 获取token
        self.token = self.get_token()
        # 将token存入self.s.params
        self.s.params = {"access_token": self.token}

    def send(self, method, *args, **kwargs):
        """封装发送请求方法"""
        if method == 0:
            return self.s.request("GET", *args, **kwargs)
        elif method == 1:
            return self.s.request("POST", *args, **kwargs)

    def get_token(self):
        """测试通讯录"""
        # 获取token
        params = {
            "corpid": "ww9de1334e944bb0d0",
            "corpsecret": "UZlXa4rp-54tE369hO0XCJc8DMc7cWZrI2ULh0F0N8E"
        }
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=params)
        # 将token存到变量里
        token = r.json()['access_token']
        return token
