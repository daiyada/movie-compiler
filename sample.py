class BaseClass(object):
    def __init__(self):
        self.__param = "I'm BaseClass"
        self._param2 = "yaho"
        self.param3 = "hello"

    @property
    def _param(self):
        return self.__param


class ChildClass(BaseClass):
    def hello(self):
        print(self._param)


if __name__ == "__main__":
    cc = ChildClass()
    cc.hello()
