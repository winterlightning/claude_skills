'Pound note: straight symmetric border and a simple legible currency stroke.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a52b466-8e1b-412a-aaa1-cea9d33e173c'
SOURCE_PATH = 'icons-json/money/currency pound bill_7a52b466-8e1b-412a-aaa1-cea9d33e173c.json'
AUTHOR = 'gpt-6'

class CurrencyPoundBill(Solo48):
    icon_id = 'currency-pound-bill'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('currency', 'pound', 'bill', 'money')

    def build(self):
        # Pound note: straight symmetric border and a simple legible currency stroke.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('bill',(8,8),(40,8),(44,18),(44,30),(40,40),(8,40),(4,30),(4,18),(8,8))
        p('pound',(29,17),(26,16),(22,19),(22,32),(29,32))
        l('bar',(18,24),(28,24))
        link('connect','pound','bar')
