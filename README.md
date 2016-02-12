thumbor-presets
===============

Make [Thumbor](https://github.com/thumbor/thumbor) urls short and sweet by keeping common
sizes and filters in settings.

Ever felt your inner perfectionist crying when looking at the Thumbor urls? Want to nominate Thumbor for the Guinness World Record for having the longest urls in the universe? So did I. Meet thumbor-presets - a tiny add-on to keep your most common sizes, filters and settings right in the Thumbor's config.

Usage
-----

Install this package via PyPi or GitHub:
```sh
pip install thumbor_presets
# or
pip install https://github.com/alexmorozov/thumbor-presets
```
Add your common presets to your Thumbor config file:
```python
# thumbor.conf
PRESETS = {
    'small_thumb': '250x100/smart/filters:grayscale(),watermark(/some/image.jpg)',
}
```
Start a Thumbor instance with a presets-aware app:
```sh
thumbor -a thumbor_presets.app.ThumborServiceApp
```
And you're done! Access your presets the easy way:
````curl
curl http://thumbor_server.com/unsafe/preset/small_thumb/image.jpg
````

Requirements
------------

* thumbor

License
-------

MIT

Authors
-------

`thumbor-presets` was written by [Alex Morozov](mailto:inductor2000@mail.ru).
