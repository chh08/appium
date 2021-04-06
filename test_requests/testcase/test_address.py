import pytest
import yaml

from test_requests.wework_contact.address import Address


class TestAddress:
    def setup(self):
        # 实例化
        self.address = Address()

    @pytest.mark.parametrize("user_id, name, mobile, department",
                             yaml.safe_load(open("../datas/members.yaml","r",encoding="utf-8"))["create_member"])
    def test_create_member(self, user_id, name, mobile, department):
        # 利用删除接口进行数据清理
        # 删除成员
        self.address.delete_member(user_id)
        # 创建成员
        r = self.address.create_member(user_id, name, mobile, department)
        # get可以获取r里的值，和【】一样，但是get不存在的值不会报错s
        # 断言
        assert r.get('errmsg', 'network error') == 'created'
        # 创建之后需要再次查询，断言创建信息是否正确
        r = self.address.get_member_info(user_id)
        # 删除无用数据
        # 在断言前删，防止断言不通过时不调用删除
        self.address.delete_member(user_id)
        assert r.get("name") == name

    @pytest.mark.parametrize("user_id, name, mobile, department",
                             yaml.safe_load(open("../datas/members.yaml", "r", encoding="utf-8"))["get_member"])
    def test_get_member_info(self, user_id, name, mobile, department):
        # 运行前创建成员，防止没有成员
        self.address.create_member(user_id, name, mobile, department)
        # 查询
        r = self.address.get_member_info(user_id)
        # 删除无用数据
        # 在断言前删，防止断言不通过时不调用删除
        self.address.delete_member(user_id)
        assert r.get('errmsg', 'network error') == 'ok'
        assert r.get("name") == name

    @pytest.mark.parametrize("user_id, name, mobile, department",
                             yaml.safe_load(open("../datas/members.yaml", "r", encoding="utf-8"))["delete_member"])
    def test_delete_member(self, user_id, name, mobile, department):
        # 删除前创建
        self.address.create_member(user_id, name, mobile, department)
        # 删除成员
        r = self.address.delete_member(user_id)
        assert r.get('errmsg', 'network error') == 'deleted'
        r = self.address.get_member_info(user_id)
        assert r.get('errcode') == 60111

    @pytest.mark.parametrize("user_id, name, mobile, department",
                             yaml.safe_load(open("../datas/members.yaml", "r", encoding="utf-8"))["update_member"])
    def test_update_member(self, user_id, name, mobile, department):
        # 保证成员一定是新添加的
        # 删除成员
        self.address.delete_member(user_id)
        # update前创建
        self.address.create_member(user_id, name, mobile, department)
        # 传递一个新名字
        new_name = name + "tmp"
        r = self.address.update_member(user_id, new_name, mobile)
        assert r.get('errmsg', 'network error') == 'updated'
        r = self.address.get_member_info(user_id)
        assert r.get("name") == new_name
