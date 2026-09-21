"""100 Percent. Stacks the numeral over the percent sign, preserving the full value and unit.

Keyshape SQUARE: visible extremes (4, 4, 44, 44); centerline extremes (6, 6, 42, 42).
Lucide percent informs diagonal/counter separation; Lucide type informs
coherent monoline letter strokes. Digits and word order retain intentional
asymmetry. All coordinates are authored directly for the live SOLO48 keyshape.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '16e1f964-eb14-47ea-a749-2f4868526913'
SOURCE_PATH = 'pictographic-primitives/symbol/100% (text)_16e1f964-eb14-47ea-a749-2f4868526913.svg'
AUTHOR = 'gpt-6'


class Percent100(Solo48):
    icon_id = 'percent-100'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/labels"
    aliases = ()
    keywords = ('100%', 'percent', 'hundred', 'full', 'complete', 'percentage', 'number', 'text')

    def build(self) -> None:
        self.add_polyline('one', (6, 9), (8, 6), (8, 20))
        self.add_arc('zero-first-top', (17, 10), (25, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_line('zero-first-right', (25, 10), (25, 16))
        self.add_arc('zero-first-bottom', (25, 16), (17, 16), radius_x=4, radius_y=4, sweep=True)
        self.add_line('zero-first-left', (17, 16), (17, 10))
        self.add_contour('zero-first', 'zero-first-top', 'zero-first-right', 'zero-first-bottom', 'zero-first-left', closed=True)
        self.add_arc('zero-second-top', (34, 10), (42, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_line('zero-second-right', (42, 10), (42, 16))
        self.add_arc('zero-second-bottom', (42, 16), (34, 16), radius_x=4, radius_y=4, sweep=True)
        self.add_line('zero-second-left', (34, 16), (34, 10))
        self.add_contour('zero-second', 'zero-second-top', 'zero-second-right', 'zero-second-bottom', 'zero-second-left', closed=True)
        self.add_line('percent-slash', (14, 42), (34, 31))
        self.add_dot('percent-upper-dot', (14, 31))
        self.add_dot('percent-lower-dot', (34, 42))
