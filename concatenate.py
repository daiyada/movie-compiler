"""
@file concatenate.py
@brief 2または4本の動画を連結する

@author daiyada / created on 2021/07/21
"""
import os

from config.cfg_manager import ReadConcatenater
from movie_utils.concatenater import MovieConcatenater

if __name__ == "__main__":
    MovieConcatenater()
