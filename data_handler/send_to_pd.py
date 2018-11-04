from os import system
from multiprocessing import Pool
from button_handler import get_data, get_sensor_data
from accel_handler import calc_zero

pool = Pool(processes=4)


def send_to_pd(message=' '):
    system("echo '" + message + "' | pdsend 3000")


while True:
    preset = get_data('PR')
    power = get_data('SP')

    if power != [0, 0, 0, 0]:
        accel_pool = pool.apply_async(calc_zero)
        get_sensor_data(accel_pool.get())

    sensor = get_data('SD')
    send_to_pd('data %i %i %i %i %i %i %i %i %i;' % (
        preset,
        power[0],
        power[1],
        power[2],
        power[3],
        sensor[0],
        sensor[1],
        sensor[2],
        sensor[3]))
    print(calc_zero('YL'))
