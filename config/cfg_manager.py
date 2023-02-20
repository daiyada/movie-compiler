"""
@file cfg_manager.py
@brief config/*.yamlファイルの設定値を読み取る

@author daiyada / created on 2021/07/21
"""
import os

from inout.load import YamlLoader


class ReadCutter(object):
    PATH = os.path.join(os.getcwd(), "config", "cut.yaml")

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


class ReadConcatenater(object):
    PATH = os.path.join(os.getcwd(), "config", "concatenate.yaml")

    @classmethod
    def getYamlPath(cls) -> str:
        return cls.PATH

    @property
    def getConcateType(self) -> bool:
        return self.__concate_type

    @property
    def getArrangement(self) -> bool:
        return self.__arrangement

    @property
    def getInputPath1(self) -> str:
        return self.__input_path_1

    @property
    def getInputPath2(self) -> str:
        return self.__input_path_2

    @property
    def getInputPath3(self) -> str:
        return self.__input_path_3

    @property
    def getInputPath4(self) -> str:
        return self.__input_path_4

    @property
    def getSavePath(self) -> str:
        return self.__save_path

    @property
    def getTitle1(self) -> str:
        return self.__title_1

    @property
    def getTitle2(self) -> str:
        return self.__title_2

    @property
    def getTitle3(self) -> str:
        return self.__title_3

    @property
    def getTitle4(self) -> str:
        return self.__title_4

    @property
    def getTitleColor(self) -> tuple:
        return self.__title_color

    @property
    def getTitleCoord(self) -> tuple:
        return self.__title_coord

    @property
    def getFontSize(self) -> float:
        return self.__font_size

    @property
    def getThickness(self) -> int:
        return self.__thickness

    def __init__(self, path) -> None:
        """Constructor"""
        self.__load = YamlLoader(path)
        self.__yaml_data = self.__load.getYamlData
        self.__deserialize()

    def __makeSavePath(self) -> None:
        file_name = self.__yaml_data["output"]["file_name"]
        ext = self.__yaml_data["output"]["ext"]
        output_dir = self.__yaml_data["output"]["dir"]
        os.makedirs(output_dir, exist_ok=True)
        self.__save_path = os.path.join(output_dir, "{}.{}".format(file_name, ext))

    def __checkPath(self) -> None:
        if not bool(self.__input_path_1) or not bool(self.__input_path_2):
            print("[ERROR]画像パス1, 2が未入力")
            raise Exception
        if self.__concate_type:  # 4動画合体の場合は3,4のパスが入力されていないとエラーをはく
            if not bool(self.__input_path_3) or bool(not self.__input_path_4):
                print("[ERROR]画像パス1, 2が未入力")
                raise Exception

    def __deserialize(self) -> None:
        self.__concate_type = bool(self.__yaml_data["concate_type"])
        self.__arrangement = bool(self.__yaml_data["arrangement"])
        self.__input_path_1 = self.__yaml_data["input"]["path_1"]
        self.__input_path_2 = self.__yaml_data["input"]["path_2"]
        self.__input_path_3 = self.__yaml_data["input"]["path_3"]
        self.__input_path_4 = self.__yaml_data["input"]["path_4"]
        self.__title_1 = self.__yaml_data["output"]["title_1"]
        self.__title_2 = self.__yaml_data["output"]["title_2"]
        self.__title_3 = self.__yaml_data["output"]["title_3"]
        self.__title_4 = self.__yaml_data["output"]["title_4"]
        self.__title_color = tuple(self.__yaml_data["output"]["color"])
        self.__title_coord = tuple(self.__yaml_data["output"]["coordination"])
        self.__font_size = float(self.__yaml_data["output"]["fontsize"])
        self.__thickness = int(self.__yaml_data["output"]["thickness"])
        self.__makeSavePath()
        self.__checkPath()
