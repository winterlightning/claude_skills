"""Fire (weather), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ae1316a-475c-4f56-8965-7568f85bd529'
SOURCE_PATH = 'pictographic-primitives/weather/fire_5ae1316a-475c-4f56-8965-7568f85bd529.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Fire5ae1316a(Solo48):
    icon_id = 'fire-5ae1316a'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('fire', 'weather')

    def build(self):
        self.add_line('e0', (17, 16), (12, 21))
        self.add_line('e1', (27, 8), (22, 4))
        self.add_arc('e2', (22, 4), (17, 16), radius_x=18)
        self.add_arc('e3-1', (12, 21), (9, 26), radius_x=16, sweep=False)
        self.add_line('e3-2', (9, 26), (8, 31))
        self.add_arc('e3-3', (8, 31), (10, 37), radius_x=10, sweep=False)
        self.add_arc('e3-4', (10, 37), (24, 44), radius_x=18, sweep=False)
        self.add_arc('e3-5', (24, 44), (35, 40), radius_x=18, sweep=False)
        self.add_arc('e3-6', (35, 40), (40, 30), radius_x=13, sweep=False)
        self.add_arc('e3-7', (40, 30), (27, 8), radius_x=32, sweep=False)
        self.add_contour('c0', 'e2', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e1', closed=True)
