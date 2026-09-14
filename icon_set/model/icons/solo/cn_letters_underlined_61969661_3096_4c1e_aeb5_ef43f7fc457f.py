"""Cn Letters Underlined. Retains the identifying silhouette and visible features.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Supplied Cn reference; Lucide type construction inspected earlier informed coherent monoline lettering.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '61969661-3096-4c1e-aeb5-ef43f7fc457f'
SOURCE_PATH = 'pictographic-primitives/symbol/cn (text u)_61969661-3096-4c1e-aeb5-ef43f7fc457f.svg'
AUTHOR = 'gpt-6'


class CnLettersUnderlined(Solo48):
    icon_id = 'cn-letters-underlined'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('cn', 'letters', 'chinese', 'text', 'underline', 'language', 'typography', 'abbreviation')

    def build(self) -> None:
        self.add_arc('c-top', (18, 8), (4, 15), radius_x=14, radius_y=7, sweep=False)
        self.add_line('c-side', (4, 15), (4, 23))
        self.add_arc('c-bottom', (4, 23), (18, 30), radius_x=14, radius_y=7, sweep=False)
        self.add_contour('c', 'c-top', 'c-side', 'c-bottom')
        self.add_polyline('n-stem', (30, 16), (30, 22), (30, 30))
        self.add_arc('n-arch', (30, 22), (44, 22), radius_x=7, radius_y=7, sweep=True)
        self.add_line('n-right', (44, 22), (44, 30))
        self.add_contour('n-bowl', 'n-arch', 'n-right')
        self.relate("connect", 'n-stem', 'n-bowl')
        self.add_line('underline', (4, 40), (44, 40))
