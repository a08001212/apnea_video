import os
import sys
from colorama import Fore, Style
import numpy as np
import sp_RR.breathe
import cv2
from function.draw_breath import draw_breath
from function.apnea_time import apnea_time, has_apnea
from function.output_log import output_log
level = ["正常","輕度睡眠呼吸中止症","中度睡眠呼吸中止症", "重度睡眠呼吸中止症"]
level_color = [Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Fore.RED]
# video = "F:\\video\\video\\11_gray.mov"

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"{Fore.RED}error:{Style.RESET_ALL} no input file")
        exit(0)
    video = sys.argv[1]


    cam = cv2.VideoCapture(video)
    fps = cam.get(cv2.CAP_PROP_FPS)


    rr_rate = sp_RR.breathe.get_breath_data(video)
    rr_rate = np.array(rr_rate)


    ans = apnea_time(rr_rate, fps, .5)
    apnea_level = has_apnea(ans, fps)
    print(f"{level_color[apnea_level]}{level[apnea_level]}{Style.RESET_ALL}")

    print(ans)
    if len(sys.argv) < 3:
        output_log(ans)
    elif sys.argv[2] != "--no_log":
        output_log(ans, sys.argv[2])
    draw_breath(rr_rate, fps)
