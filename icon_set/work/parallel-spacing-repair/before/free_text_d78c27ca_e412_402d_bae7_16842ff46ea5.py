"""The word FREE is written in rounded monoline capitals. VRECT_L extremes (8,6)-(40,42). Reflow FR above EE to preserve all four letters at 48px rather than crowd the R bowl. No useful local Lucide text match; use shared eight-unit bar spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd78c27ca-e412-402d-bae7-16842ff46ea5'
SOURCE_PATH = 'pictographic-primitives/symbol/free (text)_d78c27ca-e412-402d-bae7-16842ff46ea5.svg'
AUTHOR = 'gpt-6'


class FreeText(Solo48):
    icon_id = 'free-text'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('free', 'label', 'no-cost', 'offer', 'promotion', 'badge', 'text', 'gratis')

    def build(self) -> None:
        # Row-major FREE preserves all four letters with legal 8-unit bar spacing.
        self.add_polyline('f', (16,6), (8,6), (8,12), (8,19))
        self.add_line('f-middle', (8,12), (16,12))
        self.relate('connect', 'f', 'f-middle')
        self.add_line('r-left-top-1', (32,19), (32,12))
        self.add_line('r-left-top-2', (32,12), (32,6))
        self.add_line('r-left-top-3', (32,6), (38,6))
        self.add_arc('r-round-top', (38,6), (40,6), radius_x=2)
        self.add_line('r-right', (40,6), (40,10))
        self.add_arc('r-round-bottom', (40,10), (38,12), radius_x=2)
        self.add_line('r-bowl-bottom', (38,12), (32,12))
        self.add_contour('r', 'r-left-top-1', 'r-left-top-2', 'r-left-top-3', 'r-round-top', 'r-right', 'r-round-bottom', 'r-bowl-bottom')
        self.add_line('r-leg', (32,12), (40,19))
        self.relate('connect', 'r', 'r-leg')
        for i,x in enumerate((8,32)):
            self.add_polyline(f'e-{i}', (x+8,28), (x,28), (x,36), (x,44), (x+8,44))
            self.add_line(f'e-{i}-middle', (x,36), (x+8,36))
            self.relate('connect', f'e-{i}', f'e-{i}-middle')
