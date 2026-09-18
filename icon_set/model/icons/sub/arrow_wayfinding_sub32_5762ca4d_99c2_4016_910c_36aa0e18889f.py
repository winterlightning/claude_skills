"""Independent 32px profile of arrow-wayfinding.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '5762ca4d-99c2-4016-910c-36aa0e18889f'
SOURCE_PATH = 'pictographic-primitives/wayfinding/arrow_5762ca4d-99c2-4016-910c-36aa0e18889f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5762ca4d-99c2-4016-910c-36aa0e18889f', 'pictographic-primitives/wayfinding/arrow_5762ca4d-99c2-4016-910c-36aa0e18889f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-wayfinding',)
SOLO_SOURCE_ICON_IDS = ('arrow-wayfinding',)
REFERENCE_EXPORT_SHA256 = 'fb7ca096e67a76ab9545e9bb995029cc04dc63104de961ddeb74587322372691'

class Drawing(Sub32):
    icon_id = 'arrow-wayfinding-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'wayfinding'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (17, 5), (22, 5))
        self.add_bezier('p1-r1-2', (22, 5), ((27, 5), (30, 8), (30, 13)))
        self.add_bezier('p1-r1-3', (30, 13), ((30, 17), (27, 20), (22, 20)))
        self.add_line('p1-r1-4', (22, 20), (2, 20))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (9, 13), (2, 20))
        self.add_line('p2-r1-2', (2, 20), (9, 27))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-2')
