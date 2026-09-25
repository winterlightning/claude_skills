"""Fresh batch-038 result for smiling-face-with-round-glasses.
Plan: subject-owned contours and shared repeated parameters on the SOLO48 grid.
Keyshape HRECT_L: ink extremes (2,6)-(46,42).
Source concept and arrangement: supplied reference SVG recorded below.
Lucide original and atomic-debug construction reference: glasses.
Human reference: human_ref/user.svg circular head; no torso/head-to-body gap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac229f1d-eac6-45e2-958d-ac9a8938b1af'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face glasses_ac229f1d-eac6-45e2-958d-ac9a8938b1af.svg'
AUTHOR = 'gpt-6'

class Batch038Icon(Solo48):
    icon_id = 'smiling-face-with-round-glasses-batch038'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('smiling', 'face', 'with', 'round', 'glasses')

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
        # Paired equal round lenses and one connected bridge; no head outline in source.
        for i,x in enumerate((12,36)):
            circle('lens-'+str(i),x,16,8)
        self.add_line('bridge',(20,16),(28,16))
        self.relate('connect','bridge','lens-0')
        self.relate('connect','bridge','lens-1')
        self.add_arc('smile',(14,34),(34,34),radius_x=10,radius_y=6,sweep=False)
