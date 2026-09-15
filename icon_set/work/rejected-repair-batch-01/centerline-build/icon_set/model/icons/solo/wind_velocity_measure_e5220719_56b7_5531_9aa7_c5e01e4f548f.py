"""Wind velocity measure (weather), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5220719-56b7-5531-9aa7-c5e01e4f548f'
SOURCE_PATH = 'pictographic-primitives/weather/wind velocity measure_e5220719-56b7-5531-9aa7-c5e01e4f548f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class WindVelocityMeasure(Solo48):
    icon_id = 'wind-velocity-measure'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('wind', 'velocity', 'measure', 'weather')

    def build(self):
        self.add_line('e0', (17, 9), (41, 18))
        self.add_line('e1', (42, 21), (17, 30))
        self.add_line('e2', (17, 9), (17, 30))
        self.add_line('e3', (17, 30), (6, 22))
        self.add_line('e4', (17, 9), (6, 17))
        self.add_line('e5', (30, 25), (30, 14))
        self.add_line('e6', (6, 42), (6, 6))
        self.add_line('e7-1', (41, 18), (42, 20))
        self.add_line('e7-2', (42, 20), (42, 21))
        self.add_contour('c0', 'e0', 'e7-1', 'e7-2', 'e1')
        self.add_contour('c1', 'e2', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c3', 'c0')
