"""Independent 32px profile of fragile-upright-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '25d79f58-c01d-4a82-8565-6562d2773dd8'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/25d79f58-c01d-4a82-8565-6562d2773dd8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('25d79f58-c01d-4a82-8565-6562d2773dd8', 'icon_set/dist/gallery/combination-originals/25d79f58-c01d-4a82-8565-6562d2773dd8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/fragile-upright-content',)
SOLO_SOURCE_ICON_IDS = ('fragile-upright-content',)
REFERENCE_EXPORT_SHA256 = '684799bceda1932058fa59f8db556355cc33f59f3aad4e8046420d745316aaa0'

class Drawing(Sub32):
    icon_id = 'fragile-upright-content-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Fragile, this way up: a narrower glass on its stem and base, and an up arrow 4 units clear.
        self.add_line('g-1', (2, 2), (12, 2))
        self.add_line('g-2', (12, 2), (12, 13))
        self.add_arc('g-3', (12, 13), (2, 13), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('g-4', (2, 13), (2, 2))
        self.add_contour('glass', 'g-1', 'g-2', 'g-3', 'g-4', closed=True)
        self.add_line('stem', (7, 18), (7, 30))
        self.add_line('base', (2, 30), (12, 30))
        self.add_polyline('head', (20, 6), (25, 2), (30, 6))
        self.add_line('shaft', (25, 2), (25, 30))
        self.relate('connect', 'glass', 'stem')
        self.relate('connect', 'stem', 'base')
        self.relate('connect', 'head', 'shaft')
