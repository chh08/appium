from test_requests.wework_contact.base import Base


class Address(Base):

    def get_member_info(self, userid):
        """读取"""
        get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        # 利用params特性减短url长度
        params = {
        "userid": userid
        }

        r = self.send(0, get_member_url, params=params)
        return r.json()

    def update_member(self, userid, name, mobile):
        """更新"""
        update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,

        }
        r = self.send(1, url=update_member_url, json=data)
        return r.json()

    def create_member(self, userid, name, mobile, department):
        """创建"""
        create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department,
        }
        r = self.send(1, url=create_member_url, json=data)
        return r.json()

    def delete_member(self, userid):
        """删除"""
        delete_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        # 利用params特性减短url长度
        params = {
        "userid": userid
        }
        r = self.send(0, delete_member_url, params=params)
        return r.json()