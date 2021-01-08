#!/bin/bash

# copy scripts
COPYTO=/home/kechung/bin/openrazer-custom-effects/
mkdir -p $COPYTO
cp reset-razer-profile.py $COPYTO
cp screensaver-razer-profile.py $COPYTO
cp run-screensaver.sh $COPYTO

# run script via systemd service unit as yourself
#sudo cp system-local.conf /etc/dbus-1/system-local.conf
mkdir -p ~/.config/systemd/user
cp openrazer-custom-effects.service ~/.config/systemd/user/
systemctl daemon-reload --user
systemctl enable openrazer-custom-effects.service --user
systemctl restart openrazer-custom-effects.service --user
