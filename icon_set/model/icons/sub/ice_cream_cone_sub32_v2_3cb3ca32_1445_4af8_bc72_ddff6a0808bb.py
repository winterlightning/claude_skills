# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of ice-cream-cone.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '3cb3ca32-1445-4af8-bc72-ddff6a0808bb'
SOURCE_PATH = 'pictographic-primitives/symbol/ice scream_3cb3ca32-1445-4af8-bc72-ddff6a0808bb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3cb3ca32-1445-4af8-bc72-ddff6a0808bb', 'pictographic-primitives/symbol/ice scream_3cb3ca32-1445-4af8-bc72-ddff6a0808bb.svg'),)
PROFILE_SOURCE_KEYS = ('solo/ice-cream-cone',)
SOLO_SOURCE_ICON_IDS = ('ice-cream-cone',)
REFERENCE_EXPORT_SHA256 = '3a8065d5d7f15afafa0a2d23f9c808bc0d95d2c5d74fed62eff3c1a289edd3d9'

class DrawingVariant2(Sub32):
    icon_id = 'ice-cream-cone-sub32-v2'
    variant_of = 'ice-cream-cone-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Central scoop and mirrored side lobes, with smooth shoulder transitions.
        self.add_arc('scoop',(9,9),(23,9),radius_x=7,radius_y=7,sweep=True)
        self.add_bezier('right-shoulder',(23,9),((23,11),(28,11),(28,14)))
        self.add_bezier('right-lobe',(28,14),((28,18),(26,20),(23,20)))
        self.add_bezier('right-base',(23,20),((20,20),(18,20),(16,18)))
        self.add_bezier('left-base',(16,18),((14,20),(12,20),(9,20)))
        self.add_bezier('left-lobe',(9,20),((6,20),(4,18),(4,14)))
        self.add_bezier('left-shoulder',(4,14),((4,11),(9,11),(9,9)))
        self.add_contour('scoops','scoop','right-shoulder','right-lobe','right-base','left-base','left-lobe','left-shoulder',closed=True)
        self.add_line('cone-left',(9,20),(16,30))
        self.add_line('cone-right',(16,30),(23,20))
        self.add_contour('cone','cone-left','cone-right',closed=False)
        for member in ['left-base','left-lobe']: self.relate('connect',member,'cone-left')
        for member in ['right-base','right-lobe']: self.relate('connect',member,'cone-right')
