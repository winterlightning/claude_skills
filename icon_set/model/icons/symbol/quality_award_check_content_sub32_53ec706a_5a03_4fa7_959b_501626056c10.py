"""Independent 32px profile of quality-award-check-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '53ec706a-5a03-4fa7-959b-501626056c10'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/53ec706a-5a03-4fa7-959b-501626056c10.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('53ec706a-5a03-4fa7-959b-501626056c10', 'icon_set/dist/gallery/combination-originals/53ec706a-5a03-4fa7-959b-501626056c10.svg'),)
PROFILE_SOURCE_KEYS = ('solo/quality-award-check-content',)
SOLO_SOURCE_ICON_IDS = ('quality-award-check-content',)
REFERENCE_EXPORT_SHA256 = '5135882253e5ddc32063df5791063f24b4be810851b5e6ebcccba37c8b365da4'

class Drawing(Sub32):
    icon_id = 'quality-award-check-content-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Quality award: medal circle with a check mark, two ribbon tails.
        self.add_arc('medal-1', (4, 14), (28, 14), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('medal-2', (28, 14), (4, 14), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_contour('medal', 'medal-1', 'medal-2', closed=True)
        self.add_polyline('check', (13, 14), (15, 16), (19, 12))
        self.add_line('ribbon-l', (8, 23), (5, 30))
        self.add_line('ribbon-r', (24, 23), (27, 30))
        self.relate('connect', 'medal', 'ribbon-l')
        self.relate('connect', 'medal', 'ribbon-r')
