"""Ds Letters Underlined. Retains the identifying silhouette and visible features.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Supplied reference; no useful exact Lucide match found.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b2f8456d-0bd5-418c-8cb5-8aa61117c3f2'
SOURCE_PATH = 'pictographic-primitives/symbol/ds (text u)_b2f8456d-0bd5-418c-8cb5-8aa61117c3f2.svg'
AUTHOR = 'gpt-6'


class DsLettersUnderlined(Solo48):
    icon_id = 'ds-letters-underlined'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('ds', 'letters', 'text', 'underline', 'typography', 'abbreviation', 'language')

    def build(self) -> None:
        self.add_arc('d-curve', (4, 8), (4, 30), radius_x=14, radius_y=11, sweep=True)
        self.add_line('d-back', (4, 30), (4, 8))
        self.add_contour('d', 'd-curve', 'd-back', closed=True)
        self.add_line('s-top', (44, 14), (37, 14))
        self.add_arc('s-upper', (37, 14), (37, 22), radius_x=7, radius_y=4, sweep=False)
        self.add_arc('s-lower', (37, 22), (37, 30), radius_x=7, radius_y=4, sweep=True)
        self.add_line('s-foot', (37, 30), (30, 30))
        self.add_contour('s', 's-top', 's-upper', 's-lower', 's-foot')
        self.add_line('underline', (4, 40), (44, 40))
