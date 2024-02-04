
import matplotlib.pyplot as plt

def draw_breath(rr_rate, fps):
    time = list()
    count = 0
    for i in range(len(rr_rate)):
        time.append(count)
        count += 1/fps

    plt.plot(time, rr_rate, color='blue')
    plt.show()
