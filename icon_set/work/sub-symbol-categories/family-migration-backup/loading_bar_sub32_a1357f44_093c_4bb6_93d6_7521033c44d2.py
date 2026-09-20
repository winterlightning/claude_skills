"""Independent 32px profile of loading-bar.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a1357f44-093c-4bb6-93d6-7521033c44d2'
SOURCE_PATH = 'pictographic-primitives/interface-essential/loading bar_a1357f44-093c-4bb6-93d6-7521033c44d2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a1357f44-093c-4bb6-93d6-7521033c44d2', 'pictographic-primitives/interface-essential/loading bar_a1357f44-093c-4bb6-93d6-7521033c44d2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/loading-bar',)
SOLO_SOURCE_ICON_IDS = ('loading-bar',)
REFERENCE_EXPORT_SHA256 = 'c44d8ded20a6551ec80e2862465f106c70b67040044ba6801272bb5ae5e8c13c'

class Drawing(Sub32):
    icon_id = 'loading-bar-sub32'
    keyshape = Keyshape.HRECT_S
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 10), (24, 10))
        self.add_arc('p1-r1-2', (24, 10), (24, 22), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (24, 22), (8, 22))
        self.add_arc('p1-r1-4', (8, 22), (8, 10), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (9, 16), (19, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
