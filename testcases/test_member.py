
import time


import allure
import pytest


from API.api.member import User

@allure.feature('成员管理')
class TestMember:
    def setup(self):
        self.user=User()

    @allure.story('添加用户：user/create')
    def test_add(self,userinfo):

        r=self.user.create_user(userinfo[0].get('params'))

        assert r.json().get('errcode')==userinfo[1].get('result')
    @allure.story('删除用户')
    @pytest.mark.parametrize('userid',[time.strftime("%Y%m%d%H%M%S", time.localtime()),4214,213251],ids=['删除成功','删除的用户id不存在','重复删除一个userid'])
    def test_delete(self,getuserid,userid):
        self.user.create_user({'department': 1, 'mobile': getuserid, 'name': 'zhangsan', 'userid': userid})
        r=self.user.delete_user(userid)
        assert r.json().get('errcode')==0


