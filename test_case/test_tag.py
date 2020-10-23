from api.tag import Tag
from base import base


class TestTag(object):
    # 测试数据的测试驱动
    data = base.Base.yaml_load("test_tag_data.yaml")
    @classmethod
    def setup_class(cls):
        cls.tag = Tag()

    # @pytest.mark.parametrize("name", ["sangfor1", "sangfor2", "sangfor3"])
    # @pytest.mark.parametrize("name", data["test_add"])
    def test_add(self, name):
        r = self.tag.add()
        assert r["errcode"] == 0

    def test_get(self):
        r = self.tag.get(3)
        assert r["errcode"] == 0

    def test_get_api(self):
        r = self.tag.get_api()
        print('-'*50)
        print(r)
        assert r["errcode"] == 0

    def test_delete(self):
        r = self.tag.delete(3)
        assert r["errcode"] == 0