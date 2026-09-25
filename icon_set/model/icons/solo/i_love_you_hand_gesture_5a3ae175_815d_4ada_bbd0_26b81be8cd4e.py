"""I love you hand sign: two extended fingers, folded middle/ring fingers and outward thumb. Lucide hand: equal round fingertips, tangent palm arcs. Omit tiny crease between folded fingers.
Keyshape VRECT_L: exact SOLO48 envelope. Reviewer: clean centerlines and joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5a3ae175-815d-4ada-bbd0-26b81be8cd4e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/wayfinding/sign language love_5a3ae175-815d-4ada-bbd0-26b81be8cd4e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'i-love-you-hand-gesture'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('i', 'love', 'you', 'hand', 'gesture')

    def build(self):
        self.path('hand',(8,30),[(8,16),((16,16),4,4,True),(16,25),(24,25),(24,8),((32,8),4,4,True),(32,28),(36,24),((40,28),4,4,True),(40,30),((26,44),14,14,True),(22,44),((8,30),14,14,True)],True)
        self.add_line('fold',(16,25),(16,32));self.relate('connect','hand','fold')

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
