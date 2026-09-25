"""Fresh batch-038 result for worried-face-with-tiny-eyes.
Plan: subject-owned contours and shared repeated parameters on the SOLO48 grid.
Keyshape CIRCLE: radial radius 22 about (24,24), cardinal ink extremes (2,2)-(46,46).
Source concept and arrangement: supplied reference SVG recorded below.
Lucide original and atomic-debug construction reference: face-slightly-frowning.
Human reference: human_ref/user.svg circular head; no torso/head-to-body gap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '93741e67-dd2f-4f00-9273-2a6a575b45aa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face frown_93741e67-dd2f-4f00-9273-2a6a575b45aa.svg'
AUTHOR = 'gpt-6'

class Batch038Icon(Solo48):
    icon_id = 'worried-face-with-tiny-eyes-batch038'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('worried', 'face', 'with', 'tiny', 'eyes')

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
        circle('face',24,24,20)
        # Three feature rows share a central axis and 9-unit vertical spacing.
        for i,x in enumerate((18,30)):
            self.add_dot('eye-'+str(i),(x,24))
        self.add_line('brow-left',(18,16),(20,14))
        self.add_line('brow-right',(28,14),(30,16))
        mouth(34,True,4,3)
