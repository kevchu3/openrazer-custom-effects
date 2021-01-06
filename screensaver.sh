#!/bin/bash

dbus-monitor --session "type='signal',interface='org.gnome.ScreenSaver'" | \
( while true
    do read X
    if echo $X | grep "boolean true" &> /dev/null; then
        python3 screensaver-razer-profile.py
    elif echo $X | grep "boolean false" &> /dev/null; then
        python3 reset-razer-profile.py
    fi
    done )

