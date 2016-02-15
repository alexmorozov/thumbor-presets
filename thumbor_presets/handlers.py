#--coding: utf8--

import re
import urlparse

from thumbor.url import Url
from thumbor.handlers.imaging import ImagingHandler

import tornado.web


# Stolen from https://github.com/thumbor-community/core/blob/master/tc_core/web.py  # NOQA
class RequestParser(object):

    _url_regex = None

    @classmethod
    def path_to_parameters(cls, path):
        '''
        :param path: url path
        :return: A dictionary of parameters to be used with
                ImagingHandler instances
        '''
        if not cls._url_regex:
            cls._url_regex = re.compile(Url.regex())

        if cls._url_regex.groups:
            match = cls._url_regex.match(path)

            # Pass matched groups to the handler.  Since
            # match.groups() includes both named and
            # unnamed groups, we want to use either groups
            # or groupdict but not both.
            if cls._url_regex.groupindex:
                parameters = dict(
                    (str(k), tornado.web._unquote_or_none(v))
                    for (k, v) in match.groupdict().items())
            else:
                parameters = [
                    tornado.web._unquote_or_none(s)
                    for s in match.groups()
                ]
        else:
            parameters = dict()

        return parameters


class PresetHandler(ImagingHandler):
    def redirect_to_image(self, **kwargs):
        preset_url = self.context.config.PRESETS[kwargs['preset']]
        # TODO: Validate hash
        uri = [
            'unsafe',
            preset_url,
            kwargs['image'],
        ]
        self.request.uri = urlparse.urlparse('/'.join(uri)).path
        options = RequestParser.path_to_parameters(self.request.uri)
        super(PresetHandler, self).get(**options)

    @tornado.web.asynchronous
    def get(self, **kwargs):
        return self.redirect_to_image(**kwargs)

    @tornado.web.asynchronous
    def head(self, **kwargs):
        return self.redirect_to_image(**kwargs)
