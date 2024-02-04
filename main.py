import os
import sys
import colorama
from colorama import Fore, Style
from os import path
import matlab, matlab.engine
import numpy as np
import sp_RR.breathe
import matplotlib.pyplot as plt
import cv2
from function.draw_breath import draw_breath
from function.apnea_time import apnea_time, has_apnea

level = ["正常","輕度睡眠呼吸中止症","中度睡眠呼吸中止症", "重度睡眠呼吸中止症"]

# video = "F:\\video\\video\\11_gray.mov"

if __name__ == '__main__':
    if len(sys.argv) < 2:
        # print(f"{Fore.BLUE}Hello World{Style.RESET_ALL}")
        print(f"{Fore.RED}error:{Style.RESET_ALL} no input file")
        exit(0)
    video = sys.argv[1]

    cam = cv2.VideoCapture(video)
    fps = cam.get(cv2.CAP_PROP_FPS)


    rr_rate = sp_RR.breathe.get_breath_data(video)
    rr_rate = np.array(rr_rate)
    # time = list()
    # count = 0
    # for i in range(len(rr_rate)):
    #     time.append(count)
    #     count += 1/fps
    # plt.plot(time, rr_rate)
    # plt.show()

    ans = apnea_time(rr_rate, fps, .5)
    apnea_level = has_apnea(ans, fps)
    print(f"{level[apnea_level]}")
    print(ans)
    draw_breath(rr_rate, fps)
    print("finish")