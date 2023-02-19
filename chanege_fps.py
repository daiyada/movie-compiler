"""
@file adjust_fps.py
@brief フレームレートを調整する

@author Shunsuke Hishida / created on 2023/02/15
"""
import argparse
import os

import cv2

def main(cap: cv2.VideoCapture, file_name: str, fps: int) -> None:
    writer = cv2.VideoWriter(
        f"./{fps}fps_{file_name}", cv2.VideoWriter_fourcc("m", "p", "4", "v"), 
        int(fps), 
        (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    )
    current_fps = int(round(cap.get(cv2.CAP_PROP_FPS), 0))
    write_per = int(current_fps / fps)
    index = 1
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if index % write_per != 0:
            index += 1
            continue
        writer.write(frame)
        index += 1
        if cv2.waitKey(10) == 5:
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_path", type=str, help="Input movie path")
    parser.add_argument("-f", "--fps", type=int, help="Input target fps")
    args = parser.parse_args()

    # 編集する動画のパス
    cap = cv2.VideoCapture(args.input_path)
    main(cap, os.path.basename(args.input_path, args.fps))