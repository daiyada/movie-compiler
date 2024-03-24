"""
@file   change_movie_extension.py
@brief  imgs から 動画を生成する

@author daiyada / created on 2024/03/24
"""
import argparse
import os

import cv2


def main(input_file_path: str, output_dir, extension: str) -> None:
    file_name, _ = os.path.splitext(os.path.basename(input_file_path))
    output_path = os.path.join(output_dir, f"{file_name}.{extension}")
    cap = cv2.VideoCapture(input_file_path)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'XVID') if extension == 'avi' else cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
    cap.release()
    out.release()

    print('変換完了')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file_path", "-i")
    parser.add_argument("--output_dir", "-od", default="./output/change_movie_extension")
    parser.add_argument("--extension", default="mp4")
    args = parser.parse_args()

    if not os.path.isfile(args.input_file_path):
        raise FileNotFoundError("Designated file is not found.")
    os.makedirs(args.output_dir, exist_ok=True)

    main(args.input_file_path, args.output_dir, args.extension)