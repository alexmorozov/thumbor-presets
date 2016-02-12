thumbor-presets
===============

Make [Thumbor](https://github.com/thumbor/thumbor) urls short and sweet by keeping common
sizes and filters in settings.

Usage
-----

* Install this package via PyPi or GitHub:

        pip install thumbor_presets
        pip install https://github.com/alexmorozov/thumbor-presets
* Add your common presets to your Thumbor config file:

        # thumbor.conf
        PRESETS = {
            'small_thumb': '250x100/smart/filters:grayscale(),watermark(/some/image.jpg)',
        }
* Start a Thumbor instance with a presets-aware app:

        thumbor -a thumbor_presets.app.ThumborServiceApp

And you're done! Access your presets the easy way:

    curl http://thumbor_server.com/unsafe/preset/small_thumb/image.jpg

Requirements
------------

* thumbor

License
-------

MIT

Authors
-------

`thumbor-presets` was written by [Alex Morozov](mailto:inductor2000@mail.ru).
