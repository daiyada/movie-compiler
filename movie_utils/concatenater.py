"""
@file concatenater.py
@brief 2または4本の動画を連結する

@author daiyada / created on 2021/07/21
"""
import os

import numpy as np

import cv2
from config.cfg_manager import ReadConcatenater
from movie_utils.movie import Movie


class MovieConcatenater(object):
    def __init__(self) -> None:
        self.__config = ReadConcatenater(ReadConcatenater.getYamlPath())
        self.__movie_1 = Movie(self.__config.getInputPath1).getMovie
        self.__movie_2 = Movie(self.__config.getInputPath2).getMovie
        if self.__config.getConcateType:
            self.__movie_3 = Movie(self.__config.getInputPath3).getMovie
            self.__movie_4 = Movie(self.__config.getInputPath4).getMovie
            # HACK: 画像サイズが合わない場合はエラーを出す
            self.__checkMovieResolution()
            self.__setFormat()
            self.__concate4Video()
        else:
            # HACK: 画像サイズが合わない場合はエラーを出す
            self.__checkMovieResolution()
            self.__setFormat()
            self.__concate2Video()

    def __checkMovieResolution(self):
        """画像サイズが合わない場合はエラーを出す"""
        height1 = int(self.__movie_1.get(cv2.CAP_PROP_FRAME_HEIGHT))
        width1 = int(self.__movie_1.get(cv2.CAP_PROP_FRAME_WIDTH))
        height2 = int(self.__movie_2.get(cv2.CAP_PROP_FRAME_HEIGHT))
        width2 = int(self.__movie_2.get(cv2.CAP_PROP_FRAME_WIDTH))
        if self.__config.getConcateType:
            height3 = int(self.__movie_3.get(cv2.CAP_PROP_FRAME_HEIGHT))
            width3 = int(self.__movie_3.get(cv2.CAP_PROP_FRAME_WIDTH))
            height4 = int(self.__movie_4.get(cv2.CAP_PROP_FRAME_HEIGHT))
            width4 = int(self.__movie_4.get(cv2.CAP_PROP_FRAME_WIDTH))
            if not all(
                [
                    height1 == height2,
                    height2 == height3,
                    height3 == height4,
                    height4 == height1,
                ]
            ):
                print("動画の高さ方向のサイズが異なる")
                raise Exception
            if not all(
                [
                    width1 == width2,
                    width2 == width3,
                    width3 == width4,
                    width4 == width1,
                ]
            ):
                print("動画の幅方向のサイズが異なる")
                raise Exception
        else:
            if not (height1 == height2):
                print("動画の高さ方向のサイズが異なる")
                raise Exception
            if not (width1 == width2):
                print("動画の幅方向のサイズが異なる")
                raise Exception

    def __setFormat(self) -> None:
        # Hack: 今はとりあえずmovie_1の設定値をそのまま使うことに
        fourcc = int(self.__movie_1.get(cv2.CAP_PROP_FOURCC))
        fps = int(self.__movie_1.get(cv2.CAP_PROP_FPS))
        height = int(self.__movie_1.get(cv2.CAP_PROP_FRAME_HEIGHT))
        width = int(self.__movie_1.get(cv2.CAP_PROP_FRAME_WIDTH))
        if self.__config.getConcateType:  # 4動画
            img_width = width * 2
            img_height = height * 2
        else:
            if self.__config.getArrangement:  # 2動画横並び
                img_width = width * 2
                img_height = height
            else:  # 2動画縦並び
                img_width = width
                img_height = height * 2
        self.__new_movie = cv2.VideoWriter(
            self.__config.getSavePath, fourcc, fps, (img_width, img_height)
        )

    def __concate2Video(self) -> None:
        while True:
            ret1, img_1 = self.__movie_1.read()
            ret2, img_2 = self.__movie_2.read()
            ret = ret1 and ret2
            if ret:
                concatenater = ImageConcatenater(
                    self.__config.getConcateType, img_1=img_1, img_2=img_2
                )
                self.__new_movie.write(concatenater.getImage)
            else:
                break
        self.__new_movie.release()
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
                concatenater = ImageConcatenater(
                    self.__config.getConcateType,
                    img_1=img_1,
                    img_2=img_2,
                    img_3=img_3,
                    img_4=img_4,
                )
                self.__new_movie.write(concatenater.getImage)
            else:
                break
        self.__new_movie.release()
        self.__movie_1.release()
        self.__movie_2.release()
        self.__movie_3.release()
        self.__movie_4.release()


class ImageConcatenater(object):
    @property
    def getImage(self) -> np.array:
        return self.__img

    def __init__(self, concate_flag, **kwargs) -> None:
        self.__config = ReadConcatenater(ReadConcatenater.getYamlPath())
        self.__img_1 = kwargs["img_1"]
        self.__img_2 = kwargs["img_2"]
        if self.__config.getConcateType:
            self.__img_3 = kwargs["img_3"]
            self.__img_4 = kwargs["img_4"]
            self.__concatenate4Img()
        else:
            self.__concatenate2Img()

    def __concatenate2Img(self) -> None:
        self.__putTitle()
        if self.__config.getArrangement:
            self.__img = cv2.hconcat([self.__img_1, self.__img_2])
        else:
            self.__img = cv2.vconcat([self.__img_1, self.__img_2])

    def __concatenate4Img(self) -> None:
        self.__putTitle()
        if self.__config.getArrangement:
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
            self.__config.getTitle1,
            self.__config.getTitleCoord,
            cv2.FONT_HERSHEY_PLAIN,
            self.__config.getFontSize,
            self.__config.getTitleColor,
            self.__config.getThickness,
            cv2.LINE_AA,
        )
        cv2.putText(
            self.__img_2,
            self.__config.getTitle2,
            self.__config.getTitleCoord,
            cv2.FONT_HERSHEY_PLAIN,
            self.__config.getFontSize,
            self.__config.getTitleColor,
            self.__config.getThickness,
            cv2.LINE_AA,
        )

        if self.__config.getConcateType:
            cv2.putText(
                self.__img_3,
                self.__config.getTitle3,
                self.__config.getTitleCoord,
                cv2.FONT_HERSHEY_PLAIN,
                self.__config.getFontSize,
                self.__config.getTitleColor,
                self.__config.getThickness,
                cv2.LINE_AA,
            )
            cv2.putText(
                self.__img_4,
                self.__config.getTitle4,
                self.__config.getTitleCoord,
                cv2.FONT_HERSHEY_PLAIN,
                self.__config.getFontSize,
                self.__config.getTitleColor,
                self.__config.getThickness,
                cv2.LINE_AA,
            )
