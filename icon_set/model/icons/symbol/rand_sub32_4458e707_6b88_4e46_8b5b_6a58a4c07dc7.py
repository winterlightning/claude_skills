"""Independent 32px profile of rand.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '4458e707-6b88-4e46-8b5b-6a58a4c07dc7'
SOURCE_PATH = 'pictographic-primitives/money/rand_4458e707-6b88-4e46-8b5b-6a58a4c07dc7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4458e707-6b88-4e46-8b5b-6a58a4c07dc7', 'pictographic-primitives/money/rand_4458e707-6b88-4e46-8b5b-6a58a4c07dc7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rand',)
SOLO_SOURCE_ICON_IDS = ('rand',)
REFERENCE_EXPORT_SHA256 = '46e26b758a0af08ee3fba4a653e061fcf890869e4012434b83f084c2ddac4520'

class Drawing(Sub32):
    icon_id = 'rand-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'money'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 30), (5, 2))
        self.add_line('p1-r1-2', (5, 2), (19, 2))
        self.add_arc('p1-r1-3', (19, 2), (19, 19), radius_x=8.5, radius_y=8.5, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (19, 19), (5, 19))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (19, 19), (27, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
