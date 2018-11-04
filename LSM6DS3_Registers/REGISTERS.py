from enum import Enum


class Master(Enum):
    ADDRESS = 0x6A  # I2C Module Address
    FUNC_CFG = 0x01  # Enable embedded functions register (r/w)
    SENSOR_SYNC = 0x04  # Sensor synchronization time frame register (r/w)
    MASTER_CONFIG = 0x1A  # Angular rate sensor sign and orientation register (r/w)
    ORIENT_CFG_G = 0x0B
    WHO_AM_I = 0x0F
    STATUS_REG = 0x1E


class Fifo(Enum):
    CTRL01 = 0x06
    CTRL02 = 0x07
    CTRL03 = 0x08
    CTRL04 = 0x09
    ODR = 0x0A  # FIFO ODR and Mode selection

    STATUS01 = 0x3A
    STATUS02 = 0x3B
    STATUS03 = 0x3C
    STATUS04 = 0x3D

    DATA_OUT_L = 0x3E
    DATA_OUT_H = 0x3F


class Control(Enum):
    INT1_CTRL = 0x0D
    INT2_CTRL = 0x0E

    CTRL03 = 0x12
    CTRL04 = 0x13
    CTRL05 = 0x14
    CTRL06 = 0x15
    CTRL07 = 0x16
    CTRL08 = 0x17
    CTRL09 = 0x18
    CTRL10 = 0x19


class Interrupt(Enum):
    WAKE_UP_SRC = 0x1B
    WAKE_UP_THS = 0x5B
    WAKE_UP_DUR = 0x5C

    D6D_SRC = 0x1D

    FUNC_SRC = 0x53

    TAP_SRC = 0x1C
    TAP_CFG = 0x58
    TAP_THS_6D = 0x59

    INT_DUR2 = 0x5A
    FREE_FALL = 0x5D
    MD1_CFG = 0x5E
    MD2_CFG = 0x5F


class Acceleration(Enum):
    CTRL = 0x10  # Linear acceleration sensor control register

    OUT_X_L = 0x28
    OUT_X_H = 0x29
    OUT_Y_L = 0x2A
    OUT_Y_H = 0x2B
    OUT_Z_L = 0x2C
    OUT_Z_H = 0x2D


class Gyroscope(Enum):
    CTRL = 0x11  # Angular rate sensor control register

    OUT_X_L = 0x22
    OUT_X_H = 0x23
    OUT_Y_L = 0x24
    OUT_Y_H = 0x25
    OUT_Z_L = 0x26
    OUT_Z_H = 0x27


class Temperature(Enum):
    OUT_L = 0x20
    OUT_H = 0x21


class SensorHub(Enum):
    HUB01 = 0x2E
    HUB02 = 0x2F
    HUB03 = 0x30
    HUB04 = 0x31
    HUB05 = 0x32
    HUB06 = 0x33
    HUB07 = 0x34
    HUB08 = 0x35
    HUB09 = 0x36
    HUB10 = 0x37
    HUB11 = 0x38
    HUB12 = 0x39
    HUB13 = 0x4D
    HUB14 = 0x4E
    HUB15 = 0x4F
    HUB16 = 0x50
    HUB17 = 0x51
    HUB18 = 0x52


class Timestamp(Enum):
    TIMESTAMP0 = 0x40
    TIMESTAMP1 = 0x41
    TIMESTAMP2 = 0x42


class StepCounter(Enum):
    TIMESTAMP_OUT_L = 0x49
    TIMESTAMP_OUT_H = 0x4A

    COUNTER_OUT_L = 0x4B
    COUNTER_OUT_H = 0x4C


class Magnitude(Enum):
    OUT_X_L = 0x66
    OUT_X_H = 0x67
    OUT_Y_L = 0x68
    OUT_Y_H = 0x69
    OUT_Z_L = 0x6A
    OUT_Z_H = 0x6B
