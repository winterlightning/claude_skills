"""Independent 32px profile of six-lobed-cog-66a27160-f0ef-48c6-8ce3-c2ea9255ad5b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '66a27160-f0ef-48c6-8ce3-c2ea9255ad5b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_66a27160-f0ef-48c6-8ce3-c2ea9255ad5b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('66a27160-f0ef-48c6-8ce3-c2ea9255ad5b', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_66a27160-f0ef-48c6-8ce3-c2ea9255ad5b.svg'), ('e3d63c1e-a685-484b-8eae-ef88e3411b1e', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_e3d63c1e-a685-484b-8eae-ef88e3411b1e.svg'))
PROFILE_SOURCE_KEYS = ('solo/six-lobed-cog-66a27160-f0ef-48c6-8ce3-c2ea9255ad5b', 'solo/six-lobed-cog-e3d63c1e-a685-484b-8eae-ef88e3411b1e')
SOLO_SOURCE_ICON_IDS = ('six-lobed-cog-66a27160-f0ef-48c6-8ce3-c2ea9255ad5b', 'six-lobed-cog-e3d63c1e-a685-484b-8eae-ef88e3411b1e')
REFERENCE_EXPORT_SHA256 = 'de2b86749ce5a30a52bed4e6b5975351feba0d38cc4c88e8fe073bde0fb9c4ab'

class DrawingVariant2ContainerSymbol(Sub32):
    icon_id = 'six-lobed-cog-66a27160-f0ef-48c6-8ce3-c2ea9255ad5b-sub32-v2-symbol'
    related_origin_icon_id = 'six-lobed-cog-66a27160-f0ef-48c6-8ce3-c2ea9255ad5b-sub32-v2'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/six-lobed-cog-66a27160-f0ef-48c6-8ce3-c2ea9255ad5b-sub32-v2'
    counterpart_icon_id = 'six-lobed-cog-66a27160-f0ef-48c6-8ce3-c2ea9255ad5b-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Six trapezoid teeth that taper enough to keep the 4-unit rule, small closed centre hole.
        self.add_polyline('gear', (20, 6), (18, 2), (14, 2), (12, 6), (10, 7), (5, 7), (2, 11), (5, 15), (5, 17), (2, 21), (5, 25), (10, 25), (12, 26), (14, 30), (18, 30), (20, 26), (22, 25), (27, 25), (30, 21), (27, 17), (27, 15), (30, 11), (27, 7), (22, 7), closed=True)
        self.add_arc('hole-top', (14, 16), (18, 16), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('hole-bottom', (18, 16), (14, 16), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('hole', 'hole-top', 'hole-bottom', closed=True)
