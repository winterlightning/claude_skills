"""Independent 32px profile of information.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '13718512-f145-41c1-8a96-ce57c5ff8408'
SOURCE_PATH = 'pictographic-primitives/symbol/information_13718512-f145-41c1-8a96-ce57c5ff8408.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('13718512-f145-41c1-8a96-ce57c5ff8408', 'pictographic-primitives/symbol/information_13718512-f145-41c1-8a96-ce57c5ff8408.svg'),)
PROFILE_SOURCE_KEYS = ('solo/information',)
SOLO_SOURCE_ICON_IDS = ('information',)
REFERENCE_EXPORT_SHA256 = '419264226416cd0613d9f3369e4549fa9b33c4a4eb8af82cec199f5f6ffdbd4f'

class Drawing(Sub32):
    icon_id = 'information-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 2), (20, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (5, 12), (16, 12))
        self.add_line('p2-r1-2', (16, 12), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (5, 30), (27, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
