#!/bin/bash

# Update these files to add persistent storage
# https://github.com/openrazer/openrazer/pull/1149/files

cd ~/Git/openrazer
git checkout effect_storage
sudo cp ~/Git/openrazer/daemon/openrazer_daemon/daemon.py /usr/lib/python3.8/site-packages/openrazer_daemon/daemon.py
sudo cp ~/Git/openrazer/daemon/openrazer_daemon/dbus_services/dbus_methods/bw2013.py /usr/lib/python3.8/site-packages/openrazer_daemon/dbus_services/dbus_methods/bw2013.py
sudo cp ~/Git/openrazer/daemon/openrazer_daemon/dbus_services/dbus_methods/chroma_keyboard.py /usr/lib/python3.8/site-packages/openrazer_daemon/dbus_services/dbus_methods/chroma_keyboard.py
sudo cp ~/Git/openrazer/daemon/openrazer_daemon/dbus_services/dbus_methods/deathadder_chroma.py /usr/lib/python3.8/site-packages/openrazer_daemon/dbus_services/dbus_methods/deathadder_chroma.py
sudo cp ~/Git/openrazer/daemon/openrazer_daemon/dbus_services/dbus_methods/kraken.py /usr/lib/python3.8/site-packages/openrazer_daemon/dbus_services/dbus_methods/kraken.py
sudo cp ~/Git/openrazer/daemon/openrazer_daemon/dbus_services/dbus_methods/lanceheadte.py /usr/lib/python3.8/site-packages/openrazer_daemon/dbus_services/dbus_methods/lanceheadte.py
sudo cp ~/Git/openrazer/daemon/openrazer_daemon/dbus_services/dbus_methods/mamba.py /usr/lib/python3.8/site-packages/openrazer_daemon/dbus_services/dbus_methods/mamba.py
sudo cp ~/Git/openrazer/daemon/openrazer_daemon/dbus_services/dbus_methods/nagahexv2.py /usr/lib/python3.8/site-packages/openrazer_daemon/dbus_services/dbus_methods/nagahexv2.py
sudo cp ~/Git/openrazer/daemon/openrazer_daemon/hardware/device_base.py /usr/lib/python3.8/site-packages/openrazer_daemon/hardware/device_base.py
sudo cp ~/Git/openrazer/daemon/openrazer_daemon/hardware/headsets.py /usr/lib/python3.8/site-packages/openrazer_daemon/hardware/headsets.py
sudo cp ~/Git/openrazer/daemon/openrazer_daemon/hardware/keyboards.py /usr/lib/python3.8/site-packages/openrazer_daemon/hardware/keyboards.py
sudo cp ~/Git/openrazer/daemon/openrazer_daemon/hardware/mouse.py /usr/lib/python3.8/site-packages/openrazer_daemon/hardware/mouse.py
sudo cp ~/Git/openrazer/daemon/openrazer_daemon/misc/autosave_persistence.py /usr/lib/python3.8/site-packages/openrazer_daemon/misc/autosave_persistence.py
sudo cp ~/Git/openrazer/pylib/openrazer/client/fx.py /usr/lib/python3.8/site-packages/openrazer/client/fx.py
sudo cp ~/Git/openrazer/pylib/openrazer/client/devices/__init__.py /usr/lib/python3.8/site-packages/openrazer/client/devices/__init__.py


# Update these files to add support for Razer Kraken Ultimate
# https://github.com/openrazer/openrazer/commit/64eccf4446d8169cd2816a64484136d4e8659a24

# /usr/lib/python3.8/site-packages/openrazer_daemon/hardware/headsets.py
# /usr/lib/udev/rules.d/99-razer.rules

