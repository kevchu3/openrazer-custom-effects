#!/usr/bin/python3
import openrazer.client
a = openrazer.client.DeviceManager()
a.turn_off_on_screensaver = False

# Disable daemon effect syncing.
# Without this, the daemon will try to set the lighting effect to every device.
a.sync_effects = False

for device in a.devices:
    # mouse profile
    if device.type == "mouse":
        device.dpi = (3800,3800)
        device.poll_rate=1000
        device.fx.breath_dual(75, 156, 211, 122, 174, 211)
        device.fx.misc.backlight.breath_single(75, 156, 211)
        device.fx.misc.scroll_wheel.breath_single(75, 156, 211)
        device.fx.misc.scroll_wheel.brightness = 75
        device.fx.misc.logo.breath_single(75, 156, 211)
        device.fx.misc.logo.brightness = 75

    # headset profile
    if device.type == "headset":
        device.fx.breath_dual(75, 156, 211, 122, 174, 211)
    
    if device.type == "keyboard":
        device.brightness = 75
        device.fx.starlight_dual(75, 156, 211, 122, 174, 211, 2) # starlight speed = normal

    if device.type == "mousemat":
        device.brightness = 75
        device.fx.breath_dual(75, 156, 211, 122, 174, 211)

