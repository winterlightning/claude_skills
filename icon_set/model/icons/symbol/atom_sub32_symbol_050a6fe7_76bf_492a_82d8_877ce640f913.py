"""Independent 32px profile of atom.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '050a6fe7-76bf-492a-82d8-877ce640f913'
SOURCE_PATH = 'pictographic-primitives/symbol/atom_050a6fe7-76bf-492a-82d8-877ce640f913.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('050a6fe7-76bf-492a-82d8-877ce640f913', 'pictographic-primitives/symbol/atom_050a6fe7-76bf-492a-82d8-877ce640f913.svg'),)
PROFILE_SOURCE_KEYS = ('solo/atom',)
SOLO_SOURCE_ICON_IDS = ('atom',)
REFERENCE_EXPORT_SHA256 = '9fe04446709f1a61123d5f896fda56386268bffbc787cd15296091c6295b2839'

class DrawingContainerSymbol(Sub32):
    icon_id = 'atom-sub32-symbol'
    related_origin_icon_id = 'atom-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/atom-sub32'
    counterpart_icon_id = 'atom-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Atom: two crossing orbits (exact ellipses), 8 units apart where they part.
        self.add_arc('orbit-h-1', (2, 16), (30, 16), radius_x=14, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('orbit-h-2', (30, 16), (2, 16), radius_x=14, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('orbit-h', 'orbit-h-1', 'orbit-h-2', closed=True)
        self.add_arc('orbit-v-1', (16, 2), (16, 30), radius_x=6, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('orbit-v-2', (16, 30), (16, 2), radius_x=6, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('orbit-v', 'orbit-v-1', 'orbit-v-2', closed=True)
        self.relate('connect', 'orbit-h', 'orbit-v')
