# encoding: utf-8


class Test(object):

    def test_01(self):
        print('This is test01')

    def test_02(self):
        print("This is test02")

    def test_03(self):
        print('This is test03')


if __name__ == "__main__":
    t = Test()
    t.test_01()
    t.test_02()
    t.test_03()
