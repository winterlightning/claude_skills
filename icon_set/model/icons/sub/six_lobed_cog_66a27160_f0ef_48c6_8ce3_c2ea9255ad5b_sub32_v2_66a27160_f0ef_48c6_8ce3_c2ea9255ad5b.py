# Variant of six-lobed-cog-66a27160-f0ef-48c6-8ce3-c2ea9255ad5b-sub32; parent file remains unchanged.
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

class DrawingVariant2(Sub32):
    icon_id = 'six-lobed-cog-66a27160-f0ef-48c6-8ce3-c2ea9255ad5b-sub32-v2'
    variant_of = 'six-lobed-cog-66a27160-f0ef-48c6-8ce3-c2ea9255ad5b-sub32'
    variant_label = 'Broaden all six lobes with smooth symmetric curves'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('lobe-0', (16, 2), ((21, 2), (18, 9), (23, 9)))
        self.add_bezier('lobe-1', (23, 9), ((24, 9), (25, 6), (27, 6)))
        self.add_bezier('lobe-2', (27, 6), ((29, 6), (30, 8), (30, 10)))
        self.add_bezier('lobe-3', (30, 10), ((30, 13), (25, 13), (25, 16)))
        self.add_bezier('lobe-4', (25, 16), ((25, 19), (30, 19), (30, 22)))
        self.add_bezier('lobe-5', (30, 22), ((30, 24), (29, 26), (27, 26)))
        self.add_bezier('lobe-6', (27, 26), ((25, 26), (24, 23), (23, 23)))
        self.add_bezier('lobe-7', (23, 23), ((18, 23), (21, 30), (16, 30)))
        self.add_bezier('lobe-8', (16, 30), ((11, 30), (14, 23), (9, 23)))
        self.add_bezier('lobe-9', (9, 23), ((8, 23), (7, 26), (5, 26)))
        self.add_bezier('lobe-10', (5, 26), ((3, 26), (2, 24), (2, 22)))
        self.add_bezier('lobe-11', (2, 22), ((2, 19), (7, 19), (7, 16)))
        self.add_bezier('lobe-12', (7, 16), ((7, 13), (2, 13), (2, 10)))
        self.add_bezier('lobe-13', (2, 10), ((2, 8), (3, 6), (5, 6)))
        self.add_bezier('lobe-14', (5, 6), ((7, 6), (8, 9), (9, 9)))
        self.add_bezier('lobe-15', (9, 9), ((14, 9), (11, 2), (16, 2)))
        self.add_contour('cog', 'lobe-0', 'lobe-1', 'lobe-2', 'lobe-3', 'lobe-4', 'lobe-5', 'lobe-6', 'lobe-7', 'lobe-8', 'lobe-9', 'lobe-10', 'lobe-11', 'lobe-12', 'lobe-13', 'lobe-14', 'lobe-15', closed=True)
        self.add_line('axle', (16,15), (16,17))
        self.add_contour('center','axle',closed=False)
