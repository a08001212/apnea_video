def apnea_time(rr_rate, fps, threshold):
    apnea_count = 0
    count = 0
    start = 0
    end = 0
    ans = list()
    for i in range(len(rr_rate)-1):
        if (rr_rate[i] > threshold or rr_rate[i] < -threshold):
            count = 0
            apnea_time = (end-start)/ fps
            if(apnea_time >=10):
                ans.append([start/fps, apnea_time])
                apnea_count += 1
            start = i
            end = i
        else:
            end = i
    print(f"apnea {apnea_count} times")
    return ans

def has_apnea(apnea_time, fps):
    count_time = 0
    start = 0
    count = 0
    max_apnea_time = 0
    for i in range(len(apnea_time)):
        while start<len(apnea_time) and apnea_time[i][0] - apnea_time[start][0] >= 3600:
            start += 1
            count_time -= 1
        count_time += 1
        max_apnea_time = max(max_apnea_time, count_time)

    if max_apnea_time <5:
        return 0
    elif max_apnea_time <15:
        return 1
    elif max_apnea_time <30:
        return 2
    else:
        return 3