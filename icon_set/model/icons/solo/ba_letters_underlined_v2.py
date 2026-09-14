# Review candidate; original preserved.
"""Ba Letters Underlined. Retains the identifying silhouette and visible features.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Lucide type, inspected earlier: coherent monoline lettering.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a29d1bb4-f540-4abf-8aa9-a7c5843a6984'
SOURCE_PATH = 'pictographic-primitives/symbol/ba (text u)_a29d1bb4-f540-4abf-8aa9-a7c5843a6984.svg'
AUTHOR = 'gpt-6'

class BaLettersUnderlinedVariant2(Solo48):
    icon_id = 'ba-letters-underlined-v2'
    variant_of = 'ba-letters-underlined'
    variant_label = 'Roomier openings — pending review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbols/standalone'
    aliases = ()
    keywords = ('ba', 'letters', 'text', 'underline', 'language', 'typography', 'abbreviation')

    def build(self) -> None:
        """Opening repair: Moved the lowercase a stem to the bowl tangent, eliminating the narrow overlapping sliver."""
        self.add_line('b-top', (6, 8), (12, 8))
        self.add_arc('b-upper', (12, 8), (12, 18), radius_x=8, radius_y=5, sweep=True)
        self.add_arc('b-lower', (12, 18), (12, 30), radius_x=10, radius_y=6, sweep=True)
        self.add_line('b-back-1', (12, 30), (6, 30))
        self.add_line('b-back-2', (6, 30), (6, 18))
        self.add_line('b-back-3', (6, 18), (6, 8))
        self.add_contour('b', 'b-top', 'b-upper', 'b-lower', 'b-back-1', 'b-back-2', 'b-back-3', closed=True)
        self.add_line('b-bar', (6, 18), (12, 18))
        self.relate('connect', 'b', 'b-bar')
        self.add_line('underline', (6, 40), (42, 40))
        self.add_arc('a-top', (44, 24), (38, 18), radius_x=6, sweep=False)
        self.add_arc('a-left', (38, 18), (38, 30), radius_x=6, sweep=False)
        self.add_arc('a-bottom', (38, 30), (44, 24), radius_x=6, sweep=False)
        self.add_contour('a-bowl', 'a-top', 'a-left', 'a-bottom', closed=True)
        self.add_polyline('a-stem', (44, 18), (44, 24), (44, 30))
        self.relate('connect', 'a-bowl', 'a-stem')
