"""Number 45. Preserves the reference characters; reconstructs their stroke geometry.

Keyshape HRECT_L: visible extremes (2, 6, 46, 42); centerline extremes (4, 8, 44, 40).
Lucide percent informs diagonal/counter separation; Lucide type informs
coherent monoline letter strokes. Digits and word order retain intentional
asymmetry. All coordinates are authored directly for the live SOLO48 keyshape.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9a389b9c-8800-4ddb-a7b5-00af44020677'
SOURCE_PATH = 'pictographic-primitives/symbol/45_9a389b9c-8800-4ddb-a7b5-00af44020677.svg'
AUTHOR = 'gpt-6'


class Number45(Solo48):
    icon_id = 'number-45'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/labels"
    aliases = ()
    keywords = ('45', 'number', 'forty-five', 'numeral', 'digits', 'count', 'text')

    def build(self) -> None:
        self.add_polyline('four-arm', (18, 8), (4, 29), (20, 29))
        self.add_polyline('four-stem', (20, 8), (20, 29), (20, 40))
        self.relate("connect", 'four-arm', 'four-stem')
        self.add_line('five-cap-1', (42, 8), (30, 8))
        self.add_line('five-cap-2', (30, 8), (30, 24))
        self.add_line('five-cap-3', (30, 24), (37, 24))
        self.add_arc('five-bowl', (37, 24), (37, 40), radius_x=7, radius_y=8, sweep=True)
        self.add_line('five-foot', (37, 40), (30, 40))
        self.add_contour('five', 'five-cap-1', 'five-cap-2', 'five-cap-3', 'five-bowl', 'five-foot')
