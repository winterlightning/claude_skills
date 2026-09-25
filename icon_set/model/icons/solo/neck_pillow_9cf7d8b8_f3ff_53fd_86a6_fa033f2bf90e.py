"""neck-pillow: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9cf7d8b8-f3ff-53fd-86a6-fa033f2bf90e'
SOURCE_PATH = 'pictographic-primitives/travel/neck pillow_9cf7d8b8-f3ff-53fd-86a6-fa033f2bf90e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class NeckPillow(Solo48):
    icon_id = 'neck-pillow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    categories = ('travel', 'primitives')
    aliases = ()
    keywords = ('neck', 'pillow', 'travel')

    def build(self):
        # Plan: HRECT_L; exact mirrored arms, smooth crown and round ends; preserve the U opening.
        # Reference: Geometric paired curves; no useful neck-pillow reference.
        self.add_bezier('outer-left',(14,40),((7,40),(4,30),(4,24)),((4,13),(13,8),(24,8)))
        self.add_bezier('outer-right',(24,8),((35,8),(44,13),(44,24)),((44,30),(41,40),(34,40)))
        self.add_bezier('right-tip',(34,40),((31,40),(29,38),(29,35)),((29,32),(32,28),(32,24)))
        self.add_bezier('inner',(32,24),((32,20),(28,18),(24,18)),((20,18),(16,20),(16,24)))
        self.add_bezier('left-tip',(16,24),((16,28),(19,32),(19,35)),((19,38),(17,40),(14,40)))
        self.add_contour('outline','outer-left','outer-right','right-tip','inner','left-tip',closed=True)
