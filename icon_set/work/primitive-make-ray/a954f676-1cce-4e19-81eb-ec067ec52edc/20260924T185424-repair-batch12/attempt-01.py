"""Heart with Pulse Wave. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._payments_batch01 import circle, rounded_rect
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
        self.add_bezier('left-shoulder',(4,18),((4,20),(5,22),(6,24)))
        self.add_bezier('left-side',(6,24),((10,30),(16,35),(24,40)))
        self.add_bezier('right-side',(24,40),((32,35),(38,30),(42,24)))
        self.add_bezier('right-shoulder',(42,24),((43,22),(44,20),(44,18)))
        self.add_arc('right-outer',(44,18),(34,8),radius_x=10,sweep=False)
        self.add_arc('right-inner',(34,8),(24,16),radius_x=10,radius_y=8,sweep=False)
        self.add_contour('outline','left-inner','left-outer','left-shoulder','left-side','right-side','right-shoulder','right-outer','right-inner',closed=True)
        self.add_polyline('pulse',(6,24),(16,24),(20,17),(24,28),(28,24),(32,24))
        self.relate('connect','outline','pulse')
