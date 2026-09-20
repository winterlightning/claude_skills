# Variant of gas-symbol-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of gas-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'c6b95b7c-51f0-41d6-9758-e2c0e4821afa'
SOURCE_PATH = 'pictographic-primitives/symbol/gas_c6b95b7c-51f0-41d6-9758-e2c0e4821afa.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c6b95b7c-51f0-41d6-9758-e2c0e4821afa', 'pictographic-primitives/symbol/gas_c6b95b7c-51f0-41d6-9758-e2c0e4821afa.svg'),)
PROFILE_SOURCE_KEYS = ('solo/gas-symbol',)
SOLO_SOURCE_ICON_IDS = ('gas-symbol',)
REFERENCE_EXPORT_SHA256 = '66068ccf3c86165962d29426ca0212da0c787d24a2b3f1e5bf9195fb716a239c'

class DrawingVariant3(Sub32):
    icon_id = 'gas-symbol-sub32-v3'
    variant_of = 'gas-symbol-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Bottle body with rounded shoulders and a flat base; restore neck rim and remove the unsupported middle stripe.
        self.add_line('rim',(10,2),(22,2))
        self.add_line('neck-right',(20,2),(20,8))
        self.add_bezier('shoulder-right',(20,8),((24,8),(26,10),(26,14)))
        self.add_line('right',(26,14),(26,25))
        self.add_arc('br',(26,25),(21,30),radius_x=5,radius_y=5,sweep=True)
        self.add_line('base',(21,30),(11,30))
        self.add_arc('bl',(11,30),(6,25),radius_x=5,radius_y=5,sweep=True)
        self.add_line('left',(6,25),(6,14))
        self.add_bezier('shoulder-left',(6,14),((6,10),(8,8),(12,8)))
        self.add_line('neck-left',(12,8),(12,2))
        self.add_contour('bottle','neck-right','shoulder-right','right','br','base','bl','left','shoulder-left','neck-left')
        self.relate('connect','rim','neck-right');self.relate('connect','rim','neck-left')
