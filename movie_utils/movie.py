"""
@file movie.py
@brief 動画ファイルを読み込む

@author daiyada / created on 2021/07/21
"""
import cv2


class Movie(object):
    @property
    def getMovie(self) -> object:
        return self.__movie

    @property
    def getFourcc(self) -> int:
        return int(self.__movie.get(cv2.CAP_PROP_FOURCC))

    @property
    def getFps(self) -> int:
        return int(self.__movie.get(cv2.CAP_PROP_FPS))

    @property
    def getWidth(self) -> int:
        return int(self.__movie.get(cv2.CAP_PROP_FRAME_WIDTH))

    @property
    def getHeight(self) -> int:
        return int(self.__movie.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def __init__(self, path) -> None:
        """Constructor"""
        self.__movie = cv2.VideoCapture(path)
