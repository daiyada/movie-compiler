"""
@file cfg_manager.py
@brief config/*.yamlファイルの設定値を読み取る

@author daiyada / created on 2021/07/21
"""
import os

from inout.load import YamlLoader


class ReadCutter(object):
    PATH = os.path.join(os.getcwd(), "config", "cutter.yaml")

    @classmethod
    def getYamlPath(cls):
        return cls.PATH

    @property
    def getStartTime(self):
        return self.__start_time

    @property
    def getEndTime(self):
        return self.__end_time

    @property
    def getInputPath(self):
        return self.__input_path

    @property
    def getOutputDir(self):
        return self.__output_dir

    def __init__(self, path):
        """Constructor"""
        load = YamlLoader(path)
        self.__yaml_data = load.getYamlData
        self.__deserialize()

    def __checkInputPath(self) -> None:
        if not os.path.isfile(self.__input_path):
            print("input_pathに記載のファイルはありません")
            raise FileNotFoundError

    def __deserialize(self):
        self.__start_time = int(self.__yaml_data["start_time"])
        self.__end_time = int(self.__yaml_data["end_time"]) - 1
        self.__input_path = str(self.__yaml_data["input_path"])
        self.__output_dir = str(self.__yaml_data["output_dir"])
        self.__checkInputPath()
