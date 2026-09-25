"""Smiling short-haired boy bust. Shared user.svg head/shoulder proportions: circular jaw radius12 at24,16, shoulder top36; exact4 visible detached gap. Hair drawn as a smoothly parted crown; no cramped enclosed fringe band, smile as circular arc. Eyes omitted for spacing.
Keyshape VRECT_L: exact SOLO48 envelope. Reviewer: clean centerlines and joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f01e448f-89f4-4275-bd9a-ab35d0b89a80'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/45-f01e448f-89f4-4275-bd9a-ab35d0b89a80.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smiling-short-hair-boy-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('smiling', 'short', 'hair', 'boy', 'bust')

    def build(self):
        # Circular jaw r12, center24,16; jaw bottom28 and shoulder top36: exact4 visible gap.
        self.add_arc('jaw',(12,16),(36,16),radius_x=12,sweep=False)
        self.add_bezier('hair',(12,16),((12,9),(16,4),(22,4)),((25,4),(27,8),(30,8)),((33,8),(36,11),(36,16)))
        self.relate('connect','hair','jaw')
        self.add_arc('smile',(21,18),(27,18),radius_x=5,sweep=False)
        self.path('shoulders',(8,44),[((16,36),8,8,True),(32,36),((40,44),8,8,True)])

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
