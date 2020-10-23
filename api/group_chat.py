import requests
from base.base import Base


class GroupChat(object):
    def __init__(self, corpsecret):
        self. token = Base.get_token(corpsecret)

    def list(self, userid, **kwargs):
        _url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/list"
        params = {"access_token": self.token,
                  "userid": userid}
        _json = {}
        _json.update(kwargs)
        res = requests.post(url=_url, params=params)

        return res.json()

    def get(self, external_userid):
        # todo 多环境支持
        # todo 自动加减密
        params = {
            "access_token": self.token,
            "external_userid": external_userid,
        }
        res = requests.get('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get', params=params)
        return res.json()