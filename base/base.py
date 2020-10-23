import requests
import json

import yaml


class Base:
    _token = []
    _token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    _corpid = "wwcbefdd1de3927e42"

    @classmethod
    def yaml_load(cls, path):
        with open(path, encoding='utf-8') as f:
            return yaml.safe_load(f)

    @classmethod
    def format(cls, r):
        cls.r = r
        # print(json.dumps(r.json(), indent=2))
        print(json.dumps(json.loads(r.text), indent=2, ensure_ascii=False))

    def api_load(self, path):
        return self.yaml_load(path)

    def api_send(self, req: dict):
        req['params']['access_token'] = self._token[0]
        print(req)
        r = requests.request(req["method"],
                             url=req["url"],
                             params=req["params"],
                             json=req["json"])
        self.format(r)
        return r.json()

    @classmethod
    def get_token(cls, corpsecret):
        # todo 这里还可以把时间记录下来，每次调用都判读一下时间
        if corpsecret not in cls._token:
            res_dict = cls.get_access_token(corpsecret)
            cls._token.append(res_dict["access_token"])
        return cls._token[-1]

    @classmethod
    def get_access_token(cls, corpsecret):
        _token_url_params = {
            "corpid": cls._corpid,
            "corpsecret": corpsecret,
        }
        res = requests.get(cls._token_url, params=_token_url_params)
        return res.json()
