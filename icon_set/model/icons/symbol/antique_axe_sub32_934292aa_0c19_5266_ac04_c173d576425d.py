"""Independent 32px profile of antique-axe.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '934292aa-0c19-5266-ac04-c173d576425d'
SOURCE_PATH = 'pictographic-primitives/war/antique axe_934292aa-0c19-5266-ac04-c173d576425d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('934292aa-0c19-5266-ac04-c173d576425d', 'pictographic-primitives/war/antique axe_934292aa-0c19-5266-ac04-c173d576425d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/antique-axe',)
SOLO_SOURCE_ICON_IDS = ('antique-axe',)
REFERENCE_EXPORT_SHA256 = '72a66de3e6a3625a7e88b7a52841d8347d3dc50b9dc5394b731c5de939adccd9'

class Drawing(Sub32):
    icon_id = 'antique-axe-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'war'
    categories = ('war', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Adopted from the production stroke edit (Browser Edit by hina).
        self.add_line('p1-r1-1', (8, 10), (13, 2))
        self.add_line('p1-r1-2', (13, 2), (30, 6))
        self.add_line('p1-r1-3', (30, 6), (30, 6))
        self.add_bezier('p1-r1-4', (30, 6), ((30, 16), (24.444444, 24), (20, 24)))
        self.add_line('p1-r1-5', (20, 24), (20, 16))
        self.add_line('p1-r1-6', (20, 16), (8, 10))
        self.add_line('p1-r1-7', (8, 10), (8, 10))
        self.add_line('p2-r1-1', (15, 14), (2, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        # Declared joints: these strokes meet or cross on purpose.
        self.relate('connect', 'path-1-1', 'path-2-1')
