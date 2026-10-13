"""Independent 32px profile of electric-plug-bolt-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '1fed8230-55dc-4ab0-90b8-ea4b658f60cf'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/1fed8230-55dc-4ab0-90b8-ea4b658f60cf.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1fed8230-55dc-4ab0-90b8-ea4b658f60cf', 'icon_set/dist/gallery/combination-originals/1fed8230-55dc-4ab0-90b8-ea4b658f60cf.svg'),)
PROFILE_SOURCE_KEYS = ('solo/electric-plug-bolt-content',)
SOLO_SOURCE_ICON_IDS = ('electric-plug-bolt-content',)
REFERENCE_EXPORT_SHA256 = '46050475537a73cb1a1ff32473a293eab6e2031bb6f07f015031ae93e1521b10'

class Drawing(Sub32):
    icon_id = 'electric-plug-bolt-content-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Plug on the left (prongs on its top corners), a Z bolt on the right with diagonals 8 units apart.
        self.add_line('p1-r1-1', (2, 6), (2, 14))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (12, 6), (12, 14))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 14), (12, 14))
        self.add_line('p3-r1-2', (12, 14), (12, 20))
        self.add_arc('p3-r1-3', (12, 20), (7, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (7, 25), (2, 20), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p3-r1-5', (2, 20), (2, 14))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=True)
        self.add_line('p4-r1-1', (7, 25), (7, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (30, 2), (20, 16))
        self.add_line('p5-r1-2', (20, 16), (30, 16))
        self.add_line('p5-r1-3', (30, 16), (20, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-5')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p3-r1-3', 'p4-r1-1')
        self.relate('connect', 'p3-r1-4', 'p4-r1-1')
