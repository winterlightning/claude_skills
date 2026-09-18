"""Independent 32px profile of fire.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd57b67f9-c8ed-433b-aa42-f2f21b118e83'
SOURCE_PATH = 'pictographic-primitives/fire/fire_d57b67f9-c8ed-433b-aa42-f2f21b118e83.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d57b67f9-c8ed-433b-aa42-f2f21b118e83', 'pictographic-primitives/fire/fire_d57b67f9-c8ed-433b-aa42-f2f21b118e83.svg'),)
PROFILE_SOURCE_KEYS = ('solo/fire',)
SOLO_SOURCE_ICON_IDS = ('fire',)
REFERENCE_EXPORT_SHA256 = 'c6dd4677dfb60bf75d6076281dd70575b17f10a91240fb12519e0475ec6926c8'

class Drawing(Sub32):
    icon_id = 'fire-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'fire'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (15, 2), ((17, 4), (21, 9), (21, 13)))
        self.add_bezier('p1-r1-2', (21, 13), ((21, 15), (20, 17), (20, 18)))
        self.add_line('p1-r1-3', (20, 18), (25, 14))
        self.add_bezier('p1-r1-4', (25, 14), ((26, 17), (27, 19), (27, 21)))
        self.add_bezier('p1-r1-5', (27, 21), ((27, 26), (22, 30), (16, 30)))
        self.add_bezier('p1-r1-6', (16, 30), ((10, 30), (5, 26), (5, 20)))
        self.add_bezier('p1-r1-7', (5, 20), ((5, 13), (13, 10), (15, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
