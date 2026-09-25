# Variant of open-full-torso-person-sub; parent file remains unchanged.
"""Simple User Profile Icon: complete-source SUB32 candidate."""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '53c3e6a6-c8a3-4333-b0db-0f7f9d33f82c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/full body person 1_53c3e6a6-c8a3-4333-b0db-0f7f9d33f82c.svg'
AUTHOR = 'gpt-6'
USER_APPROVED_HEAD_BODY_CONTACT = True

class DrawingVariant2(Sub32):
    icon_id = 'open-full-torso-person-sub-v2'
    variant_of = 'open-full-torso-person-sub'
    variant_label = 'Larger body with user-authorized head contact'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'

    def build(self):
        # User explicitly permits head/body contact. Use one genuine head/shoulder junction at (16,10).
        # Circular head (16,6), r=4; upper torso rises to the bottom of the head.
        self.add_arc('head-top',(12,6),(20,6),radius_x=4)
        self.add_arc('head-bottom-right',(20,6),(16,10),radius_x=4)
        self.add_arc('head-bottom-left',(16,10),(12,6),radius_x=4)
        self.add_contour('head','head-top','head-bottom-right','head-bottom-left',closed=True)
        self.add_polyline('left-body',(10,30),(9,22),(4,22))
        self.add_bezier('shoulder-left',(4,22),((4,14),(9,10),(16,10)))
        self.add_bezier('shoulder-right',(16,10),((23,10),(28,14),(28,22)))
        self.add_polyline('right-body',(28,22),(23,22),(22,30))
        self.add_contour('torso','left-body-1','left-body-2','shoulder-left','shoulder-right','right-body-1','right-body-2')
        self.contours=[c for c in self.contours if c.contour_id not in ('left-body','right-body')]
        self.relate('connect','head','torso')
