'Cutlery: equal 8-unit tine spacing, smooth fork bowl and a clear 8-unit knife blade.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b66fd641-5f5f-41b7-acfe-644485d3c82d'
SOURCE_PATH = 'icons-json/symbol/fork and knife_b66fd641-5f5f-41b7-acfe-644485d3c82d.json'
AUTHOR = 'gpt-6'

class ForkAndKnife(Solo48):
    icon_id = 'fork-and-knife'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('fork', 'and', 'knife', 'symbol')

    def build(self):
        # Cutlery: equal 8-unit tine spacing, smooth fork bowl and a clear 8-unit knife blade.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        l('fork-left',(6,6),(6,18))
        a('fork-bottom',(6,18),(22,18),8,sweep=False)
        l('fork-right',(22,18),(22,6))
        self.add_contour('fork','fork-left','fork-bottom','fork-right')
        l('middle-tine',(14,6),(14,26))
        l('fork-handle',(14,26),(14,42))
        link('connect','middle-tine','fork')
        link('connect','fork-handle','fork')
        link('connect','middle-tine','fork-handle')
        p('knife',(34,42),(34,6),(42,22),(42,30),(34,30))
