#!/bin/bash

# this will run as UID 1000; change if using another user
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"
export DISPLAY=":1"
dbus-monitor --session "type='signal',interface='org.gnome.ScreenSaver'" | \
( while true
    do read X
    if echo $X | grep "boolean true" &> /dev/null; then
        /usr/bin/python /home/kechung/bin/openrazer-custom-effects/screensaver-razer-profile.py
    elif echo $X | grep "boolean false" &> /dev/null; then
        /usr/bin/python /home/kechung/bin/openrazer-custom-effects/reset-razer-profile.py
    fi
    done )

