"""Fresh batch-038 result for smiling-face-with-cheek-tear.
Plan: subject-owned contours and shared repeated parameters on the SOLO48 grid.
Keyshape CIRCLE: radial radius 22 about (24,24), cardinal ink extremes (2,2)-(46,46).
Source concept and arrangement: supplied reference SVG recorded below.
Lucide original and atomic-debug construction reference: face-slightly-smiling.
Human reference: human_ref/user.svg circular head; no torso/head-to-body gap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0d6e2fe5-d4d4-4167-8084-dc07c804ecc1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face grin tears_0d6e2fe5-d4d4-4167-8084-dc07c804ecc1.svg'
AUTHOR = 'gpt-6'

class Batch038Icon(Solo48):
    icon_id = 'smiling-face-with-cheek-tear-batch038'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/expressions" 
    aliases = ()
    keywords = ('smiling', 'face', 'with', 'cheek', 'tear')

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
        # Happy eyes and asymmetric smile leave room for one cheek tear trail.
        circle('face',24,24,20)
        for i,x in enumerate((18,30)):
            eye('closed-eye-'+str(i),x,17,True)
        self.add_arc('smile',(16,28),(24,33),radius_x=9,sweep=False)
        self.add_line('tear',(33,26),(33,29))
