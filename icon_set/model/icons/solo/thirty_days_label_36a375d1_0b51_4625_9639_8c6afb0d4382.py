"""30 Days Label. Uses the conventional d abbreviation for days to preserve duration at native size.

Keyshape SQUARE: visible extremes (4, 4, 44, 44); centerline extremes (6, 6, 42, 42).
Lucide percent informs diagonal/counter separation; Lucide type informs
coherent monoline letter strokes. Digits and word order retain intentional
asymmetry. All coordinates are authored directly for the live SOLO48 keyshape.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '36a375d1-0b51-4625-9639-8c6afb0d4382'
SOURCE_PATH = 'pictographic-primitives/symbol/30day (text)_36a375d1-0b51-4625-9639-8c6afb0d4382.svg'
AUTHOR = 'gpt-6'


class ThirtyDaysLabel(Solo48):
    icon_id = 'thirty-days-label'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/labels"
    aliases = ()
    keywords = ('30-days', 'days', 'thirty', 'month', 'duration', 'trial', 'label', 'text')

    def build(self) -> None:
        self.add_line('three-top', (6, 6), (14, 6))
        self.add_arc('three-upper', (14, 6), (14, 14), radius_x=4, radius_y=4, sweep=True)
        self.add_line('three-in', (14, 14), (12, 14))
        self.add_line('three-out', (12, 14), (14, 14))
        self.add_arc('three-lower', (14, 14), (14, 22), radius_x=4, radius_y=4, sweep=True)
        self.add_line('three-bottom', (14, 22), (6, 22))
        self.add_contour('three', 'three-top', 'three-upper', 'three-in', 'three-out', 'three-lower', 'three-bottom')
        self.add_arc('zero-top', (28, 13), (42, 13), radius_x=7, radius_y=7, sweep=True)
        self.add_line('zero-right', (42, 13), (42, 15))
        self.add_arc('zero-bottom', (42, 15), (28, 15), radius_x=7, radius_y=7, sweep=True)
        self.add_line('zero-left', (28, 15), (28, 13))
        self.add_contour('zero', 'zero-top', 'zero-right', 'zero-bottom', 'zero-left', closed=True)
        self.add_line('day-top', (18, 31), (24, 31))
        self.add_arc('day-ne', (24, 31), (30, 37), radius_x=6, radius_y=6, sweep=True)
        self.add_line('day-right', (30, 37), (30, 36))
        self.add_arc('day-se', (30, 36), (24, 42), radius_x=6, radius_y=6, sweep=True)
        self.add_line('day-left-1', (24, 42), (18, 42))
        self.add_line('day-left-2', (18, 42), (18, 31))
        self.add_contour('day', 'day-top', 'day-ne', 'day-right', 'day-se', 'day-left-1', 'day-left-2', closed=True)
