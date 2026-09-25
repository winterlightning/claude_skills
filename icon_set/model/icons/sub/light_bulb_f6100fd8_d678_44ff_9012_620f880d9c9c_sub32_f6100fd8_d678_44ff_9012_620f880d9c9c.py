"""Independent 32px profile of light-bulb-f6100fd8-d678-44ff-9012-620f880d9c9c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f6100fd8-d678-44ff-9012-620f880d9c9c'
SOURCE_PATH = 'pictographic-primitives/lights/light bulb_f6100fd8-d678-44ff-9012-620f880d9c9c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f6100fd8-d678-44ff-9012-620f880d9c9c', 'pictographic-primitives/lights/light bulb_f6100fd8-d678-44ff-9012-620f880d9c9c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/light-bulb-f6100fd8-d678-44ff-9012-620f880d9c9c',)
SOLO_SOURCE_ICON_IDS = ('light-bulb-f6100fd8-d678-44ff-9012-620f880d9c9c',)
REFERENCE_EXPORT_SHA256 = '2e76e8983b56cdc4ddbd1728d2b49e0c5f50bdd1bcac4c24ef47b5ccc0b36460'

class Drawing(Sub32):
    icon_id = 'light-bulb-f6100fd8-d678-44ff-9012-620f880d9c9c-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'lights'
    categories = ('lights', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 11), (30, 11), radius_x=14, radius_y=9, large_arc=False, sweep=True)
        self.add_bezier('p1-r1-2', (30, 11), ((30, 13), (30, 14), (29, 15)))
        self.add_bezier('p1-r1-3', (29, 15), ((29, 16), (28, 17), (27, 18)))
        self.add_arc('p1-r1-4', (27, 18), (24, 24), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('p1-r1-5', (24, 24), (8, 24), radius_x=8, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (8, 24), (5, 18), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_bezier('p1-r1-7', (5, 18), ((4, 17), (3, 16), (3, 15)))
        self.add_bezier('p1-r1-8', (3, 15), ((2, 14), (2, 13), (2, 11)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (8, 24), (24, 24))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
