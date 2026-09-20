"""Independent 32px profile of fragile-upright-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

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
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (13, 2))
        self.add_line('p1-r1-2', (13, 2), (13, 13))
        self.add_arc('p1-r1-3', (13, 13), (2, 13), radius_x=5.5, radius_y=5.5, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (2, 13), (2, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (7, 18), (7, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 30), (13, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (19, 8), (25, 2))
        self.add_line('p4-r1-2', (25, 2), (30, 8))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (25, 2), (25, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
        self.relate("connect", 'p4-r1-2', 'p5-r1-1')
