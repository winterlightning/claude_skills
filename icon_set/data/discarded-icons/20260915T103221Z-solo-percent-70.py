"""70 Percent. Stacks the numeral over the percent sign, preserving the full value and unit.

Keyshape SQUARE: visible extremes (4, 4, 44, 44); centerline extremes (6, 6, 42, 42).
Lucide percent informs diagonal/counter separation; Lucide type informs
coherent monoline letter strokes. Digits and word order retain intentional
asymmetry. All coordinates are authored directly for the live SOLO48 keyshape.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2db006bf-b601-494c-82f0-ad85cdab5beb'
SOURCE_PATH = 'pictographic-primitives/symbol/70 %_2db006bf-b601-494c-82f0-ad85cdab5beb.svg'
AUTHOR = 'gpt-6'


class Percent70(Solo48):
    icon_id = 'percent-70'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/labels"
    aliases = ()
    keywords = ('70%', 'percent', 'seventy', 'discount', 'sale', 'percentage', 'text')

    def build(self) -> None:
        self.add_polyline('tens', (6, 6), (18, 6), (8, 22))
        self.add_arc('zero-top', (28, 13), (42, 13), radius_x=7, radius_y=7, sweep=True)
        self.add_line('zero-right', (42, 13), (42, 15))
        self.add_arc('zero-bottom', (42, 15), (28, 15), radius_x=7, radius_y=7, sweep=True)
        self.add_line('zero-left', (28, 15), (28, 13))
        self.add_contour('zero', 'zero-top', 'zero-right', 'zero-bottom', 'zero-left', closed=True)
        self.add_line('percent-slash', (14, 42), (34, 31))
        self.add_dot('percent-upper-dot', (14, 31))
        self.add_dot('percent-lower-dot', (34, 42))
