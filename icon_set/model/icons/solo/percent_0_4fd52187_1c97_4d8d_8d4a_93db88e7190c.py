"""Zero Percent. Preserves the reference characters; reconstructs their stroke geometry.

Keyshape HRECT_L: visible extremes (2, 6, 46, 42); centerline extremes (4, 8, 44, 40).
Lucide percent informs diagonal/counter separation; Lucide type informs
coherent monoline letter strokes. Digits and word order retain intentional
asymmetry. All coordinates are authored directly for the live SOLO48 keyshape.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fd52187-1c97-4d8d-8d4a-93db88e7190c'
SOURCE_PATH = 'pictographic-primitives/symbol/0%_4fd52187-1c97-4d8d-8d4a-93db88e7190c.svg'
AUTHOR = 'gpt-6'


class Percent0(Solo48):
    icon_id = 'percent-0'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/labels"
    aliases = ()
    keywords = ('zero', 'percent', '0%', 'percentage', 'number', 'discount', 'rate', 'none')

    def build(self) -> None:
        self.add_arc('zero-top', (6, 14), (16, 14), radius_x=6, radius_y=6, sweep=True)
        self.add_line('zero-right', (16, 14), (16, 34))
        self.add_arc('zero-bottom', (16, 34), (6, 34), radius_x=6, radius_y=6, sweep=True)
        self.add_line('zero-left', (6, 34), (6, 14))
        self.add_contour('zero', 'zero-top', 'zero-right', 'zero-bottom', 'zero-left', closed=True)
        self.add_line('percent-slash', (26, 40), (42, 8))
        self.add_dot('percent-upper-dot', (26, 8))
        self.add_dot('percent-lower-dot', (42, 40))
