import time
from string import Template

import pytest
import yaml


@pytest.fixture()
def get_tagname():
    return  str(time.time())
@pytest.fixture()
def getuserid():
    a = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    return f'1{a[4:14]}'
def getmo():
    a=str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    return f'1{a[4:14]}'

def getdata():
    with open("./datas/usercreate.yml",encoding='utf-8') as f:
        read_yml=f.read()
        tempTemplate=Template(read_yml)
        c=tempTemplate.safe_substitute({"mobile":getmo(),"userid":getmo()})
        data=yaml.safe_load(c)
    return data
data=getdata()
print(data)
@pytest.fixture(params=data['data'],ids=data['ids'])
def userinfo(request):
    return request.param
