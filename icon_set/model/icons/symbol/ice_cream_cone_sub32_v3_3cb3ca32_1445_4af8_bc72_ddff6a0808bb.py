"""Independent 32px profile of ice-cream-cone.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '3cb3ca32-1445-4af8-bc72-ddff6a0808bb'
SOURCE_PATH = 'pictographic-primitives/symbol/ice scream_3cb3ca32-1445-4af8-bc72-ddff6a0808bb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3cb3ca32-1445-4af8-bc72-ddff6a0808bb', 'pictographic-primitives/symbol/ice scream_3cb3ca32-1445-4af8-bc72-ddff6a0808bb.svg'),)
PROFILE_SOURCE_KEYS = ('solo/ice-cream-cone',)
SOLO_SOURCE_ICON_IDS = ('ice-cream-cone',)
REFERENCE_EXPORT_SHA256 = '3a8065d5d7f15afafa0a2d23f9c808bc0d95d2c5d74fed62eff3c1a289edd3d9'

class DrawingVariant3(Sub32):
    icon_id = 'ice-cream-cone-sub32-v3'
    related_origin_icon_id = 'ice-cream-cone-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('dome', (10, 8), (22, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_bezier('shoulder-right', (22, 8), ((22, 10), (26, 10), (26, 12)))
        self.add_arc('lobe-right', (26, 12), (22, 16), radius_x=4, radius_y=4, sweep=True)
        self.add_line('rim', (22, 16), (10, 16))
        self.add_arc('lobe-left', (10, 16), (6, 12), radius_x=4, radius_y=4, sweep=True)
        self.add_bezier('shoulder-left', (6, 12), ((6, 10), (10, 10), (10, 8)))
        self.add_contour('scoop', 'dome', 'shoulder-right', 'lobe-right', 'rim', 'lobe-left', 'shoulder-left', closed=True)
        self.add_polyline('cone', (10, 16), (16, 30), (22, 16))
        self.relate('connect', 'cone', 'scoop')
