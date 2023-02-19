"""
@file adjust_fps.py
@brief 解像度を調整する

@author Shunsuke Hishida / created on 2023/02/15
@explanation
- 1920 x 1080 ( 16 : 9 ) ( Full-HD / 元動画 )
- 1280 x  720 ( 16 : 9 ) ( HDTV )
-  720 x  480 ( 16 : 9 ) ( SDTV )
-  480 x  270 ( 16 : 9 ) ( WQVGA )
"""
import argparse
import os

import cv2


def main(cap: cv2.VideoCapture, file_name: str, target_width: int, target_height: int) -> None:
    writer = cv2.VideoWriter(
        f"./areso_{target_width}_{target_height}_{file_name}", cv2.VideoWriter_fourcc("m", "p", "4", "v"), 
        int(cap.get(cv2.CAP_PROP_FPS)), 
        (target_width, target_height)
    )

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        resized_frame = cv2.resize(frame, dsize=(target_width, target_height))
        writer.write(resized_frame)
        if cv2.waitKey(10) == 5:
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_path", type=str, help="Input movie path")
    parser.add_argument("-w", "--width", type=int, help="Target width of frame")
    parser.add_argument("-h", "--height", type=int, help="Height width of frame")
    args = parser.parse_args()

    cap = cv2.VideoCapture(args.input_path)
    main(cap, os.path.basename(args.input_path, args.width, args.height))