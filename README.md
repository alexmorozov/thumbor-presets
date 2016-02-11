thumbor-presets
===============

Make [Thumbor][https://github.com/thumbor/thumbor] urls short and sweet by keeping common
sizes and filters in settings.

Usage
-----

    pip install thumbor thumbor_presets
    thumbor -a thumbor_presets.app.ThumborServiceApp

    :::python
    PRESETS = {
        'small_thumb': '250x100/smart/filters:grayscale(),watermark(/some/image.jpg)',
    }

    http://thumbor_server.com/unsafe/preset/small_thumb/image.jpg

Requirements
------------

* thumbor

License
-------

MIT

Authors
-------

`thumbor-presets` was written by [Alex Morozov](inductor2000@mail.ru).
