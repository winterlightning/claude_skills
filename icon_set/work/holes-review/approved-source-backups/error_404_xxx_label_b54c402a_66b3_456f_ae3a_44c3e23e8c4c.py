"""404 Error Label. Preserves the reference characters; reconstructs their stroke geometry.

Keyshape HRECT_L: visible extremes (2, 6, 46, 42); centerline extremes (4, 8, 44, 40).
Lucide percent informs diagonal/counter separation; Lucide type informs
coherent monoline letter strokes. Digits and word order retain intentional
asymmetry. All coordinates are authored directly for the live SOLO48 keyshape.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b54c402a-66b3-456f-ae3a-44c3e23e8c4c'
SOURCE_PATH = 'pictographic-primitives/symbol/404 XXX_b54c402a-66b3-456f-ae3a-44c3e23e8c4c.svg'
AUTHOR = 'gpt-6'


class Error404XxxLabel(Solo48):
    icon_id = 'error-404-xxx-label'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/labels"
    aliases = ()
    keywords = ('404', 'error', 'not-found', 'xxx', 'web', 'page', 'label', 'text')

    def build(self) -> None:
        self.add_polyline('four-left-arm', (8, 8), (6, 16), (10, 16))
        self.add_polyline('four-left-stem', (10, 8), (10, 16), (10, 20))
        self.relate("connect", 'four-left-arm', 'four-left-stem')
        self.add_arc('zero-top', (19, 12), (27, 12), radius_x=4, radius_y=4, sweep=True)
        self.add_line('zero-right', (27, 12), (27, 16))
        self.add_arc('zero-bottom', (27, 16), (19, 16), radius_x=4, radius_y=4, sweep=True)
        self.add_line('zero-left', (19, 16), (19, 12))
        self.add_contour('zero', 'zero-top', 'zero-right', 'zero-bottom', 'zero-left', closed=True)
        self.add_polyline('four-right-arm', (42, 8), (36, 16), (42, 16))
        self.add_polyline('four-right-stem', (42, 8), (42, 16), (42, 20))
        self.relate("connect", 'four-right-arm', 'four-right-stem')
        self.add_polyline('cross-0-down', (6, 29), (8, 34), (12, 40))
        self.add_polyline('cross-0-up', (6, 40), (8, 34), (12, 29))
        self.relate("connect", 'cross-0-down', 'cross-0-up')
        self.add_polyline('cross-1-down', (20, 29), (24, 34), (28, 40))
        self.add_polyline('cross-1-up', (20, 40), (24, 34), (28, 29))
        self.relate("connect", 'cross-1-down', 'cross-1-up')
        self.add_polyline('cross-2-down', (36, 29), (40, 34), (42, 40))
        self.add_polyline('cross-2-up', (36, 40), (40, 34), (42, 29))
        self.relate("connect", 'cross-2-down', 'cross-2-up')
