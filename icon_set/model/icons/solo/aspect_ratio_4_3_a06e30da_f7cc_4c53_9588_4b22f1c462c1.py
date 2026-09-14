"""4:3 Aspect Ratio. Preserves the reference characters; reconstructs their stroke geometry.

Keyshape HRECT_L: visible extremes (2, 6, 46, 42); centerline extremes (4, 8, 44, 40).
Lucide percent informs diagonal/counter separation; Lucide type informs
coherent monoline letter strokes. Digits and word order retain intentional
asymmetry. All coordinates are authored directly for the live SOLO48 keyshape.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a06e30da-f7cc-4c53-9588-4b22f1c462c1'
SOURCE_PATH = 'pictographic-primitives/symbol/4-3 (text)_a06e30da-f7cc-4c53-9588-4b22f1c462c1.svg'
AUTHOR = 'gpt-6'


class AspectRatio43(Solo48):
    icon_id = 'aspect-ratio-4-3'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/labels"
    aliases = ()
    keywords = ('aspect-ratio', '4:3', 'ratio', 'screen', 'format', 'video', 'display', 'text')

    def build(self) -> None:
        self.add_polyline('four-arm', (12, 8), (6, 29), (14, 29))
        self.add_polyline('four-stem', (14, 8), (14, 29), (14, 40))
        self.relate("connect", 'four-arm', 'four-stem')
        self.add_dot('colon-top', (24, 17))
        self.add_dot('colon-bottom', (24, 31))
        self.add_line('three-top', (34, 8), (36, 8))
        self.add_arc('three-upper', (36, 8), (36, 24), radius_x=8, radius_y=8, sweep=True)
        self.add_line('three-in', (36, 24), (39, 24))
        self.add_line('three-out', (39, 24), (36, 24))
        self.add_arc('three-lower', (36, 24), (36, 40), radius_x=8, radius_y=8, sweep=True)
        self.add_line('three-bottom', (36, 40), (34, 40))
        self.add_contour('three', 'three-top', 'three-upper', 'three-in', 'three-out', 'three-lower', 'three-bottom')
