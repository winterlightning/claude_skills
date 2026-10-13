"""Independent 32px profile of dryer-hair.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '34e94fc5-ce90-4627-9cd4-0ded39755e20'
SOURCE_PATH = 'pictographic-primitives/symbol/dryer hair_34e94fc5-ce90-4627-9cd4-0ded39755e20.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('34e94fc5-ce90-4627-9cd4-0ded39755e20', 'pictographic-primitives/symbol/dryer hair_34e94fc5-ce90-4627-9cd4-0ded39755e20.svg'),)
PROFILE_SOURCE_KEYS = ('solo/dryer-hair',)
SOLO_SOURCE_ICON_IDS = ('dryer-hair',)
REFERENCE_EXPORT_SHA256 = '24826e34de8889dd4bdd8920ac49b85bed88b7790c87cb2bbf2a32feede15b6a'

class Drawing(Sub32):
    icon_id = 'dryer-hair-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (23, 2))
        self.add_arc('p1-r1-2', (23, 2), (23, 16), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (23, 16), (21, 30))
        self.add_line('p1-r1-4', (21, 30), (12, 30))
        self.add_line('p1-r1-5', (12, 30), (14, 16))
        self.add_line('p1-r1-6', (14, 16), (2, 12))
        self.add_line('p1-r1-7', (2, 12), (2, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=True)
