"""Mechanical Robotic Hand. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '6444a5ca-ed45-4973-a423-c42fca7fd778'
SOURCE_PATH = 'pictographic-primitives/other/hand robot_6444a5ca-ed45-4973-a423-c42fca7fd778.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mechanical-robotic-hand-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'mechanical robotic hand')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_bezier('hand',(4,8),((12,6),(15,10),(23,13)),((29,14),(31,18),(29,22)),((34,17),(39,13),(42,16)),((47,21),(36,31),(32,35)),((25,42),(13,34),(4,32)))
        self.add_bezier('wrist',(4,32),((9,23),(9,17),(4,8)))
        self.add_contour('outline','hand','wrist',closed=True)
        self.add_polyline('palm',(17,12),(17,25),(29,28),(29,22))
        self.relate('connect','outline','palm')
