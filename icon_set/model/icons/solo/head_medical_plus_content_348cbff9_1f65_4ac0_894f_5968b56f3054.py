"""Side-profile head with medical plus. Smooth circular cranium, deliberate nose corner and rounded chin; neck stays open. Human reference informs minimal anatomy. No useful exact Lucide profile match.
Keyshape VRECT_L: exact SOLO48 envelope. Reviewer: clean centerlines and joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '348cbff9-1f65-4ac0-894f-5968b56f3054'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/348cbff9-1f65-4ac0-894f-5968b56f3054.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'head-medical-plus-content'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    aliases = ()
    keywords = ('head', 'medical', 'plus', 'content')

    def build(self):
        self.path('head',(12,44),[(12,34),((8,22),20,20,True),(8,18),((22,4),14,14,True),((36,18),14,14,True),(40,26),(34,28),(34,32),((30,36),4,4,True),(28,36),(28,44)])
        self.add_polyline('plus-horizontal',(17,20),(22,20),(27,20))
        self.add_polyline('plus-vertical',(22,15),(22,20),(22,25))
        self.relate('connect','plus-horizontal','plus-vertical')

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
