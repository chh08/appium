import requests


def get_token():
    """测试通讯录"""
    # 获取token
    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww9de1334e944bb0d0&corpsecret=UZlXa4rp-54tE369hO0XCJc8DMc7cWZrI2ULh0F0N8E')
    # 把结果以json格式展示
    # print(r.json()['access_token'])
    # 断言errcode
    # assert 0 == r.json()['errcode']
    # 将token存到变量里
    token = r.json()['access_token']
    return token


def test_defact_member():
    """读取"""
    get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid=666'

    r = requests.get(get_member_url)
    print(r.json())
    assert "xiaoing" == r.json()['name']


def test_update_member():
    """更新"""
    update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}'
    data = {
        "userid": "666",
        "name": "李四",
        "mobile": "13812345678",

    }
    r = requests.post(url=update_member_url, json=data)
    print(r.json())


def test_create_member():
    """创建"""
    create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}'
    data = {
        "userid": "zhangsan123",
        "name": "张三",
        "mobile": "+86 13811111111",
        "department": [1],
    }
    r = requests.post(url=create_member_url, json=data)
    print(r.json())


def test_delete_member():
    """删除"""
    delete_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=zhangsan123'
    r = requests.get(delete_member_url)
    print(r.json())