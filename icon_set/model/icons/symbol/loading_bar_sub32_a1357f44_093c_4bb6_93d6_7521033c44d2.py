"""Independent 32px profile of loading-bar.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'a1357f44-093c-4bb6-93d6-7521033c44d2'
SOURCE_PATH = 'pictographic-primitives/interface-essential/loading bar_a1357f44-093c-4bb6-93d6-7521033c44d2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a1357f44-093c-4bb6-93d6-7521033c44d2', 'pictographic-primitives/interface-essential/loading bar_a1357f44-093c-4bb6-93d6-7521033c44d2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/loading-bar',)
SOLO_SOURCE_ICON_IDS = ('loading-bar',)
REFERENCE_EXPORT_SHA256 = 'c44d8ded20a6551ec80e2862465f106c70b67040044ba6801272bb5ae5e8c13c'

class Drawing(Sub32):
    icon_id = 'loading-bar-sub32'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Pill outline on the taller HRECT_L box so the progress bar keeps 4 units to the outline.
        self.add_line('p1-r1-1', (12, 6), (20, 6))
        self.add_arc('p1-r1-2', (20, 6), (20, 26), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (20, 26), (12, 26))
        self.add_arc('p1-r1-4', (12, 26), (12, 6), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=True)
        self.add_line('p2-r1-1', (10, 16), (18, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
