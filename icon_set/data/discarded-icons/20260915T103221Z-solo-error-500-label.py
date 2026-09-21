"""500 Error Label. Keeps the exact 500 server error code; drops the redundant ERROR caption, which cannot fit legibly.

Keyshape HRECT_L: visible extremes (2, 6, 46, 42); centerline extremes (4, 8, 44, 40).
Lucide percent informs diagonal/counter separation; Lucide type informs
coherent monoline letter strokes. Digits and word order retain intentional
asymmetry. All coordinates are authored directly for the live SOLO48 keyshape.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef5df59f-84d6-4816-b3bd-f093f78b50f4'
SOURCE_PATH = 'pictographic-primitives/symbol/500 ERROR_ef5df59f-84d6-4816-b3bd-f093f78b50f4.svg'
AUTHOR = 'gpt-6'


class Error500Label(Solo48):
    icon_id = 'error-500-label'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/labels"
    aliases = ()
    keywords = ('500', 'error', 'server-error', 'web', 'failure', 'label', 'text', 'status')

    def build(self) -> None:
        self.add_line('five-cap-1', (10, 8), (4, 8))
        self.add_line('five-cap-2', (4, 8), (4, 24))
        self.add_line('five-cap-3', (4, 24), (7, 24))
        self.add_arc('five-bowl', (7, 24), (7, 40), radius_x=3, radius_y=8, sweep=True)
        self.add_line('five-foot', (7, 40), (4, 40))
        self.add_contour('five', 'five-cap-1', 'five-cap-2', 'five-cap-3', 'five-bowl', 'five-foot')
        self.add_arc('zero-first-top', (19, 12), (27, 12), radius_x=4, radius_y=4, sweep=True)
        self.add_line('zero-first-right', (27, 12), (27, 36))
        self.add_arc('zero-first-bottom', (27, 36), (19, 36), radius_x=4, radius_y=4, sweep=True)
        self.add_line('zero-first-left', (19, 36), (19, 12))
        self.add_contour('zero-first', 'zero-first-top', 'zero-first-right', 'zero-first-bottom', 'zero-first-left', closed=True)
        self.add_arc('zero-second-top', (36, 12), (44, 12), radius_x=4, radius_y=4, sweep=True)
        self.add_line('zero-second-right', (44, 12), (44, 36))
        self.add_arc('zero-second-bottom', (44, 36), (36, 36), radius_x=4, radius_y=4, sweep=True)
        self.add_line('zero-second-left', (36, 36), (36, 12))
        self.add_contour('zero-second', 'zero-second-top', 'zero-second-right', 'zero-second-bottom', 'zero-second-left', closed=True)
