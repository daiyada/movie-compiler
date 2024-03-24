"""
@file   imgs2movie.py
@brief  imgs から 動画を生成する

@author daiyada / created on 2024/03/24
"""
import argparse
import os
from glob import glob
from typing import List

import cv2


def main(img_path_list: List[str], fps: float, output_dir: str, file_name: str, extension: str) -> None:
    """画像から動画を作成する"""
    fourcc = cv2.VideoWriter_fourcc(*'XVID') if extension == 'avi' else cv2.VideoWriter_fourcc(*'mp4v')
    first_image = cv2.imread(img_path_list[0])
    height, width, _ = first_image.shape
    output_path = os.path.join(output_dir, f"{file_name}.{extension}")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    for img_path in img_path_list:
        img = cv2.imread(img_path)
        out.write(img)
    out.release()
    print(f"動画が正常に生成されました: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", "-i", default="./input/imgs")
    parser.add_argument("--output_dir", "-od", default="./output/imgs2movie")
    parser.add_argument("--fps", default=20.0)
    parser.add_argument("--file_name", default="sample")
    parser.add_argument("--extension", default="mp4")
    args = parser.parse_args()

    if not os.path.isdir(args.input_dir):
        raise Exception("Desicgnated input directory is not found.")
    os.makedirs(args.output_dir, exist_ok=True)

    img_path_list = sorted(glob(os.path.join(args.input_dir, "*.jpg"), recursive=True))
    if len(img_path_list) == 0:
        raise Exception("Files are not found in designate input directory path.")

    main(img_path_list, float(args.fps), args.output_dir, args.file_name, args.extension)