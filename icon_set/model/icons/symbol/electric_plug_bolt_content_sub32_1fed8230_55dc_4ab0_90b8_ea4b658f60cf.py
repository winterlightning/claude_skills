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
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 8), (5, 14))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (11, 8), (11, 14))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 14), (14, 14))
        self.add_line('p3-r1-2', (14, 14), (14, 18))
        self.add_arc('p3-r1-3', (14, 18), (8, 24), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (8, 24), (2, 18), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p3-r1-5', (2, 18), (2, 14))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (8, 24), (8, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (30, 2), (21, 11))
        self.add_line('p5-r1-2', (21, 11), (30, 11))
        self.add_line('p5-r1-3', (30, 11), (22, 19))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.relate('connect', 'p3-r1-3', 'p4-r1-1')
        self.relate('connect', 'p3-r1-4', 'p4-r1-1')
