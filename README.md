# OpenRazer Custom Effects

This repository is intended to be a collection of custom scripts used by the maintainer to enhance the implementation of [OpenRazer] and [Polychromatic].

### Hardware
I have the following Razer accessories:
* Mouse - Razer Naga Chroma (0053:1532)
* Headset - Razer Kraken Ultimate (0527:1532)

### Install

OpenRazer
* I cloned the [effect_storage branch] and [built from source]

Polychromatic
* I cloned the [dev-1.0.0 branch] and manually applied the file deltas for [openrazer-effects-storage-patch.sh]

### Custom Effects

I applied custom effects with this command: `python reset-razer-profile.py`


[OpenRazer]: https://github.com/openrazer/openrazer
[Polychromatic]: https://github.com/polychromatic/polychromatic
[effect_storage branch]: https://github.com/openrazer/openrazer/tree/effect_storage
[built from source]: https://github.com/openrazer/openrazer/wiki/Building-a-package#fedora
[dev-1.0.0 branch]: https://github.com/polychromatic/polychromatic/tree/dev-1.0.0
[openrazer-effects-storage-patch.sh]: ./openrazer-effects-storage-patch.sh
