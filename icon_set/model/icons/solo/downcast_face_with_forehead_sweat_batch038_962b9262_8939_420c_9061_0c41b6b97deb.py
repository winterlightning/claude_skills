"""Fresh batch-038 result for downcast-face-with-forehead-sweat.
Plan: subject-owned contours and shared repeated parameters on the SOLO48 grid.
Keyshape SQUARE: ink extremes (4,4)-(44,44).
Source concept and arrangement: supplied reference SVG recorded below.
Lucide original and atomic-debug construction reference: face-slightly-frowning.
Human reference: human_ref/user.svg circular head; no torso/head-to-body gap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '962b9262-8939-420c-9061-0c41b6b97deb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face downcast sweat_962b9262-8939-420c-9061-0c41b6b97deb.svg'
AUTHOR = 'gpt-6'

class Batch038Icon(Solo48):
    icon_id = 'downcast-face-with-forehead-sweat-batch038'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('downcast', 'face', 'with', 'forehead', 'sweat')

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
        # Interrupted forehead leaves the sweat droplet its own clear opening.
        self.add_arc('face-a',(24,6),(6,24),radius_x=18,sweep=False)
        self.add_arc('face-b',(6,24),(24,42),radius_x=18,sweep=False)
        self.add_arc('face-c',(24,42),(40,34),radius_x=20,sweep=False)
        self.add_contour('face','face-a','face-b','face-c')
        drop('sweat',38,6)
        eye('eye-left',17,22)
        eye('eye-right',29,24)
        self.add_arc('mouth',(19,32),(23,32),radius_x=2,radius_y=1)
