"""
@file concatenater.py
@brief 2または4本の動画を連結する

@author daiyada / created on 2021/07/21
"""
import os

import cv2
from config.cfg_manager import ReadConcatenater
from movie_utils.movie import Movie


class MovieConcatenater(object):
    @property
    def getConfig(self) -> dict:
        return self.__config

    @property
    def getMovie1(self) -> object:
        return self.__movie_1

    @property
    def getMovie2(self) -> object:
        return self.__movie_2

    @property
    def getMovie3(self) -> object:
        return self.__movie_3

    @property
    def getMovie4(self) -> object:
        return self.__movie_4

    def __init__(self):
        self.__config = ReadConcatenater(ReadConcatenater.getYamlPath())
        self.__movie_1 = Movie(self.__config.getInputPath1).getMovie
        self.__movie_2 = Movie(self.__config.getInputPath1).getMovie
        if self.__config.getConcateType:
            self.__movie_3 = Movie(self.__config.getInputPath3).getMovie
            self.__movie_4 = Movie(self.__config.getInputPath4).getMovie
            SetMovieFormat()
            self.__concate4Video()
        else:
            SetMovieFormat()
            self.__concate2Video()

    def __setFormat(self):
        fourcc = int(movie.get(cv2.CAP_PROP_FOURCC))
        fps = int(movie.get(cv2.CAP_PROP_FPS))
        height, width, _ = img.shape
        new_movie = cv2.VideoWriter(save_path, fourcc, fps, (width, height))
        return new_movie

    def __concate2Video(self):
        while True:
            ret1, img1 = self.__movie_1.read()
            ret2, img2 = self.__movie_2.read()
            ret = ret1 and ret2
            if ret:
                ImageConcatenater(img_1=img_1, img_2=img_2)
            else:
                break
        concatenated_2movie.release()
        self.__movie_1.release()
        self.__movie_2.release()

    def __concate4Video(self):
        while True:
            ret1, img_1 = self.__movie_1.read()
            ret2, img_2 = self.__movie_2.read()
            ret3, img_3 = self.__movie_3.read()
            ret4, img_4 = self.__movie_4.read()
            ret = ret1 and ret2 and ret3 and ret4
            if ret:
                ImageConcatenater(img_1=img_1, img_2=img_2, img_3=img_3, img_4=img_4)
                concatenated_2movie.write(img)
            else:
                break
        concatenated_4movie.release()
        movie1.release()
        movie2.release()
        movie3.release()
        movie4.release()


class ImageConcatenater(object):
    def __init__(self, **kwargs):
        self.__img_1 = kwargs["img_1"]
        self.__img_2 = kwargs["img_2"]
        if self.getconfig.getConcateType:
            self.__img_3 = kwargs["img_3"]
            self.__img_4 = kwargs["img_4"]
            self.__concatenate4Img()
        else:
            self.__concatenate2Img()

    def __concatenate2Img():
        self.__putTitle()
        if self.getConfig.getArrangement:
            self.__img = cv2.hconcat([self.__img_1, self.__img_2])
        else:
            self.__img = cv2.vconcat([self.__img_1, self.__img_2])

    def __concatenate4Img():
        self.__putTitle()
        if self.__arangement:
            img_h1 = cv2.hconcat([self.__img_1, self.__img_2])
            img_h2 = cv2.hconcat([self.__img_3, self.__img_4])
            self.__img = cv2.vconcat([img_h1, img_h2])
        else:
            img_v1 = cv2.vconcat([self.__img_1, self.__img_2])
            img_v2 = cv2.vconcat([self.__img_3, self.__img_4])
            self.__img = cv2.hconcat([img_v1, img_v2])

    def __putTitle(self) -> None:
        cv2.putText(
            self.__img_1,
            self.getconfig.getTitle1,
            self.getconfig.getTitleCoord,
            cv2.FONT_HERSHEY_PLAIN,
            self.getconfig.getFontSize,
            self.getconfig.getTitleColor,
            self.getconfig.getThickness,
            cv2.LINE_AA,
        )
        cv2.putText(
            self.__img_2,
            self.getconfig.getTitle2,
            self.getconfig.getTitleCoord,
            cv2.FONT_HERSHEY_PLAIN,
            self.getconfig.getFontSize,
            self.getconfig.getTitleColor,
            self.getconfig.getThickness,
            cv2.LINE_AA,
        )

        if self.getconfig.getConcateType:
            cv2.putText(
                self.__img_3,
                self.getconfig.getTitle3,
                self.getconfig.getTitleCoord,
                cv2.FONT_HERSHEY_PLAIN,
                self.getconfig.getFontSize,
                self.getconfig.getTitleColor,
                self.getconfig.getThickness,
                cv2.LINE_AA,
            )
            cv2.putText(
                self.__img_4,
                self.getconfig.getTitle4,
                self.getconfig.getTitleCoord,
                cv2.FONT_HERSHEY_PLAIN,
                self.getconfig.getFontSize,
                self.getconfig.getTitleColor,
                self.getconfig.getThickness,
                cv2.LINE_AA,
            )


class SetMovieFormat(MovieConcatenater):
    def __init__(self):
        """Constructor"""
        super().__init__()
        print(self.getMovie1)
        input()
