# encoding: utf-8
import requests
import json
from jsonpath import jsonpath

import yaml


class Base:
    _params = {}
    _token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    _corpid = "wwcbefdd1de3927e42"

    @classmethod
    def yaml_load(cls, path):
        """
        读取yaml数据文件
        :param path: yaml文件路径
        :return: dict(文件内容)
        """
        with open(path, encoding='utf-8') as f:
            return yaml.safe_load(f)

    def jsonpath(self, path, r=None, **kwargs):
        """
        jsonpath 查找json格式响应的某字段
        :param path: jsonpath的查询表达式
        :param r: json响应，默认为空，从最近的请求中self.format获取
        :param kwargs:
        :return: 返回找到的字段 -> list
        """
        # 这也可以用到最新的响应
        if r is None:
            r = self.r.json()
        return jsonpath(r, path)

    @classmethod
    def format(cls, res):
        """
        对字典格式数据美化打印
        :param res: requests请求响应的未解码数据
        :return:
        """
        # 记录最新的响应
        cls.r = res
        print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))

    def api_load(self, path):
        return self.yaml_load(path)

    def api_send(self, data: dict):
        """
        发送api请求，发送前把python数据转化为yaml流做替换再转回来
        :param data: dict(参数数据)
        :return: dict(响应结果)
        """
        raw = yaml.dump(data)
        for key, value in self._params.items():
            # 替换${key}字段，f'{{}}' => {}
            # repr(value)保证value不是str也能加进去
            raw = raw.replace(f"'${{{key}}}'", repr(value))
        data = yaml.load(raw)
        res = requests.request(data["method"],
                               url=data["url"],
                               params=data["params"],
                               # data.get("json")若data没有json字段不会报错
                               json=data.get("json"))
        self.format(res)
        return res.json()

    @classmethod
    def get_token(cls, corpsecret):
        if "access_token" not in cls._params:
            res_dict = cls.get_access_token(corpsecret)
            cls._params["access_token"] = res_dict["access_token"]

    @classmethod
    def get_access_token(cls, corpsecret):
        _token_url_params = {
            "corpid": cls._corpid,
            "corpsecret": corpsecret,
        }
        res = requests.get(cls._token_url, params=_token_url_params)
        print(res)
        return res.json()
