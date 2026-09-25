"""Devicon logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '338407cf-8252-40de-9f7e-dedf013d599c'
SOURCE_PATH = 'pictographic-primitives/logos/devicon logo_338407cf-8252-40de-9f7e-dedf013d599c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class DeviconLogo(Solo48):
    icon_id = 'devicon-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('devicon', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (17, 9), (4, 24))
        self.add_line('e1', (4, 24), (18, 40))
        self.add_line('e2', (20, 39), (30, 8))
        self.add_line('e3', (30, 8), (44, 23))
        self.add_line('e4', (44, 25), (31, 40))
        self.add_arc('e5-1', (18, 40), (19, 40), radius_x=21)
        self.add_arc('e5-2', (19, 40), (20, 39), radius_x=1, sweep=False)
        self.add_arc('e6', (44, 23), (44, 25), radius_x=29, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e5-1', 'e5-2', 'e2', 'e3', 'e6', 'e4')
