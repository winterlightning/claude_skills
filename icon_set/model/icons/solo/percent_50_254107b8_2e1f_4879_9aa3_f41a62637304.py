"""50 Percent. Stacks the numeral over the percent sign, preserving the full value and unit.

Keyshape SQUARE: visible extremes (4, 4, 44, 44); centerline extremes (6, 6, 42, 42).
Lucide percent informs diagonal/counter separation; Lucide type informs
coherent monoline letter strokes. Digits and word order retain intentional
asymmetry. All coordinates are authored directly for the live SOLO48 keyshape.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '254107b8-2e1f-4879-9aa3-f41a62637304'
SOURCE_PATH = 'pictographic-primitives/symbol/50 %_254107b8-2e1f-4879-9aa3-f41a62637304.svg'
AUTHOR = 'gpt-6'


class Percent50(Solo48):
    icon_id = 'percent-50'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/labels"
    aliases = ()
    keywords = ('50%', 'percent', 'fifty', 'half', 'discount', 'sale', 'percentage', 'text')

    def build(self) -> None:
        self.add_line('tens-cap-1', (18, 6), (6, 6))
        self.add_line('tens-cap-2', (6, 6), (6, 14))
        self.add_line('tens-cap-3', (6, 14), (14, 14))
        self.add_arc('tens-bowl', (14, 14), (14, 22), radius_x=4, radius_y=4, sweep=True)
        self.add_line('tens-foot', (14, 22), (6, 22))
        self.add_contour('tens', 'tens-cap-1', 'tens-cap-2', 'tens-cap-3', 'tens-bowl', 'tens-foot')
        self.add_arc('zero-top', (28, 13), (42, 13), radius_x=7, radius_y=7, sweep=True)
        self.add_line('zero-right', (42, 13), (42, 15))
        self.add_arc('zero-bottom', (42, 15), (28, 15), radius_x=7, radius_y=7, sweep=True)
        self.add_line('zero-left', (28, 15), (28, 13))
        self.add_contour('zero', 'zero-top', 'zero-right', 'zero-bottom', 'zero-left', closed=True)
        self.add_line('percent-slash', (14, 42), (34, 31))
        self.add_dot('percent-upper-dot', (14, 31))
        self.add_dot('percent-lower-dot', (34, 42))
