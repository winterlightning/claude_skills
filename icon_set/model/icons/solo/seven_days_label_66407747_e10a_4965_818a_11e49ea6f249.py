"""7 Days Label. Uses the conventional d abbreviation for days to preserve duration at native size.

Keyshape HRECT_L: visible extremes (2, 6, 46, 42); centerline extremes (4, 8, 44, 40).
Lucide percent informs diagonal/counter separation; Lucide type informs
coherent monoline letter strokes. Digits and word order retain intentional
asymmetry. All coordinates are authored directly for the live SOLO48 keyshape.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '66407747-e10a-4965-818a-11e49ea6f249'
SOURCE_PATH = 'pictographic-primitives/symbol/7 DAYS_66407747-e10a-4965-818a-11e49ea6f249.svg'
AUTHOR = 'gpt-6'


class SevenDaysLabel(Solo48):
    icon_id = 'seven-days-label'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/labels"
    aliases = ()
    keywords = ('7-days', 'days', 'seven', 'week', 'duration', 'trial', 'label', 'text')

    def build(self) -> None:
        self.add_polyline('seven', (6, 8), (22, 8), (6, 40))
        self.add_arc('day-bowl-top', (32, 22), (42, 22), radius_x=6, radius_y=6, sweep=True)
        self.add_line('day-bowl-right', (42, 22), (42, 34))
        self.add_arc('day-bowl-bottom', (42, 34), (32, 34), radius_x=6, radius_y=6, sweep=True)
        self.add_line('day-bowl-left', (32, 34), (32, 22))
        self.add_contour('day-bowl', 'day-bowl-top', 'day-bowl-right', 'day-bowl-bottom', 'day-bowl-left', closed=True)
        self.add_line('day-ascender', (42, 8), (42, 22))
        self.relate("connect", 'day-bowl', 'day-ascender')
