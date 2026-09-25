"""Fresh batch-038 result for blank-face-wearing-monocle.
Plan: subject-owned contours and shared repeated parameters on the SOLO48 grid.
Keyshape CIRCLE: radial radius 22 about (24,24), cardinal ink extremes (2,2)-(46,46).
Source concept and arrangement: supplied reference SVG recorded below.
Lucide original and atomic-debug construction reference: glasses.
Human reference: human_ref/user.svg circular head; no torso/head-to-body gap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91ce291f-5576-4068-b370-5a46ca69845b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face monocle_91ce291f-5576-4068-b370-5a46ca69845b.svg'
AUTHOR = 'gpt-6'

class Batch038Icon(Solo48):
    icon_id = 'blank-face-wearing-monocle-batch038'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('blank', 'face', 'wearing', 'monocle')

    def build(self):

        def circle(name, cx, cy, r):
            self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
            self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def eye(name, x, y, up=False):
            self.add_arc(name, (x-2,y), (x+2,y), radius_x=2, radius_y=1, sweep=up)
        def mouth(y=32, sad=False, width=6, depth=2):
            self.add_arc('mouth',(24-width,y),(24+width,y),radius_x=width,radius_y=depth,sweep=sad)
        def drop(name,x,y):
            self.add_line(name+'-left',(x,y),(x-4,y+8))
            self.add_arc(name+'-base',(x-4,y+8),(x+4,y+8),radius_x=4,sweep=False)
            self.add_line(name+'-right',(x+4,y+8),(x,y))
            self.add_contour(name,name+'-left',name+'-base',name+'-right',closed=True)
        # Circular face interrupted at lower right for the hanging monocle cord.
        self.add_arc('face-top',(4,24),(44,24),radius_x=20)
        self.add_arc('face-bottom',(24,44),(4,24),radius_x=20)
        self.add_contour('face','face-bottom','face-top')
        circle('monocle',28,20,4)
        self.add_line('cord',(32,20),(32,42))
        self.relate('connect','cord','monocle')
