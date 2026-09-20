# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of drop-smileys.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '6eeb8b64-353f-4d55-afc4-cee5edb7104e'
SOURCE_PATH = 'pictographic-primitives/smileys/drop_6eeb8b64-353f-4d55-afc4-cee5edb7104e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6eeb8b64-353f-4d55-afc4-cee5edb7104e', 'pictographic-primitives/smileys/drop_6eeb8b64-353f-4d55-afc4-cee5edb7104e.svg'), ('a1bd3645-c186-44d1-a3a2-2ec8e3d10a1b', 'pictographic-primitives/smileys/drop_a1bd3645-c186-44d1-a3a2-2ec8e3d10a1b.svg'))
PROFILE_SOURCE_KEYS = ('solo/drop-smileys', 'solo/drop-a1bd3645')
SOLO_SOURCE_ICON_IDS = ('drop-smileys', 'drop-a1bd3645')
REFERENCE_EXPORT_SHA256 = 'afc6655d1a83856b44a22f8f0b018899ae899d9fad8607c25ca680fd7e862457'

class DrawingContainerSymbol(Sub32):
    icon_id = 'drop-smileys-sub32-symbol'
    variant_of = 'drop-smileys-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/drop-smileys-sub32'
    counterpart_icon_id = 'drop-smileys-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'smileys'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 2), ((12, 7), (5, 14), (5, 19)))
        self.add_bezier('p1-r1-2', (5, 19), ((5, 25), (10, 30), (16, 30)))
        self.add_bezier('p1-r1-3', (16, 30), ((22, 30), (27, 25), (27, 19)))
        self.add_bezier('p1-r1-4', (27, 19), ((27, 14), (20, 7), (16, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_arc('p2-r1-1', (16, 23), (20, 19), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
