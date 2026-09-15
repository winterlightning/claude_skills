"""Forrst logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7cdc0286-dd4b-4add-9459-dc9c81da2cec'
SOURCE_PATH = 'pictographic-primitives/logos/forrst logo_7cdc0286-dd4b-4add-9459-dc9c81da2cec.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ForrstLogo(Solo48):
    icon_id = 'forrst-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('forrst', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (24, 26), (24, 44))
        self.add_line('e1', (20, 30), (24, 35))
        self.add_line('e2', (24, 4), (40, 39))
        self.add_line('e3', (39, 39), (9, 39))
        self.add_line('e4', (8, 39), (24, 4))
        self.add_arc('e5', (40, 39), (39, 39), radius_x=39)
        self.add_arc('e6', (9, 39), (8, 39), radius_x=20, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e5', 'e3', 'e6', 'e4', closed=True)
        self.relate('connect', 'c1', 'c0')
