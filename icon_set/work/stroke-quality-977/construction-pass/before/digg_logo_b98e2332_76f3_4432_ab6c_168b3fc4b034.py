"""Digg logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b98e2332-76f3-4432-ab6c-168b3fc4b034'
SOURCE_PATH = 'pictographic-primitives/logos/digg logo_b98e2332-76f3-4432-ab6c-168b3fc4b034.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class DiggLogo(Solo48):
    icon_id = 'digg-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('digg', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (40, 4), (40, 18))
        self.add_line('e1', (40, 18), (14, 18))
        self.add_line('e2', (8, 21), (8, 40))
        self.add_line('e3', (14, 44), (40, 44))
        self.add_line('e4', (40, 44), (40, 18))
        self.add_arc('e5', (14, 18), (8, 21), radius_x=6, sweep=False)
        self.add_line('e6-1', (8, 40), (10, 43))
        self.add_line('e6-2', (10, 43), (14, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e6-1', 'e6-2', 'e3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
