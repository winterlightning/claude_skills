"""Index finger touching a smartphone. Lucide hand: rounded fingertip; rectangle-vertical: equal phone corner radii. Deliberate overlap at touch; omit hidden phone edge and minor fingers.
Keyshape SQUARE: exact SOLO48 envelope. Reviewer: clean centerlines and joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3730401c-4d35-4b72-a477-2313ba8f23f7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bendable phone touch_3730401c-4d35-4b72-a477-2313ba8f23f7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'index-finger-touching-a-phone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('index', 'finger', 'touching', 'a', 'phone')

    def build(self):
        self.path('phone',(18,42),[(10,42),((6,38),4,4,True),(6,10),((10,6),4,4,True),(18,6),((22,10),4,4,True),(22,18)])
        self.path('hand',(28,42),[(18,32),((24,26),5,5,True),(28,30),(22,18),((30,14),5,5,True),(36,28),(42,28),(42,36),((36,42),6,6,True),(28,42)],True)
        self.relate('connect','phone','hand')

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
        # Identical supporting palms mirrored about x24; vertical to horizontal tangent quarters.
        for n,s in [('left',1),('right',-1)]:
            def p(x,y):return (24+s*(x-24),y)
            self.path(n+'-hand',p(6,30),[p(6,32),(p(16,42),10,10,s<0),p(20,42)])
