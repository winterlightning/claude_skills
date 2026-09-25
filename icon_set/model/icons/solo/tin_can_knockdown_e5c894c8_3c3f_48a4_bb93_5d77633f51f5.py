"""Tin Can Knockdown Game.
Plan: Three cans are a joined physical stack, with shared stack seam and curved lower can bases. Ball is separate at upper right. Centerline extremes (4,8)-(44,40).
Reference: No useful Lucide can-stack match; shared stack seams and circular ball.
Reduction: Motion dashes and elliptical can lips omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5c894c8-3c3f-48a4-bb93-5d77633f51f5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/hit the can_e5c894c8-3c3f-48a4-bb93-5d77633f51f5.svg'
AUTHOR = 'gpt-6'


class Batch25Icon(Solo48):
    icon_id = 'tin-can-knockdown'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    aliases = ()
    keywords = ('tin', 'can', 'knockdown', 'game')

    def build(self):
        self.add_polyline('lower-left',(14,24),(4,24),(4,36))
        self.add_arc('base-left',(4,36),(20,36),radius_x=8,radius_y=4,sweep=False)
        self.add_arc('base-right',(20,36),(36,36),radius_x=8,radius_y=4,sweep=False)
        self.add_polyline('lower-right',(36,36),(36,24),(26,24))
        self.relate('connect','lower-left','base-left')
        self.relate('connect','base-left','base-right')
        self.relate('connect','base-right','lower-right')
        self.add_line('top-left',(14,24),(14,16))
        self.add_arc('can-top',(14,16),(26,16),radius_x=6,radius_y=4)
        self.add_line('top-right',(26,16),(26,24))
        self.add_contour('top-can','top-left','can-top','top-right')
        self.add_polyline('seam',(14,24),(20,24),(26,24))
        self.add_line('division',(20,24),(20,36))
        for a,b in (('top-can','lower-left'),('top-can','lower-right'),('top-can','seam'),('seam','division'),('base-left','division'),('base-right','division'),('lower-left','seam'),('lower-right','seam')):
            self.relate('connect',a,b)
        self.add_arc('ball-top',(36,12),(44,12),radius_x=4)
        self.add_arc('ball-bottom',(44,12),(36,12),radius_x=4)
        self.add_contour('ball','ball-top','ball-bottom',closed=True)
