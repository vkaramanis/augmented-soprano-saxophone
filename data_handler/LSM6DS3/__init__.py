from Adafruit_GPIO import I2C
from _registers import Master, Acceleration, Gyroscope, Temperature
from _preferencies import AcceleratorFS, AcceleratorBW, AcceleratorODR, GyroscopeFS, GyroscopeODR

address = Master.ADDRESS.value
i2c = I2C.get_i2c_device(address)


def activate_accel(odr=AcceleratorODR.R416HZ, fs=AcceleratorFS.FS2G, bw=AcceleratorBW.BW200HZ):
    accelReg = Acceleration.CTRL.value
    word = odr.value | fs.value | bw.value
    i2c.write8(accelReg, word)


def activate_gyro(odr=GyroscopeODR.R416HZ, fs=GyroscopeFS.FS500):
    gyroReg = Gyroscope.CTRL.value
    word = odr.value | fs.value
    i2c.write8(gyroReg, word)


def read_accel(a='XL'):
    axis = {
        'XL': Acceleration.OUT_X_L.value,
        'YL': Acceleration.OUT_Y_L.value,
        'ZL': Acceleration.OUT_Z_L.value,
        'XH': Acceleration.OUT_X_H.value,
        'YH': Acceleration.OUT_Y_H.value,
        'ZH': Acceleration.OUT_Z_H.value
    }
    return i2c.readS16(axis[a])


def read_gyro(a='XL'):
    axis = {
        'XL': Gyroscope.OUT_X_L.value,
        'YL': Gyroscope.OUT_Y_L.value,
        'ZL': Gyroscope.OUT_Z_L.value,
        'XH': Gyroscope.OUT_X_H.value,
        'YH': Gyroscope.OUT_Y_H.value,
        'ZH': Gyroscope.OUT_Z_H.value
    }
    return i2c.readS16(axis[a])


def read_temp(hl='L'):
    if hl == 'H':
        return i2c.readS16(Temperature.OUT_H.value)
    else:
        return i2c.readS16(Temperature.OUT_L.value)
