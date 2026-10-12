"""Independent 32px profile of veterinary-paw-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'de729c05-6cce-4720-a0be-a92e22cd665a'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/de729c05-6cce-4720-a0be-a92e22cd665a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('de729c05-6cce-4720-a0be-a92e22cd665a', 'icon_set/dist/gallery/combination-originals/de729c05-6cce-4720-a0be-a92e22cd665a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/veterinary-paw-content',)
SOLO_SOURCE_ICON_IDS = ('veterinary-paw-content',)
REFERENCE_EXPORT_SHA256 = 'bd74d1de4f051219b562915d264d0d4b1ea6c066adceaaade33aefa9762c2515'

class Drawing(Sub32):
    icon_id = 'veterinary-paw-content-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Toes as dots; tall pad with a small medical cross.
        self.add_line('p1-r1-1', (16, 2), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 8), (2, 8))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (30, 8), (30, 8))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (8, 30), (4, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p4-r1-2', (4, 25), (4, 24))
        self.add_arc('p4-r1-3', (4, 24), (16, 10), radius_x=12, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p4-r1-4', (16, 10), (28, 24), radius_x=12, radius_y=14, large_arc=False, sweep=True)
        self.add_line('p4-r1-5', (28, 24), (28, 25))
        self.add_arc('p4-r1-6', (28, 25), (24, 30), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p4-r1-7', (24, 30), (8, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', closed=False)
        self.add_line('p5-r1-1', (16, 20), (14, 20))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (16, 20), (18, 20))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (16, 20), (16, 18))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (16, 20), (16, 22))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
        self.relate('connect', 'p5-r1-1', 'p7-r1-1')
        self.relate('connect', 'p5-r1-1', 'p8-r1-1')
        self.relate('connect', 'p6-r1-1', 'p7-r1-1')
        self.relate('connect', 'p6-r1-1', 'p8-r1-1')
        self.relate('connect', 'p7-r1-1', 'p8-r1-1')
