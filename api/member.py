import logging


from API.api.base_api import BaseApi


class User(BaseApi):
    '''
    成员管理
    '''


    def create_user(self,data):
        '''
        创建的用户
        :param data:
        :return:
        '''
        userdata=data
        r=self.request('post',f'user/create?access_token={self.token}',json=userdata)
        logging.info(f'{r.json()}')
        return r

    def read_user(self,userid):
        '''
        获取用户
        :return:
        '''
        r=self.request("get",f'user/get?access_token={self.token}&userid={userid}')
        logging.info(f'{r.json()}')
        return r
    def update_user(self,data):
        '''
        更新用户
        :param data:
        :return:
        '''
        updata=data
        r=self.request('post',f'user/update?access_token={self.token}',json=updata)
        logging.info(f'{r.json()}')
        return r
    def delete_user(self,userid):
        '''
        删除用户
        :return:
        '''
        r=self.request('get',f'user/delete?access_token={self.token}&userid={userid}')
        logging.info(f'{r.json()}')
        return r

