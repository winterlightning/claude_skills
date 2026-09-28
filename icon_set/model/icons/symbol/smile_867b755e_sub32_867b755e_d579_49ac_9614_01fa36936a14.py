"""Independent 32px profile of smile-867b755e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '867b755e-d579-49ac-9614-01fa36936a14'
SOURCE_PATH = 'pictographic-primitives/smileys/smile_867b755e-d579-49ac-9614-01fa36936a14.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('867b755e-d579-49ac-9614-01fa36936a14', 'pictographic-primitives/smileys/smile_867b755e-d579-49ac-9614-01fa36936a14.svg'),)
PROFILE_SOURCE_KEYS = ('solo/smile-867b755e',)
SOLO_SOURCE_ICON_IDS = ('smile-867b755e',)
REFERENCE_EXPORT_SHA256 = '425abd922116237f4849cf15f9905db1f85d1f12075a53b398a48c318cce1441'

class Drawing(Sub32):
    icon_id = 'smile-867b755e-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'smileys'
    categories = ('smileys', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (16, 2), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 2), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (30, 16), (16, 30), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 30), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_arc('p2-r1-1', (8, 13), (13, 13), radius_x=2.5, radius_y=2.5, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (20, 13), (24, 13), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_bezier('p4-r1-1', (9, 20), ((10, 22), (13, 24), (16, 24)))
        self.add_bezier('p4-r1-2', (16, 24), ((19, 24), (22, 22), (23, 20)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
