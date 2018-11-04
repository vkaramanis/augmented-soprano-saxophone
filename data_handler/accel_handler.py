"""

Read sensor data with and scale it from 0 to 1,
Everything above 15000  acts as 1.
All negative numbers acts as 0.

"""
from LSM6DS3 import *
from math import sqrt

activate_accel()


def calc_zero(axis='XL'):
    if 0 <= read_accel(axis) <= 15500:
        return sqrt(abs((read_accel(axis) / 15000.) - 1))
    elif read_accel(axis) > 15500.:
        return 0.
    elif read_accel(axis) < 0.:
        return 1.
    else:
        return 0.
