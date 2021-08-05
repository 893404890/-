import os

import allure
import pytest

from API.api.tag import Tag
class TestTag:
    def setup_class(self):
        self.tag=Tag()

    @allure.story('添加标签')
    @allure.title('标签名{tagname}')
    @pytest.mark.parametrize('tagname',[121313,31313,31313])
    def test_add(self,tagname):

        r=self.tag.add(tagname)

        assert r.json().get('errcode') == 0

    def test_update(self,get_tagname):
        new_tag=self.tag.add(get_tagname).json()

        r=self.tag.update(new_tag.get('tagid'),get_tagname+'new')

        assert r.json().get('errcode') == 0

    def test_delete(self,get_tagname):
        new_tag=self.tag.add(get_tagname)
        r = self.tag.delete(new_tag.json().get('tagid'))
        print(r.json())

    def test_get(self):

        r=self.tag.get()

        assert r.json().get('errcode') == 0
if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ../results/ -o ./report --clean')