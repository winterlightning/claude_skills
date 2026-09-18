"""Independent 32px profile of battery.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9ad9cd5c-98cd-452e-ad18-784b9bd66c4d'
SOURCE_PATH = 'pictographic-primitives/photography/battery_9ad9cd5c-98cd-452e-ad18-784b9bd66c4d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9ad9cd5c-98cd-452e-ad18-784b9bd66c4d', 'pictographic-primitives/photography/battery_9ad9cd5c-98cd-452e-ad18-784b9bd66c4d.svg'), ('d0244858-b455-4673-842d-844f0c652966', 'pictographic-primitives/photography/battery_d0244858-b455-4673-842d-844f0c652966.svg'))
PROFILE_SOURCE_KEYS = ('solo/battery', 'solo/empty-upright-battery')
SOLO_SOURCE_ICON_IDS = ('battery', 'empty-upright-battery')
REFERENCE_EXPORT_SHA256 = '4695269714d782ca4e93e5345b16c88649e8e9bd14b055fe8cae0f66ec910ea6'

class Drawing(Sub32):
    icon_id = 'battery-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'photography'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 8), (10, 8))
        self.add_line('p1-r1-2', (10, 8), (22, 8))
        self.add_line('p1-r1-3', (22, 8), (24, 8))
        self.add_arc('p1-r1-4', (24, 8), (27, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (27, 10), (27, 27))
        self.add_arc('p1-r1-6', (27, 27), (24, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (24, 30), (8, 30))
        self.add_arc('p1-r1-8', (8, 30), (5, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (5, 27), (5, 10))
        self.add_arc('p1-r1-10', (5, 10), (8, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (10, 8), (10, 2))
        self.add_line('p2-r1-2', (10, 2), (22, 2))
        self.add_line('p2-r1-3', (22, 2), (22, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-3')
        self.relate("connect", 'p1-r1-3', 'p2-r1-3')
