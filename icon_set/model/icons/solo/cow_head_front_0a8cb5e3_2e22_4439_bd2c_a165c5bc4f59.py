"""Cow Head. Retains the identifying silhouette and visible features.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Supplied reference; no useful exact Lucide match found.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a8cb5e3-2e22-4439-bd2c-a165c5bc4f59'
SOURCE_PATH = 'pictographic-primitives/symbol/bull head_0a8cb5e3-2e22-4439-bd2c-a165c5bc4f59.svg'
AUTHOR = 'gpt-6'


class CowHeadFront(Solo48):
    icon_id = 'cow-head-front'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('cow', 'bull', 'head', 'cattle', 'farm', 'animal', 'beef', 'dairy')

    def build(self) -> None:
        self.add_line('forehead-1', (14, 14), (24, 12))
        self.add_line('forehead-2', (24, 12), (34, 14))
        self.add_line('face-right', (34, 14), (32, 36))
        self.add_arc('chin-right', (32, 36), (26, 42), radius_x=6, radius_y=6, sweep=True)
        self.add_line('chin', (26, 42), (22, 42))
        self.add_arc('chin-left', (22, 42), (16, 36), radius_x=6, radius_y=6, sweep=True)
        self.add_line('face-left', (16, 36), (14, 14))
        self.add_contour('face', 'forehead-1', 'forehead-2', 'face-right', 'chin-right', 'chin', 'chin-left', 'face-left', closed=True)
        self.add_polyline('ear-left', (14, 14), (6, 24), (15, 28))
        self.add_polyline('ear-right', (34, 14), (42, 24), (33, 28))
        self.relate("connect", 'face', 'ear-left')
        self.relate("connect", 'face', 'ear-right')
        self.add_arc('horn-left', (8, 6), (14, 14), radius_x=10, radius_y=10, sweep=False)
        self.add_arc('horn-right', (34, 14), (40, 6), radius_x=10, radius_y=10, sweep=False)
        self.relate("connect", 'face', 'horn-left')
        self.relate("connect", 'face', 'horn-right')
        self.relate("connect", 'ear-left', 'horn-left')
        self.relate("connect", 'ear-right', 'horn-right')
