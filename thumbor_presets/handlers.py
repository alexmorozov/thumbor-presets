#--coding: utf8--

from thumbor.handlers import ContextHandler

import tornado.web
import tornado.httpserver


class PresetHandler(ContextHandler):
    def redirect_to_image(self, **kwargs):
        preset_url = self.context.config.PRESETS[kwargs['preset']]
        # TODO: Validate hash
        uri = [
            'unsafe',
            preset_url,
            kwargs['image'],
        ]
        self.application(tornado.httpserver.HTTPRequest(
            method=self.request.method,
            uri='/'.join(uri),
            version=self.request.version,
            headers=self.request.headers,
            connection=self.request.connection))

    @tornado.web.asynchronous
    def get(self, **kwargs):
        return self.redirect_to_image(**kwargs)

    @tornado.web.asynchronous
    def head(self, **kwargs):
        return self.redirect_to_image(**kwargs)
