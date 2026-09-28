"""Independent 32px profile of three-lines.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'f91c6f84-9971-4a9d-a251-a2d0cd8844cb'
SOURCE_PATH = 'pictographic-primitives/symbol/three lines_f91c6f84-9971-4a9d-a251-a2d0cd8844cb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f91c6f84-9971-4a9d-a251-a2d0cd8844cb', 'pictographic-primitives/symbol/three lines_f91c6f84-9971-4a9d-a251-a2d0cd8844cb.svg'),)
PROFILE_SOURCE_KEYS = ('solo/three-lines',)
SOLO_SOURCE_ICON_IDS = ('three-lines',)
REFERENCE_EXPORT_SHA256 = '1924370ece7dd9b9f91aae1815a18ce562860d365255ffd79bb5fba747d895b2'

class Drawing(Sub32):
    icon_id = 'three-lines-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 2), (27, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (5, 16), (27, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (5, 30), (27, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
