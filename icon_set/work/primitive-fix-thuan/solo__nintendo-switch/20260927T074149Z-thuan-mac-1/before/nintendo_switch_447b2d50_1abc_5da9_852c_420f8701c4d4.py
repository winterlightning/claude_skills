"""Nintendo switch (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '447b2d50-1abc-5da9-852c-420f8701c4d4'
SOURCE_PATH = 'pictographic-primitives/video-games/nintendo switch_447b2d50-1abc-5da9-852c-420f8701c4d4.svg'
AUTHOR = 'gpt-6'

class NintendoSwitch(Solo48):
    icon_id = 'nintendo-switch'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('nintendo', 'switch', 'video-games')

    def build(self):
        self.add_line('sym-e0', (13, 8), (13, 40))
        self.add_line('sym-e1', (13, 40), (35, 40))
        self.add_line('sym-e3', (35, 40), (35, 8))
        self.add_line('sym-e4', (35, 8), (9, 8))
        self.add_arc('sym-e7', (9, 8), (4, 15), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('sym-e8', (4, 15), (4, 33))
        self.add_arc('sym-e10', (4, 33), (9, 40), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('sym-e11', (9, 40), (13, 40))
        self.add_line('sym-e12', (35, 40), (39, 40))
        self.add_arc('sym-e13', (39, 40), (44, 33), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('sym-e14', (44, 33), (44, 15))
        self.add_arc('sym-e16', (44, 15), (39, 8), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('sym-e17', (39, 8), (35, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3', 'sym-e4', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e11', closed=False)
        self.add_contour('sym-c1', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e16', 'sym-e17', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
