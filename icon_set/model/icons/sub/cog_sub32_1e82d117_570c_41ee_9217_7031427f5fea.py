"""Independent 32px profile of cog.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1e82d117-570c-41ee-9217-7031427f5fea'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cog_1e82d117-570c-41ee-9217-7031427f5fea.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1e82d117-570c-41ee-9217-7031427f5fea', 'pictographic-primitives/interface-essential/cog_1e82d117-570c-41ee-9217-7031427f5fea.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cog',)
SOLO_SOURCE_ICON_IDS = ('cog',)
REFERENCE_EXPORT_SHA256 = 'ca0417b4f2e37b73908fefeafc40a3aea2f0054eb4eead924858a3db26c2903e'

class Drawing(Sub32):
    icon_id = 'cog-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    categories = ('interface-essential', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 2), (19, 2))
        self.add_line('p1-r1-2', (19, 2), (21, 8))
        self.add_line('p1-r1-3', (21, 8), (27, 7))
        self.add_line('p1-r1-4', (27, 7), (30, 13))
        self.add_line('p1-r1-5', (30, 13), (25, 18))
        self.add_line('p1-r1-6', (25, 18), (30, 22))
        self.add_line('p1-r1-7', (30, 22), (27, 28))
        self.add_line('p1-r1-8', (27, 28), (21, 27))
        self.add_line('p1-r1-9', (21, 27), (19, 30))
        self.add_line('p1-r1-10', (19, 30), (13, 30))
        self.add_line('p1-r1-11', (13, 30), (11, 27))
        self.add_line('p1-r1-12', (11, 27), (5, 28))
        self.add_line('p1-r1-13', (5, 28), (2, 22))
        self.add_line('p1-r1-14', (2, 22), (7, 18))
        self.add_line('p1-r1-15', (7, 18), (2, 13))
        self.add_line('p1-r1-16', (2, 13), (5, 7))
        self.add_line('p1-r1-17', (5, 7), (11, 8))
        self.add_line('p1-r1-18', (11, 8), (13, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', 'p1-r1-18', closed=False)
        self.add_line('p2-r1-1', (16, 16), (16, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
