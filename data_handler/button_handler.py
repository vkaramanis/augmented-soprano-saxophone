import touchphat
from pickle import load, dump
from subprocess import call
from os import getcwd

touchphat.auto_leds = False

page = 0
bank = 0
preset = 0

setting_page = 0

sensor_data = [[0 for c in range(4)] for r in range(16)]
sensor_onoff = [[0 for c in range(4)] for r in range(16)]

cwd = getcwd()

sensor_data_file = cwd + '/Python/presets/sensor_data.pkl'
sensor_onoff_file = cwd + '/Python/presets/sensor_onoff.pkl'

try:
    with open(sensor_data_file, 'rb') as sdi:
        sensor_data = load(sdi)
    with open(sensor_onoff_file, 'rb') as spi:
        sensor_onoff = load(spi)
except:
    print('No Preset files found in ' + cwd)


def get_page(button):
    global page
    if button == 6 and page != -1:
        page = 0
    elif 2 <= button <= 5 and -1 < page < 2:
        page += 1
    elif button == 1 and page > 0:
        page -= 1
    if button == 6 and setting_page == 5:
        page = -1


def get_bank(button):
    global bank
    if page == 0:
        if button == 2:
            bank = 0
        elif button == 3:
            bank = 1
        elif button == 4:
            bank = 2
        elif button == 5:
            bank = 3


def get_preset(button):
    global preset
    if page == 1:
        if bank == 0:
            if button == 2:
                preset = 0
            elif button == 3:
                preset = 1
            elif button == 4:
                preset = 2
            elif button == 5:
                preset = 3
        elif bank == 1:
            if button == 2:
                preset = 4
            elif button == 3:
                preset = 5
            elif button == 4:
                preset = 6
            elif button == 5:
                preset = 7
        elif bank == 2:
            if button == 2:
                preset = 8
            elif button == 3:
                preset = 9
            elif button == 4:
                preset = 10
            elif button == 5:
                preset = 11
        elif bank == 3:
            if button == 2:
                preset = 12
            elif button == 3:
                preset = 13
            elif button == 4:
                preset = 14
            elif button == 5:
                preset = 15


def get_sensor_onoff(button):
    if page == 2:
        if 1 < button < 6:
            if sensor_onoff[preset][button - 2] == 0:
                sensor_onoff[preset][button - 2] = 1
            elif sensor_onoff[preset][button - 2] == 1:
                sensor_onoff[preset][button - 2] = 0


def save_data():
    try:
        with open(sensor_data_file, 'wb') as sdo:
            dump(sensor_data, sdo)
        with open(sensor_onoff_file, 'wb') as spo:
            dump(sensor_onoff, spo)
    except:
        print('No Preset file found')


def reset():
    global sensor_data
    global sensor_onoff

    sensor_data = [[0 for c in range(4)] for r in range(16)]
    sensor_onoff = [[0 for c in range(4)] for r in range(16)]


def shutdown():
    for pad in range(1, 7):
        touchphat.set_led(pad, 0)
    call("sudo shutdown --poweroff now", shell=True)


def get_setting_page(button):
    global setting_page
    global page

    if button == 6 and page == 0:
        setting_page += 1
    else:
        setting_page = 0

    if button != 6 and page == -1:
        if button == 2:
            save_data()
        elif button == 4:
            reset()
        elif button == 5:
            shutdown()
        page = 0
        setting_page = 0


def get_light():
    if page == 0:
        for pad in range(1, 7):
            touchphat.set_led(pad, 0)
        touchphat.set_led('Enter', 1)
        touchphat.set_led(bank + 2, 1)

    elif page == 1:
        for pad in range(1, 7):
            touchphat.set_led(pad, 0)
        touchphat.set_led('Back', 1)
        if bank == 0:
            if preset <= 3:
                touchphat.set_led((preset % 4) + 2, 1)
            else:
                for pad in range(0, 4):
                    touchphat.set_led(pad + 2, 0)
        elif bank == 1:
            if 4 <= preset <= 7:
                touchphat.set_led((preset % 4) + 2, 1)
            else:
                for pad in range(0, 4):
                    touchphat.set_led(pad + 2, 0)
        elif bank == 2:
            if 8 <= preset <= 11:
                touchphat.set_led((preset % 4) + 2, 1)
            else:
                for pad in range(0, 4):
                    touchphat.set_led(pad + 2, 0)
        elif bank == 3:
            if 12 <= preset <= 15:
                touchphat.set_led((preset % 4) + 2, 1)
            else:
                for pad in range(0, 4):
                    touchphat.set_led(pad + 2, 0)
    elif page == 2:
        touchphat.set_led('Back', 1)
        touchphat.set_led('Enter', 1)
        for pad in range(0, 4):
            touchphat.set_led(pad + 2, sensor_onoff[preset][pad])
    elif page == -1:
        for pad in range(1, 7):
            touchphat.set_led(pad, 1)
        touchphat.set_led(6, 0)
        touchphat.set_led(3, 0)


def get_data(op="Pr"):
    if op == "PR":
        return preset
    elif op == "SD":
        return sensor_data[preset]
    elif op == "SP":
        return sensor_onoff[preset]


def get_sensor_data(data):
    for i in range(0, 4):
        if sensor_onoff[preset][i] == 1:
            sensor_data[preset][i] = data


get_light()


@touchphat.on_touch(['Back', 'A', 'B', 'C', 'D', 'Enter'])
def handle_touch(event):
    get_sensor_onoff(event.pad)
    get_preset(event.pad)
    get_bank(event.pad)
    get_page(event.pad)
    get_setting_page(event.pad)

    get_light()
