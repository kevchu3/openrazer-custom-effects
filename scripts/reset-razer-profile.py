#!/usr/bin/python3
import os
import fcntl
import time
import openrazer.client

RAZER_REPORT_LEN = 90

def _ioc(direction, type_val, nr, size):
    return (direction << 30) | (size << 16) | (type_val << 8) | nr

HIDIOCSFEATURE = _ioc(3, 0x48, 0x06, RAZER_REPORT_LEN)
HIDIOCGFEATURE = _ioc(3, 0x48, 0x07, RAZER_REPORT_LEN)

def build_report(command_class, command_id, data_size):
    report = bytearray(RAZER_REPORT_LEN)
    report[1] = 0x1F
    report[5] = data_size
    report[6] = command_class
    report[7] = command_id
    crc = 0
    for i in range(2, 88):
        crc ^= report[i]
    report[88] = crc
    return report

def find_cobra_hidraw():
    devices = []
    try:
        for entry in sorted(os.listdir('/sys/class/hidraw/')):
            try:
                with open(f'/sys/class/hidraw/{entry}/device/uevent') as f:
                    content = f.read().upper()
                if '1532' in content and '00DB' in content:
                    devices.append(f'/dev/{entry}')
            except (FileNotFoundError, PermissionError):
                pass
    except FileNotFoundError:
        pass
    return devices

def query_razer(hidraw_path, command_class, command_id, data_size):
    report = build_report(command_class, command_id, data_size)
    try:
        fd = os.open(hidraw_path, os.O_RDWR | os.O_NONBLOCK)
        try:
            buf = bytearray(report)
            fcntl.ioctl(fd, HIDIOCSFEATURE, buf)
            time.sleep(0.08)
            buf = bytearray(RAZER_REPORT_LEN)
            fcntl.ioctl(fd, HIDIOCGFEATURE, buf)
            return bytes(buf)
        finally:
            os.close(fd)
    except (OSError, IOError):
        return None

def get_battery_info():
    for dev in find_cobra_hidraw():
        resp = query_razer(dev, 0x07, 0x80, 0x02)
        if resp and resp[0] == 0x02:
            pct = resp[9] * 100 // 255
            resp2 = query_razer(dev, 0x07, 0x84, 0x02)
            charging = bool(resp2 and resp2[0] == 0x02 and resp2[9] == 1)
            return pct, charging
    return None, False

def dock_color():
    pct, charging = get_battery_info()
    if charging and pct is not None:
        if pct < 25:
            return (238, 0, 0)
        elif pct < 75:
            return (255, 170, 0)
        return (0, 255, 0)
    return (238, 0, 0)

a = openrazer.client.DeviceManager()
a.turn_off_on_screensaver = False

# Disable daemon effect syncing.
# Without this, the daemon will try to set the lighting effect to every device.
a.sync_effects = False

for device in a.devices:
    # Naga Chroma (1532:0053)
    # Cobra Hyperspeed (waiting for device support)
    if device.type == "mouse":
        device.dpi = (3800,3800)
        device.poll_rate=1000
        device.fx.breath_dual(238, 0, 0, 143, 0, 0)
        device.fx.misc.backlight.breath_dual(238, 0, 0, 143, 0, 0)
        device.fx.misc.scroll_wheel.breath_dual(238, 0, 0, 143, 0, 0)
        device.fx.misc.scroll_wheel.brightness = 75
        device.fx.misc.logo.breath_dual(238, 0, 0, 143, 0, 0)
        device.fx.misc.logo.brightness = 75

    # Kraken Ultimate (1532:0527)
    if device.type == "headset":
        device.fx.breath_dual(238, 0, 0, 143, 0, 0)

    # Ornata Chroma V2 (1532:025D)
    if device.type == "keyboard":
        device.brightness = 75
        device.fx.static(238, 0, 0)

    # Goliathus Extended (1532:0C02)
    if device.type == "mousemat":
        device.brightness = 75
        device.fx.static(238, 0, 0)

    # Mouse Dock Pro (1532:00A4) - battery color if charging, red if not
    if 'Mouse Dock Pro' in device.name:
        r, g, b = dock_color()
        device.brightness = 75
        device.fx.static(r, g, b)

    # Base Station V2 Chroma (1532:0F20)
    if 'Base Station V2' in device.name:
        device.brightness = 75
        device.fx.static(238, 0, 0)
