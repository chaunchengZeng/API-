# encoding: utf-8
import pytest
import json
from api.group_chat import GroupChat


class TestWechatApi(object):
    _corpsecret = "ZuqJiGA6NjxfWJOizNlcoy0F0gEgIuGyAjHXbx3Cxyo"
    _userid = "ZengChuanCheng"

    @classmethod
    def setup_class(cls):
        cls.base = GroupChat(cls._corpsecret)

    def test_groupchat_get(self):
        res = self.base.list(userid="ZengChuanCheng")
        print(json.dumps(res, indent=4))  # 这样可以打印更容易看些
        assert res["errcode"] == 0

        result = self.base.get(external_userid=res["external_userid"][0])
        assert result['errcode'] == 0


if __name__ == '__main__':
    pytest.main()
