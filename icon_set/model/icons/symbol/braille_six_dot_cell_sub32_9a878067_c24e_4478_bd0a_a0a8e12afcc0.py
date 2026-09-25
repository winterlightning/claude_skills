"""Independent 32px profile of braille-six-dot-cell.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '9a878067-c24e-4478-bd0a-a0a8e12afcc0'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/9a878067-c24e-4478-bd0a-a0a8e12afcc0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9a878067-c24e-4478-bd0a-a0a8e12afcc0', 'icon_set/dist/gallery/combination-originals/9a878067-c24e-4478-bd0a-a0a8e12afcc0.svg'),)
PROFILE_SOURCE_KEYS = ('solo/braille-six-dot-cell',)
SOLO_SOURCE_ICON_IDS = ('braille-six-dot-cell',)
REFERENCE_EXPORT_SHA256 = 'c7659ab3e748745df49387da6d4a95ce36e3dbd3d044567875901fc84767cfec'

class Drawing(Sub32):
    icon_id = 'braille-six-dot-cell-sub32'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (6, 2), (6, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (6, 16), (6, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (6, 30), (6, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (26, 2), (26, 2))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (26, 16), (26, 16))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (26, 30), (26, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
