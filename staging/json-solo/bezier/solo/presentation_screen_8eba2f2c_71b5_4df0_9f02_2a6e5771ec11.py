"""Presentation screen (office), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8eba2f2c-71b5-4df0-9f02-2a6e5771ec11'
SOURCE_PATH = 'icons-json/office/presentation screen_8eba2f2c-71b5-4df0-9f02-2a6e5771ec11.json'
AUTHOR = 'json_to_solo'

class PresentationScreenOffice(Solo48):
    icon_id = 'presentation-screen-office'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('presentation', 'screen', 'office')

    def build(self):
        self.add_line('sym-e0', (4, 21), (44, 21))
        self.add_line('sym-e1', (44, 21), (44, 36))
        self.add_bezier('sym-e2', (44, 36), ((44, 37.88), (41.718, 40), (40, 40)))
        self.add_line('sym-e3', (40, 40), (24, 40))
        self.add_line('sym-e4', (24, 40), (8, 40))
        self.add_bezier('sym-e5', (8, 40), ((6.282, 40), (4, 37.88), (4, 36)))
        self.add_line('sym-e6', (4, 36), (4, 21))
        self.add_line('sym-e7', (4, 21), (4, 12))
        self.add_bezier('sym-e8', (4, 12), ((4, 10.31), (6.464, 8), (8, 8)))
        self.add_line('sym-e9', (8, 8), (24, 8))
        self.add_line('sym-e10', (24, 8), (40, 8))
        self.add_bezier('sym-e11', (40, 8), ((41.536, 8), (44, 10.31), (44, 12)))
        self.add_line('sym-e12', (44, 12), (44, 21))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
