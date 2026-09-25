"""Open palm beneath a ball. Lucide hand-helping: long palm and curled thumb. Smooth round finger cap, larger round ball, intentional directional asymmetry. Minor finger seams omitted.
Keyshape SQUARE: exact SOLO48 envelope. Reviewer: clean centerlines and joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '46422cf0-a3b3-428d-86b8-b42d41fd1deb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/catch_46422cf0-a3b3-428d-86b8-b42d41fd1deb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-hand-beneath-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('open', 'hand', 'beneath', 'ball')

    def build(self):
        self.circle('ball',26,11,5)
        self.path('thumb',(6,31),[(13,26),((19,24),10,10,True),(23,24),((23,32),4,4,True),(18,32)])
        self.path('palm',(6,42),[(27,42),(40,32),((34,24),5,5,False),(23,32)])
        self.relate('connect','thumb','palm')

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
