"""circle-messages-bubble: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f97107e-f15e-42cb-ae76-2769af6c5f64'
SOURCE_PATH = 'pictographic-primitives/other/circle messages bubble_5f97107e-f15e-42cb-ae76-2769af6c5f64.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class CircleMessagesBubble(Solo48):
    icon_id = 'circle-messages-bubble'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('circle', 'messages', 'bubble', 'other')

    def build(self):
        # HRECT_L (4,8)-(44,40); smooth oval with a distinct tail.
        # Construction reference: Lucide message-circle: coherent bubble and purposeful tail
        self.add_bezier('upper-left',(4,23),((4,15),(13,8),(24,8)))
        self.add_bezier('upper-right',(24,8),((35,8),(44,15),(44,23)))
        self.add_bezier('lower-right',(44,23),((44,31),(35,38),(24,38)),((20,38),(17,37),(15,36)))
        self.add_polyline('tail',(15,36),(6,40),(10,32))
        self.add_bezier('lower-left',(10,32),((6,30),(4,27),(4,23)))
        self.add_contour('outline','upper-left','upper-right','lower-right','tail-1','tail-2','lower-left',closed=True)
        self.contours.pop(0)
