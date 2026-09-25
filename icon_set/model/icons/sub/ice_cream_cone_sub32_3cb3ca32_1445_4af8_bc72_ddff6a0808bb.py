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

class Drawing(Sub32):
    icon_id = 'ice-cream-cone-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (9, 9), (23, 9), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (23, 9), (23, 19), radius_x=4, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (23, 19), (16, 17), radius_x=6, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 17), (9, 19), radius_x=6, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (9, 19), (9, 9), radius_x=4, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (9, 19), (16, 30))
        self.add_line('p2-r1-2', (16, 30), (23, 19))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-2')
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
