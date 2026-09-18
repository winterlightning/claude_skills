"""Independent 32px profile of religious-cross.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9c558392-d894-4aba-8bb9-2185dd4ed2fe'
SOURCE_PATH = 'pictographic-primitives/religion/religious cross_9c558392-d894-4aba-8bb9-2185dd4ed2fe.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9c558392-d894-4aba-8bb9-2185dd4ed2fe', 'pictographic-primitives/religion/religious cross_9c558392-d894-4aba-8bb9-2185dd4ed2fe.svg'),)
PROFILE_SOURCE_KEYS = ('solo/religious-cross',)
SOLO_SOURCE_ICON_IDS = ('religious-cross',)
REFERENCE_EXPORT_SHA256 = '56d57a5c91cd60286131789072b054c481906a9fbff462c771d6b708bd17f021'

class Drawing(Sub32):
    icon_id = 'religious-cross-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'religion'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (20, 2), (13, 2))
        self.add_line('p1-r1-2', (13, 2), (13, 10))
        self.add_line('p1-r1-3', (13, 10), (5, 10))
        self.add_line('p1-r1-4', (5, 10), (5, 17))
        self.add_line('p1-r1-5', (5, 17), (13, 17))
        self.add_line('p1-r1-6', (13, 17), (13, 30))
        self.add_line('p1-r1-7', (13, 30), (20, 30))
        self.add_line('p1-r1-8', (20, 30), (20, 17))
        self.add_line('p1-r1-9', (20, 17), (27, 17))
        self.add_line('p1-r1-10', (27, 17), (27, 10))
        self.add_line('p1-r1-11', (27, 10), (20, 10))
        self.add_line('p1-r1-12', (20, 10), (20, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
