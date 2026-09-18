"""Hand Pointing at 3D Cube. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'ec7d49e5-85a7-4bad-943c-fff9ce408048'
SOURCE_PATH = 'pictographic-primitives/state/hand point cube_ec7d49e5-85a7-4bad-943c-fff9ce408048.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-pointing-at-3d-cube-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'hand pointing at 3d cube')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_polyline('cube',(24,6),(42,14),(42,28),(31,34),(31,20),(24,16),(24,6),(31,10),(42,14),(31,20))
        self.add_bezier('finger',(6,42),((4,36),(10,33),(13,37)))
        self.add_line('finger-left',(13,37),(13,27))
        self.add_arc('tip',(13,27),(21,27),radius_x=4)
        self.add_polyline('hand',(21,27),(21,36),(25,36),(27,42))
        self.relate('connect','finger','finger-left','tip','hand')
