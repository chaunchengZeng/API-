# encoding: utf-8
import pytest
from api.tag import Tag
from base.base import Base


class TestTag(object):
    # 测试数据的测试驱动
    data = Base.yaml_load("./config/test_tag_step.yaml")

    @classmethod
    def setup_class(cls):
        cls.tag = Tag()

    def test_add(self):
        r = self.tag.add("Tencent")
        assert r["errcode"] == 0
        # 恢复环境：删除添加的标签
        res = self.tag.jsonpath('$..[?(@.tagname=="Tencent")]', self.tag.get())
        self.tag.delete(res[0]["tagid"])

    def test_get(self):
        r = self.tag.get()
        assert r["errcode"] == 0

    # def test_delete(self):
    #     r = self.tag.delete(10)
    #     assert r["errcode"] == 0

    @pytest.mark.parametrize("tagname", data["test_add"])
    def test_step_run(self, tagname):
        self.tag.step_run(tagname, self.data['steps'])
        self.tag.reset()
