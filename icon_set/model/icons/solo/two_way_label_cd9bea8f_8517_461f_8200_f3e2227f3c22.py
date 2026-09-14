"""2 Way Label. Stacks 2 over WAY; keeps the full wording.

Keyshape HRECT_L: visible extremes (2, 6, 46, 42); centerline extremes (4, 8, 44, 40).
Lucide percent informs diagonal/counter separation; Lucide type informs
coherent monoline letter strokes. Digits and word order retain intentional
asymmetry. All coordinates are authored directly for the live SOLO48 keyshape.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd9bea8f-8517-461f-8200-f3e2227f3c22'
SOURCE_PATH = 'pictographic-primitives/symbol/2 way (text)_cd9bea8f-8517-461f-8200-f3e2227f3c22.svg'
AUTHOR = 'gpt-6'


class TwoWayLabel(Solo48):
    icon_id = 'two-way-label'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/labels"
    aliases = ()
    keywords = ('2-way', 'two-way', 'bidirectional', 'label', 'text', 'exchange', 'traffic', 'two')

    def build(self) -> None:
        self.add_arc('two-head', (18, 14), (30, 14), radius_x=6, radius_y=6, sweep=True)
        self.add_line('two-foot-1', (30, 14), (18, 20))
        self.add_line('two-foot-2', (18, 20), (30, 20))
        self.add_contour('two', 'two-head', 'two-foot-1', 'two-foot-2')
        self.add_polyline('w', (6, 29), (6, 40), (10, 34), (14, 40), (16, 29))
        self.add_polyline('a-arch', (24, 40), (24, 35), (24, 29), (32, 29), (32, 35), (32, 40))
        self.add_line('a-bar', (24, 35), (32, 35))
        self.relate("connect", 'a-arch', 'a-bar')
        self.add_polyline('y-arms', (40, 29), (42, 34), (42, 29))
        self.add_line('y-stem', (42, 34), (42, 40))
        self.relate("connect", 'y-arms', 'y-stem')
