"""Independent 32px profile of funnel.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '107e54f1-5e5c-40e0-a51b-c1aeca9aed3a'
SOURCE_PATH = 'pictographic-primitives/symbol/funnel_107e54f1-5e5c-40e0-a51b-c1aeca9aed3a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('107e54f1-5e5c-40e0-a51b-c1aeca9aed3a', 'pictographic-primitives/symbol/funnel_107e54f1-5e5c-40e0-a51b-c1aeca9aed3a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/funnel',)
SOLO_SOURCE_ICON_IDS = ('funnel',)
REFERENCE_EXPORT_SHA256 = '55daf44353fa75c9ac3bc62a19497107c5fa33d7a5a603267a2d21889b13fb7a'

class Drawing(Sub32):
    icon_id = 'funnel-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (12, 30), (12, 18))
        self.add_line('p1-r1-2', (12, 18), (2, 2))
        self.add_line('p1-r1-3', (2, 2), (30, 2))
        self.add_line('p1-r1-4', (30, 2), (20, 18))
        self.add_line('p1-r1-5', (20, 18), (20, 23))
        self.add_line('p1-r1-6', (20, 23), (12, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
