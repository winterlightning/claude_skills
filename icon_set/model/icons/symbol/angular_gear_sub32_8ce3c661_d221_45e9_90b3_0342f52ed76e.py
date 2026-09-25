"""Independent 32px profile of angular-gear.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '8ce3c661-d221-45e9-90b3-0342f52ed76e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_8ce3c661-d221-45e9-90b3-0342f52ed76e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8ce3c661-d221-45e9-90b3-0342f52ed76e', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_8ce3c661-d221-45e9-90b3-0342f52ed76e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/angular-gear',)
SOLO_SOURCE_ICON_IDS = ('angular-gear',)
REFERENCE_EXPORT_SHA256 = '7802da3818f98233be9a5798d5aa8799bd463a1b1b324d855b3b446722903f5c'

class Drawing(Sub32):
    icon_id = 'angular-gear-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (14, 2), (12, 7))
        self.add_line('p1-r1-2', (12, 7), (9, 8))
        self.add_line('p1-r1-3', (9, 8), (5, 7))
        self.add_line('p1-r1-4', (5, 7), (2, 11))
        self.add_line('p1-r1-5', (2, 11), (5, 15))
        self.add_line('p1-r1-6', (5, 15), (4, 16))
        self.add_line('p1-r1-7', (4, 16), (2, 18))
        self.add_line('p1-r1-8', (2, 18), (4, 24))
        self.add_line('p1-r1-9', (4, 24), (7, 24))
        self.add_line('p1-r1-10', (7, 24), (7, 30))
        self.add_line('p1-r1-11', (7, 30), (13, 30))
        self.add_line('p1-r1-12', (13, 30), (13, 24))
        self.add_line('p1-r1-13', (13, 24), (16, 24))
        self.add_line('p1-r1-14', (16, 24), (19, 24))
        self.add_line('p1-r1-15', (19, 24), (19, 30))
        self.add_line('p1-r1-16', (19, 30), (25, 30))
        self.add_line('p1-r1-17', (25, 30), (25, 24))
        self.add_line('p1-r1-18', (25, 24), (28, 24))
        self.add_line('p1-r1-19', (28, 24), (30, 18))
        self.add_line('p1-r1-20', (30, 18), (28, 16))
        self.add_line('p1-r1-21', (28, 16), (27, 15))
        self.add_line('p1-r1-22', (27, 15), (30, 11))
        self.add_line('p1-r1-23', (30, 11), (27, 7))
        self.add_line('p1-r1-24', (27, 7), (23, 8))
        self.add_line('p1-r1-25', (23, 8), (20, 7))
        self.add_line('p1-r1-26', (20, 7), (18, 2))
        self.add_line('p1-r1-27', (18, 2), (14, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', 'p1-r1-18', 'p1-r1-19', 'p1-r1-20', 'p1-r1-21', 'p1-r1-22', 'p1-r1-23', 'p1-r1-24', 'p1-r1-25', 'p1-r1-26', 'p1-r1-27', closed=False)
