import time
import hmac
import json
import requests
import pandas as pd
from hashlib import sha256
from functools import partial
from ztshare.util.str_util import random_str


class DataApi:

    __http_url = "http://139.224.3.74:8080/api/ds/pro"


    def __init__(self, app_id: str, app_secret: str, timeout: int=10) -> None:
        self.__app_id = app_id
        self.__app_secret = app_secret
        self.__timeout = timeout

    def __sign(self, api_code):
        ''' 签名算法HmacSHA256
        :param 原始请求参数
        '''
        _timestamp = int(time.time())
        _nounce_str = random_str()
        _data = str(_timestamp) + _nounce_str + str(api_code)
        _data = _data.replace(' ', '').encode('utf-8')
        _appsecret = self.__app_secret.encode('utf-8')  # 秘钥
        _signature = hmac.new(_appsecret, _data, digestmod=sha256).hexdigest()
        return _timestamp, _nounce_str, _signature

    def query(self, api_code, **kwargs):
        """ 调用服务：构造签名 封装请求参数
        :api_code  api编码对应接口
        :kwargs    可选参数
        """
        timestamp, nounce_str, signature = self.__sign(api_code)
        req_params = {
            "apiCode": api_code,
            "appId": self.__app_id,
            "ts": timestamp,
            "ns": nounce_str,
            "signature": signature,
            "data": kwargs,
        }
        req = requests.post(self.__http_url, json=req_params, timeout=self.__timeout)
        try:
            res = json.loads(req.text)
        except:
            raise Exception(req.text)
        if res["resultCode"] != 20000:
            raise Exception(res["resultMsg"])
        result = res['result']
        return pd.DataFrame(result)
    

    def __getattr__(self, name):
        return partial(self.query, name)
