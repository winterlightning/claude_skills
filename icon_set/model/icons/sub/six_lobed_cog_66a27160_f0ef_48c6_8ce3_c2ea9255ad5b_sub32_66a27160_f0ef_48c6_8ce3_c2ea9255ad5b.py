"""Independent 32px profile of six-lobed-cog-66a27160-f0ef-48c6-8ce3-c2ea9255ad5b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '66a27160-f0ef-48c6-8ce3-c2ea9255ad5b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_66a27160-f0ef-48c6-8ce3-c2ea9255ad5b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('66a27160-f0ef-48c6-8ce3-c2ea9255ad5b', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_66a27160-f0ef-48c6-8ce3-c2ea9255ad5b.svg'), ('e3d63c1e-a685-484b-8eae-ef88e3411b1e', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_e3d63c1e-a685-484b-8eae-ef88e3411b1e.svg'))
PROFILE_SOURCE_KEYS = ('solo/six-lobed-cog-66a27160-f0ef-48c6-8ce3-c2ea9255ad5b', 'solo/six-lobed-cog-e3d63c1e-a685-484b-8eae-ef88e3411b1e')
SOLO_SOURCE_ICON_IDS = ('six-lobed-cog-66a27160-f0ef-48c6-8ce3-c2ea9255ad5b', 'six-lobed-cog-e3d63c1e-a685-484b-8eae-ef88e3411b1e')
REFERENCE_EXPORT_SHA256 = 'de2b86749ce5a30a52bed4e6b5975351feba0d38cc4c88e8fe073bde0fb9c4ab'

class Drawing(Sub32):
    icon_id = 'six-lobed-cog-66a27160-f0ef-48c6-8ce3-c2ea9255ad5b-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 2), ((21, 2), (18, 9), (23, 9)))
        self.add_bezier('p1-r1-2', (23, 9), ((24, 9), (27, 8), (28, 8)))
        self.add_bezier('p1-r1-3', (28, 8), ((29, 8), (30, 8), (30, 11)))
        self.add_bezier('p1-r1-4', (30, 11), ((30, 13), (25, 14), (25, 16)))
        self.add_bezier('p1-r1-5', (25, 16), ((25, 18), (30, 19), (30, 21)))
        self.add_bezier('p1-r1-6', (30, 21), ((30, 24), (29, 24), (28, 24)))
        self.add_bezier('p1-r1-7', (28, 24), ((27, 24), (24, 23), (23, 23)))
        self.add_bezier('p1-r1-8', (23, 23), ((18, 23), (21, 30), (16, 30)))
        self.add_bezier('p1-r1-9', (16, 30), ((11, 30), (14, 23), (9, 23)))
        self.add_bezier('p1-r1-10', (9, 23), ((8, 23), (5, 24), (4, 24)))
        self.add_bezier('p1-r1-11', (4, 24), ((3, 24), (2, 24), (2, 21)))
        self.add_bezier('p1-r1-12', (2, 21), ((2, 19), (7, 18), (7, 16)))
        self.add_bezier('p1-r1-13', (7, 16), ((7, 14), (2, 13), (2, 11)))
        self.add_bezier('p1-r1-14', (2, 11), ((2, 8), (3, 8), (4, 8)))
        self.add_bezier('p1-r1-15', (4, 8), ((5, 8), (8, 9), (9, 9)))
        self.add_bezier('p1-r1-16', (9, 9), ((14, 9), (11, 2), (16, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', closed=False)
        self.add_line('p2-r1-1', (16, 15), (16, 17))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
