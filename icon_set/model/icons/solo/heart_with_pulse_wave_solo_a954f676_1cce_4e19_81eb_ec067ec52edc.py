"""Heart with Pulse Wave. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'a954f676-1cce-4e19-81eb-ec067ec52edc'
SOURCE_PATH = 'pictographic-primitives/health/heart rate_a954f676-1cce-4e19-81eb-ec067ec52edc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'heart-with-pulse-wave-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'heart with pulse wave')
    def build(self):
        self.add_arc('left-inner',(24,16),(14,8),radius_x=10,radius_y=8,sweep=False)
        self.add_arc('left-outer',(14,8),(4,18),radius_x=10,sweep=False)
        self.add_bezier('left-side',(4,18),((4,26),(16,35),(24,40)))
        self.add_bezier('right-side',(24,40),((32,35),(44,26),(44,18)))
        self.add_arc('right-outer',(44,18),(34,8),radius_x=10,sweep=False)
        self.add_arc('right-inner',(34,8),(24,16),radius_x=10,radius_y=8,sweep=False)
        self.add_contour('outline','left-inner','left-outer','left-side','right-side','right-outer','right-inner',closed=True)
        self.add_polyline('pulse',(6,25),(17,25),(22,17),(27,32),(31,25),(37,25))
        self.relate('connect','outline','pulse')
