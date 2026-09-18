"""Independent 32px profile of moon-and-star.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b7ea547a-6e38-4494-be1a-8e7ed00dd417'
SOURCE_PATH = 'pictographic-primitives/symbol/moon and star_b7ea547a-6e38-4494-be1a-8e7ed00dd417.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b7ea547a-6e38-4494-be1a-8e7ed00dd417', 'pictographic-primitives/symbol/moon and star_b7ea547a-6e38-4494-be1a-8e7ed00dd417.svg'),)
PROFILE_SOURCE_KEYS = ('solo/moon-and-star',)
SOLO_SOURCE_ICON_IDS = ('moon-and-star',)
REFERENCE_EXPORT_SHA256 = '43adbe4b281e6a9120867a13ea55b0aeb19d9eca4f1f209cdd75c834741f7c06'

class Drawing(Sub32):
    icon_id = 'moon-and-star-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (13, 5), (2, 16), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_arc('p1-r1-2', (2, 16), (13, 27), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_arc('p1-r1-3', (13, 27), (13, 5), radius_x=4, radius_y=11, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (24, 8), (26, 13))
        self.add_line('p2-r1-2', (26, 13), (30, 13))
        self.add_line('p2-r1-3', (30, 13), (26, 17))
        self.add_line('p2-r1-4', (26, 17), (27, 22))
        self.add_line('p2-r1-5', (27, 22), (24, 20))
        self.add_line('p2-r1-6', (24, 20), (20, 22))
        self.add_line('p2-r1-7', (20, 22), (20, 17))
        self.add_line('p2-r1-8', (20, 17), (17, 13))
        self.add_line('p2-r1-9', (17, 13), (22, 13))
        self.add_line('p2-r1-10', (22, 13), (24, 8))
        self.add_line('p2-r1-11', (24, 8), (24, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', 'p2-r1-11', closed=False)
