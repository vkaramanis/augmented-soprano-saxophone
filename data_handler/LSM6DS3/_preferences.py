from enum import Enum


class EmbeddedFunctions(Enum):
    Disable = 0x00  # Disable access to embedded functions configuration registers
    Enable = 0x80  # Enable access to embedded functions configuration registers


class FifoODR(Enum):
    DISABLE = 0x00  # FIFO ODR disabled
    R10HZ = 0x08  # FIFO ODR 10Hz
    R25HZ = 0x10  # FIFO ODR 25Hz
    R50HZ = 0x18  # FIFO ODR 50Hz
    R100HZ = 0x20  # FIFO ODR 100Hz
    R200HZ = 0x28  # FIFO ODR 200Hz
    R400HZ = 0x30  # FIFO ODR 400Hz
    R800HZ = 0x38  # FIFO ODR 800Hz
    R1600HZ = 0x40  # FIFO ODR 1600Hz
    R3300HZ = 0x48  # FIFO ODR 3300Hz
    R6600HZ = 0x50  # FIFO ODR 6600Hz


class FifoMode(Enum):
    FPD = 0x00  # FIFO disabled
    FIFO = 0x01  # FIFO mode. Stop collecting data when FIFO is full
    CONTINUOUS = 0x03  # Continuous mode until trigger is deasserted, then FIFO mode
    BYPASS = 0x04  # Bypass mode until trigger is deasserted, then Continuous mode
    OVERWRITE = 0x05  # Continuous mode. If the FIFO is full the new sample overwrite the older one


class AcceleratorODR(Enum):
    RPD = 0x00  # Output Data Rate: Power-down
    R13HZ = 0x10  # Output Data Rate: 13 Hz
    R26HZ = 0x20  # Output Data Rate: 26 Hz
    R52HZ = 0x30  # Output Data Rate: 52 Hz
    R104HZ = 0x40  # Output Data Rate: 104 Hz
    R208HZ = 0x50  # Output Data Rate: 208 Hz
    R416HZ = 0x60  # Output Data Rate: 416 Hz
    R833HZ = 0x70  # Output Data Rate: 833 Hz
    R1K66HZ = 0x80  # Output Data Rate: 1.66 kHz
    R3K33HZ = 0x90  # Output Data Rate: 3.33 kHz
    R6K66HZ = 0xA0  # Output Data Rate: 6.66 kHz


class AcceleratorFS(Enum):
    FS2G = 0x00  # Full scale: +- 2g
    FS4G = 0x08  # Full scale: +- 4g
    FS8G = 0x0C  # Full scale: +- 8g
    FS16G = 0x04  # Full scale: +- 16g


class AcceleratorBW(Enum):
    BW400HZ = 0X00  # Anti-aliasing filter bandwidth: 400hZ
    BW200HZ = 0X01  # Anti-aliasing filter bandwidth: 200hZ
    BW100HZ = 0X02  # Anti-aliasing filter bandwidth: 100hZ
    BW50HZ = 0X03  # Anti-aliasing filter bandwidth: 50hZ


class GyroscopeODR(Enum):
    RPD = 0x00  # Output Data Rate: Power-down
    R13HZ = 0x10  # Output Data Rate: 13 Hz
    R26HZ = 0x20  # Output Data Rate: 26 Hz
    R52HZ = 0x30  # Output Data Rate: 52 Hz
    R104HZ = 0x40  # Output Data Rate: 104 Hz
    R208HZ = 0x50  # Output Data Rate: 208 Hz
    R416HZ = 0x60  # Output Data Rate: 416 Hz
    R833HZ = 0x70  # Output Data Rate: 833 Hz
    R1K66HZ = 0x80  # Output Data Rate: 1.66 kHz


class GyroscopeFS(Enum):
    FS125 = 0x02  # Full scale: 125 dps
    FS245 = 0x00  # Full scale: 250 dps
    FS500 = 0x04  # Full scale: 500 dps
    FS1000 = 0x08  # Full scale: 1000 dps
    FS2000 = 0x0C  # Full scale: 2000 dps
