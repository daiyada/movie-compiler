"""
@file load.py
@brief 特定のファイルを読み取る

@author daiyada / created on 2021/07/21
"""

import yaml


class YamlLoader(object):
    """yamlファイルをロードするクラス"""

    @property
    def getYamlData(self) -> dict:
        return self.__yaml_data

    def __init__(self, path: str) -> None:
        """Constructor"""
        self.__path = path
        self.__loadYaml()

    def __loadYaml(self) -> None:
        try:
            with open(self.__path, mode="r", encoding="utf-8") as f:
                self.__yaml_data = yaml.safe_load(f)
        except Exception as e:
            print("[load_yaml]yamlファイルのロードができませんでした")
            print(e)
