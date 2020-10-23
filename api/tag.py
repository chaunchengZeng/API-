from base.base import Base


class Tag(Base):
    _corpsecret = "ZuqJiGA6NjxfWJOizNlcoy0F0gEgIuGyAjHXbx3Cxyo"

    def __init__(self):
        self.get_token(self._corpsecret)
        self.data = self.api_load("../api/tag_api.yaml")

    def get_api(self):
        pass

    def add(self):
        # todo 用装饰器解决参数替换，参考深信服的做法
        # todo format repr()类型替换
        return self.api_send(self.data['add'])
        # _url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/create'
        # r = requests.post(_url,
        #                   params={"access_token": self.get_token(self._corpsecret)},
        #                   json={"tagname": tagname})
        # self.format(r)
        # return r.json()

    def get(self):
        return self.api_send(self.data['get'])
        # _url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/get'
        # r = requests.post(_url,
        #                   params={
        #                       "access_token": self.get_token(self._corpsecret),
        #                       "tagid": tagid,
        #                           })
        # self.format(r)
        # return r.json()

    def delete(self, tagid):
        _url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/delete'
        # r = requests.get(_url,
        #                   params={
        #                       "access_token": self.get_token(self._corpsecret),
        #                       "tagid": tagid,
        #                           })
        # self.format(r)
        # return r.json()