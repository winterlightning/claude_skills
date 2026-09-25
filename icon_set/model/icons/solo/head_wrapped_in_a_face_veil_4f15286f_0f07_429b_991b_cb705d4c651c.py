"""Head wrapped in niqab: smooth round hood, broad exposed eye strip, lower veil draping to shoulder. Human user reference supplies head proportions; reference preserves covering. Omit small fold.
Keyshape VRECT_L: exact SOLO48 envelope. Reviewer: clean centerlines and joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4f15286f-0f07-429b-991b-cb705d4c651c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/avatar islamic women niqab 2_4f15286f-0f07-429b-991b-cb705d4c651c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'head-wrapped-in-a-face-veil'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('head', 'wrapped', 'in', 'a', 'face', 'veil')

    def build(self):
        # Round hood and lower face loop; the two mantle ends extend naturally outward.
        self.path('hood',(10,28),[(10,18),((24,4),14,14,True),((38,18),14,14,True),(38,28),((24,42),14,14,True),((10,28),14,14,True)],True)
        self.add_line('brow',(10,18),(38,18));self.relate('connect','hood','brow')
        self.path('veil',(10,28),[((38,28),14,5,False)])
        self.relate('connect','hood','veil')
        self.add_line('mantle-left',(8,44),(10,28));self.relate('connect','mantle-left','hood');self.relate('connect','mantle-left','veil')
        self.add_line('mantle-right',(38,28),(40,44));self.relate('connect','mantle-right','hood');self.relate('connect','mantle-right','veil')

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
