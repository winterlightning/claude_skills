"""Independent 32px profile of sun.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '08d492fb-d883-4e25-9423-f3721a0a418f'
SOURCE_PATH = 'pictographic-primitives/weather/weather sun_08d492fb-d883-4e25-9423-f3721a0a418f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('08d492fb-d883-4e25-9423-f3721a0a418f', 'pictographic-primitives/weather/weather sun_08d492fb-d883-4e25-9423-f3721a0a418f.svg'), ('e1640603-3ce9-5ec9-a1ab-06e3fe5239a4', 'pictographic-primitives/weather/weather sun_e1640603-3ce9-5ec9-a1ab-06e3fe5239a4.svg'), ('9612aa29-9678-40f4-95b4-380662a7ece5', 'pictographic-primitives/weather/weather sun_9612aa29-9678-40f4-95b4-380662a7ece5.svg'))
PROFILE_SOURCE_KEYS = ('solo/sun', 'solo/sun-long-rays', 'solo/sun-short-rays')
SOLO_SOURCE_ICON_IDS = ('sun', 'sun-long-rays', 'sun-short-rays')
REFERENCE_EXPORT_SHA256 = 'fb9fee90d0f8d34723cf9c9d2d9df2c295450baf7828b20dcd7a4c7785b6eb62'

class Drawing(Sub32):
    icon_id = 'sun-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'weather'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (9, 16), (23, 16), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (23, 16), (9, 16), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 2), (16, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 30), (16, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 16), (2, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (30, 16), (30, 16))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (5, 5), (6, 6))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (26, 26), (27, 27))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (5, 27), (6, 26))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (26, 6), (27, 5))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
