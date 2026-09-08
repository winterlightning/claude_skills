"""Mirrored delta wing with bowed trailing edge and trapezoidal control frame. No useful Lucide subject match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1af77d24-44c3-4ebd-97a7-9094e5cd4e55'
SOURCE_PATH = 'pictographic-primitives/animals/fly_1af77d24-44c3-4ebd-97a7-9094e5cd4e55.svg'
AUTHOR = 'gpt-6'


class HangGlider(Solo48):
    icon_id = 'hang-glider'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('hang', 'glider')

    def build(self) -> None:
        # Visible keyshape bounds: (0, 6, 48, 42); centerlines inset by 2.
        self.add_line('wing-left', (24, 8), (2, 24))
        self.add_arc('tip-left', (2, 24), (6, 30), radius_x=4, radius_y=6, sweep=False)
        self.add_line('trailing-left', (6, 30), (24, 26))
        self.add_line('trailing-right', (24, 26), (42, 30))
        self.add_arc('tip-right', (42, 30), (46, 24), radius_x=4, radius_y=6, sweep=False)
        self.add_line('wing-right', (46, 24), (24, 8))
        self.add_contour('wing', 'wing-left', 'tip-left', 'trailing-left', 'trailing-right', 'tip-right', 'wing-right')
        self.add_polyline('harness', (16, 29), (19, 40), (29, 40), (32, 29))
        self.relate("connect", 'wing', 'harness')
