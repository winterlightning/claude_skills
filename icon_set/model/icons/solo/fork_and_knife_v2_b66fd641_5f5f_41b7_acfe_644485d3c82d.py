"""Cutlery: equal 8-unit tine spacing, smooth fork bowl and a clear 8-unit knife blade."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b66fd641-5f5f-41b7-acfe-644485d3c82d'
SOURCE_PATH = 'pictographic-primitives/symbol/fork and knife_b66fd641-5f5f-41b7-acfe-644485d3c82d.svg'
AUTHOR = 'gpt-6'

class ForkAndKnifeVariant2(Solo48):
    icon_id = 'fork-and-knife-v2'
    variant_of = 'fork-and-knife'
    variant_label = 'Shared ink reconstruction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('fork', 'and', 'knife', 'symbol')

    def build(self):
        """Centerline review: preserve the silhouette; remove duplicated ink and split real attachments into shared nodes."""
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx, radius_y=rx if ry is None else ry, sweep=sweep)
        l('fork-left', (6, 6), (6, 18))
        a('fork-bottom-left', (6, 18), (14, 26), 8, sweep=False)
        a('fork-bottom-right', (14, 26), (22, 18), 8, sweep=False)
        l('fork-right', (22, 18), (22, 6))
        self.add_contour('fork', 'fork-left', 'fork-bottom-left', 'fork-bottom-right', 'fork-right')
        l('middle-tine', (14, 6), (14, 26))
        l('fork-handle', (14, 26), (14, 42))
        link('connect', 'middle-tine', 'fork')
        link('connect', 'fork-handle', 'fork')
        link('connect', 'middle-tine', 'fork-handle')
        p('knife', (34, 42), (34, 6), (42, 22), (42, 30), (34, 30))
