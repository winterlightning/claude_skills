"""American Football Ball.

Plan: Four tangent circular arcs form a broad diagonal ball with three stitches; square extrema 6,6–42,42.
Construction reference: circle (local original and atomic-debug inspected).
Simplification: Lacing reduced to three; outline broadened for legal seam clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f1d3889-db71-4132-bcfc-995f498530ae'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/rugby_5f1d3889-db71-4132-bcfc-995f498530ae.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'diagonal-rugby-ball-with-lacing'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('american', 'football', 'ball')

    def build(self):
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)

        def rect(name, left, top, right, bottom, r=2):
            pts=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
            members=[]
            for j,a in enumerate(pts):
                b=pts[(j+1)%8]; eid=f'{name}-{j}'; members.append(eid)
                if j%2: self.add_arc(eid,a,b,radius_x=r)
                else: self.add_line(eid,a,b)
            self.add_contour(name,*members,closed=True)

        self.add_arc('outline-upper',(6,32),(32,6),radius_x=26)
        self.add_arc('cap-upper',(32,6),(42,16),radius_x=10)
        self.add_arc('outline-lower',(42,16),(16,42),radius_x=26)
        self.add_arc('cap-lower',(16,42),(6,32),radius_x=10)
        self.add_contour('outline','outline-upper','cap-upper','outline-lower','cap-lower',closed=True)
        self.add_polyline('seam',(16,32),(18,30),(24,24),(30,18),(32,16))
        for j,c in enumerate((18,24,30)):
            self.add_polyline(f'lace-{j}',(c-2,48-c-2),(c,48-c),(c+2,48-c+2))
            self.relate('connect','seam',f'lace-{j}')
