# OpenRazer Custom Effects

This repository is intended to be a collection of custom scripts used by the maintainer to enhance the implementation of [OpenRazer] and [Polychromatic].

### Hardware
I tested with the following Razer accessories:
* Mouse - Razer Naga Chroma (0053:1532)
* Headset - Razer Kraken Ultimate (0527:1532)
* Mousemat - Razer Goliathus Extended (0C02:1532)
* Keyboard - Razer Ornata Chroma V2 (025D:1532)

### Install

OpenRazer
* I cloned the repository's master branch and [built from source]

Polychromatic
* I cloned the repository's master branch and installed [listed dependencies].

### Custom Effects

I wrote a collection of scripts to be run from the user's systemd to apply custom effects based on screen locking status.

Install: `cd scripts; ./install-screensaver.sh`
Restart: `systemctl restart openrazer-custom-effects`
View status: `systemctl status openrazer-custom-effects`


[OpenRazer repository]: https://github.com/openrazer/openrazer
[Polychromatic repository]: https://github.com/polychromatic/polychromatic
[built from source]: https://github.com/openrazer/openrazer/wiki/Building-a-package#fedora
[listed dependencies]: https://polychromatic.app/docs/dependencies/
