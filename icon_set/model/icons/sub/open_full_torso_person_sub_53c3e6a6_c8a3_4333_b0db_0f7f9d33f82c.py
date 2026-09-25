"""Simple User Profile Icon: complete-source SUB32 candidate."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '53c3e6a6-c8a3-4333-b0db-0f7f9d33f82c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/full body person 1_53c3e6a6-c8a3-4333-b0db-0f7f9d33f82c.svg'
AUTHOR = 'gpt-6'

class Drawing(Sub32):
    icon_id = 'open-full-torso-person-sub'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'

    def build(self):

        # Shared human_ref/user.svg proportions: round head and broad shoulders.
        # Head bottom y=10, shoulders y=18: 8 centerline / 4 visible gap.
        # Keep the original's open bottom and both tapered torso sides.
        cx, cy, r = 16, 6, 4
        self.add_arc('head-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc('head-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_polyline('left-body',(11,30),(10,24),(6,24))
        self.add_bezier('shoulders',(6,24),((6,18),(10,18),(16,18)),((22,18),(26,18),(26,24)))
        self.add_polyline('right-body',(26,24),(22,24),(21,30))
        self.add_contour('torso','left-body-1','left-body-2','shoulders','right-body-1','right-body-2')
        self.contours = [c for c in self.contours if c.contour_id not in ('left-body','right-body')]

