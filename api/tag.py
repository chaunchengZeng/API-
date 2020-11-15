# encoding: utf-8
from base.base import Base
import yaml


class Tag(Base):
    _corpsecret = "ZuqJiGA6NjxfWJOizNlcoy0F0gEgIuGyAjHXbx3Cxyo"

    def __init__(self):
        self.get_token(self._corpsecret)
        self.data = self.api_load("../config/tag_api.yaml")

    def add(self, tagname, tagid=None, **kwargs):
        """
        创建标签
        :param tagid: 标签id，默认为None
        :param tagname: 标签名字
        :return: dict(响应结果)
        """
        self._params['tagname'] = tagname
        if tagid is not None:
            self._params["tagid"] = tagid
        return self.api_send(self.data['add'])

    def get(self, **kwargs):
        return self.api_send(self.data['get'])

    def delete(self, tagid, **kwargs):
        """
        创建标签
        :param tagid:
        :param tagname: 标签名字
        :return: dict(响应结果)
        """
        self._params['tagid'] = tagid
        return self.api_send(self.data['delete'])

    def reset(self, **kwargs):
        """
        重置：删除所以标签
        :return:
        """
        res = self.jsonpath('$..[?(@.tagname)]', self.get())
        if isinstance(res, list) and len(res) > 0:
            for r in res:
                self.delete(r["tagid"])

    def step_run(self, tagname, steps: list):
        """
        步骤驱动
        :param name: 标签名称
        :param steps:
        :return:
        """
        self._params['tagname'] = tagname
        for step in steps:
            raw = yaml.dump(step)
            for key, value in self._params.items():
                raw = raw.replace(f"'${{{key}}}'", repr(value))
            step = yaml.load(raw)
            if isinstance(step, dict):
                if "method" in step.keys():
                    # getattr(self, method)(**step) = self.method(**step)
                    # todo: 此处还不兼容还带其他参数的add和delete函数，用装饰器精简参数
                    getattr(self, step['method'])(**step)
                if "extract" in step.keys():
                    self.data[step["extract"]] = getattr(self, 'jsonpath')(**step)
                    print("extract")
                    print(self.data[step["extract"]])

                if "assertion" in step.keys():
                    assertion = step["assert"]
                    if isinstance(assertion, str):
                        # eval：执行一个字符串表达式，并返回结果
                        assert eval(assertion)


if __name__ == "__main__":
    tag = Tag()
    # r = Tag.yaml_load('../config/test_tag_step.yaml')
    # tag.step_run(r)
    tag.reset()
