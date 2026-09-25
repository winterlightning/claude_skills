"""Happy face with tongue to the right. Circular face, arched eyes, curved smile and rounded tongue. No useful exact Lucide match. Open lower rim for the protruding tongue; keep deliberate tongue asymmetry.
Keyshape CIRCLE: exact SOLO48 envelope. Reviewer: clean centerlines and joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2b16bc0-fda9-42be-8b90-0bef7d9dc58b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/18-a2b16bc0-fda9-42be-8b90-0bef7d9dc58b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'happy-face-with-sideways-tongue'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('happy', 'face', 'with', 'sideways', 'tongue')

    def build(self):
        self.add_arc('face',(8,36),(40,36),radius_x=20,large_arc=True,sweep=True)
        for n,x in [('left',17),('right',31)]:
            self.add_arc(n+'-eye',(x-2,18),(x+2,18),radius_x=2,sweep=True)
        self.path('smile',(13,27),[((23,30),12,12,False),(31,27)])
        self.path('tongue',(23,30),[(23,38),((31,38),4,4,False),(31,27)])
        self.relate('connect','smile','tongue')

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
