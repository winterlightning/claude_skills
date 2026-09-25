"""Front car above mirrored cupped hands. Lucide car-front: trapezoidal windshield and rounded body. Omit lamps and mirrors for clearance.
Keyshape SQUARE: exact SOLO48 envelope. Reviewer: clean centerlines and joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f7acffbb-95f3-4cdd-98e2-2243774f9339'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/car insurance hands_f7acffbb-95f3-4cdd-98e2-2243774f9339.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hands-supporting-front-facing-car'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('hands', 'supporting', 'front', 'facing', 'car')

    def build(self):
        self.path('car',(14,14),[(17,6),(31,6),(34,14),(34,20),((32,22),2,2,True),(16,22),((14,20),2,2,True),(14,14)],True)
        self.add_line('windshield',(14,14),(34,14));self.relate('connect','car','windshield')
        for n,x in [('left',20),('right',28)]:
            self.add_line(n+'-tire',(x,22),(x,24));self.relate('connect','car',n+'-tire')
        self.cups()

    def path(self, name, start, steps, closed=False):
        members=[]; here=start
        for j,step in enumerate(steps):
            eid=f'{name}-{j}'
            if len(step)==2:
                self.add_line(eid,here,step); end=step
            else:
                end,rx,ry,sweep=step
                self.add_arc(eid,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
            members.append(eid);here=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)

    def cups(self):
        # Mirrored hands about x24; equal fingertip radii and tangent S-curves into the wrists.
        for n,s in [('left',1),('right',-1)]:
            def p(x,y):return (24+s*(x-24),y)
            self.path(n+'-hand',p(10,42),[(p(6,34),10,10,s>0),p(6,33),(p(14,33),4,4,s>0),(p(16,35),2,2,s<0),(p(18,37),2,2,s>0),p(18,42)])
