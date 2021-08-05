import logging

import requests
class BaseApi:


    BASE_URL='https://qyapi.weixin.qq.com/cgi-bin/'
    def __init__(self):
        self.token=self.get_token()

    def get_token(self):
        '''
        获取token
        :return: 返回token
        '''
        url = 'gettoken'
        data = {
            "corpid": "wwba502d2249d46009",
            "corpsecret": "n2YnkwqqYeNvEDBR46ow3tG2oz_ZIE43oNiZ_ifxB10"
        }
        r = self.request(method="post", url=url, json=data)

        return r.json().get("access_token")


    def request(self,method,url,**kwargs):
        '''
        封装发送请求
        :param method: 请求方式
        :param url:
        :param kwargs:
        :return:
        '''
        self.json_data=requests.request(method,self.BASE_URL+url, **kwargs)
        return self.json_data

