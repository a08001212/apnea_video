import matlab
import matlab.engine
import os

def get_breath_data(filename: str):
    path = os.getcwd()
    os.chdir(f'{path}\sp_RR')

    eng = matlab.engine.start_matlab()
    rr_rate = eng.superpixel_rr(filename)
    os.chdir(path)
    return rr_rate

