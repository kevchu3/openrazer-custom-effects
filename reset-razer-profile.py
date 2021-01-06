#!/usr/bin/python3
import openrazer.client
a = openrazer.client.DeviceManager()
a.turn_off_on_screensaver = False

for device in a.devices:
    # mouse profile
    if device.type == "mouse":
        device.dpi = (3000,3000)
        device.poll_rate=1000
        device.fx.breath_dual(238, 0, 0, 143, 0, 0)
        device.fx.misc.scroll_wheel.breath_dual(238, 0, 0, 143, 0, 0)
        device.fx.misc.scroll_wheel.brightness = 75
        device.fx.misc.logo.breath_dual(238, 0, 0, 143, 0, 0)
        device.fx.misc.logo.brightness = 75

    # headset profile
    if device.type == "headset":
        device.fx.breath_dual(238, 0, 0, 143, 0, 0)
    
    if device.type == "keyboard":
        device.brightness = 75
        device.fx.static(238, 0, 0)

    if device.type == "mousemat":
        device.brightness = 75
        device.fx.static(238, 0, 0)

