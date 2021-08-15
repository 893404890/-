import time
from string import Template
from typing import List

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
    with open("../datas/usercreate.yml",encoding='utf-8') as f:
        read_yml=f.read()
        tempTemplate=Template(read_yml)
        c=tempTemplate.safe_substitute({"mobile":getmo(),"userid":getmo()})
        data=yaml.safe_load(c)
    return data
data=getdata()

@pytest.fixture(params=data['data'],ids=data['ids'])
def userinfo(request):
    return request.param
#添加pytest命令行参数 选择环境
def pytest_addoption(parser):
    mygroup=parser.getgroup('zx')   #group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',  # 参数的默认值
                      dest='env',  # 存储的变量
                      help='set your run env'  # 帮助提示 参数的描述信息
                      )
# 如何针对传入的不同参数完成不同的逻辑 处理？ 创建一个fixture，
@pytest.fixture()
def cmdoption(request):
    myenv=request.config.getoption("--env")

    if myenv == 'dev':
        datapath='./datas/dev/test.yml'
    elif myenv == 'test':
        datapath='./datas/test/test.yml'

    with open(datapath) as f:
        datas=yaml.safe_load(f)
    return datas
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print("收集所有的测试用例.....")
    print(items)
    # items 代表 所有的测试用例的列表
    for item in items:
        # 用例的名字
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        # 用例的路径
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
