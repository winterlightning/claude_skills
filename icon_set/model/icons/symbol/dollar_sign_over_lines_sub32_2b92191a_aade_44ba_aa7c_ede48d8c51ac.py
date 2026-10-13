"""Independent 32px profile of dollar-sign-over-lines.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2b92191a-aade-44ba-aa7c-ede48d8c51ac'
SOURCE_PATH = 'pictographic-primitives/symbol/dollar with texts_2b92191a-aade-44ba-aa7c-ede48d8c51ac.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2b92191a-aade-44ba-aa7c-ede48d8c51ac', 'pictographic-primitives/symbol/dollar with texts_2b92191a-aade-44ba-aa7c-ede48d8c51ac.svg'),)
PROFILE_SOURCE_KEYS = ('solo/dollar-sign-over-lines',)
SOLO_SOURCE_ICON_IDS = ('dollar-sign-over-lines',)
REFERENCE_EXPORT_SHA256 = 'b2f284f3c0c7adc2de105fcfa1d52fdd4ba077fc5d102d34a07e5ca382b5e0ab'

class Drawing(Sub32):
    icon_id = 'dollar-sign-over-lines-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Dollar sign with 8-unit counters over one line (two lines leave no room for the sign).
        self.add_line('p1-r1-1', (20, 4), (16, 4))
        self.add_arc('p1-r1-2', (16, 4), (16, 12), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('p1-r1-3', (16, 12), (16, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (16, 20), (12, 20))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (16, 2), (16, 4))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 20), (16, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 30), (30, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
