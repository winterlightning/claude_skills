"""Bi Letters Underlined. Retains the identifying silhouette and visible features.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Lucide type, inspected earlier: coherent monoline lettering.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04a52c71-feec-4186-81a0-ab91725525c5'
SOURCE_PATH = 'pictographic-primitives/symbol/bi (text u)_04a52c71-feec-4186-81a0-ab91725525c5.svg'
AUTHOR = 'gpt-6'


class BiLettersUnderlined(Solo48):
    icon_id = 'bi-letters-underlined'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('bi', 'letters', 'text', 'underline', 'language', 'typography', 'abbreviation')

    def build(self) -> None:
        self.add_line('b-top', (4, 8), (14, 8))
        self.add_arc('b-upper', (14, 8), (14, 18), radius_x=10, radius_y=5, sweep=True)
        self.add_arc('b-lower', (14, 18), (14, 30), radius_x=12, radius_y=6, sweep=True)
        self.add_line('b-back-1', (14, 30), (4, 30))
        self.add_line('b-back-2', (4, 30), (4, 18))
        self.add_line('b-back-3', (4, 18), (4, 8))
        self.add_contour('b', 'b-top', 'b-upper', 'b-lower', 'b-back-1', 'b-back-2', 'b-back-3', closed=True)
        self.add_line('b-bar', (4, 18), (14, 18))
        self.relate("connect", 'b', 'b-bar')
        self.add_dot('i-dot', (40, 12))
        self.add_line('i-stem', (40, 22), (40, 30))
        self.add_line('underline', (4, 40), (44, 40))
