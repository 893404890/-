#标签管理
import logging

import allure
import pytest

from API.api.base_api import BaseApi


@allure.feature('标签管理')
class Tag(BaseApi):


    def add(self,tagname,**kwargs):
        '''
        创建标签
        :param tagname: 标签名
        :param kwargs: 其他参数
        :return:
        '''
        data={
            "tagname":tagname

        }
        data.update(kwargs)

        r=self.request("post",f'tag/create?access_token={self.token}',json=data)
        return r


    def delete(self,tagid):
        '''
        删除标签
        :return:
        '''
        r=self.request("get",f'tag/delete?access_token={self.token}&tagid={tagid}')
        return r

    def update(self,tagid,tagname):
        '''
        修改标签
        :param tagid: 标签id
        :param tagname: 标签名字
        :return:
        '''
        data={
   "tagid": tagid,
   "tagname": tagname
}
        r=self.request("post",f'tag/update?access_token={self.token}',json=data)
        logging.info(f'接口返回结果为{r.json()}')
        return r

    def get(self):
        '''

        :return:
        '''

        r=self.request('get',f'tag/list?access_token={self.token}')
        return r

