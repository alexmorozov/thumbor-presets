#--coding: utf8--

from thumbor.app import ThumborServiceApp as StockApp
from thumbor.url import Url

from thumbor_presets.handlers import PresetHandler


class ThumborServiceApp(StockApp):
    def get_handlers(self):
        reg = [
            '/',
            Url.unsafe_or_hash,
            r'preset/',
            r'(?P<preset>[\w\-_]+)/',
            Url.image,
        ]
        handlers = [
            (''.join(reg), PresetHandler, {'context': self.context}),
        ]
        handlers.extend(super(ThumborServiceApp, self).get_handlers())
        return handlers
